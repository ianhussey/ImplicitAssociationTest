########################################################################
# Calculate D1 scores and summary statistics
########################################################################
# Author: 
# Ian Hussey (ian.hussey@ugent.be)

# Notes:
# Does not contain produce data for the assessment of internal 
# consistency, due to the heterogeneity in how different researchers
# tend to calculate this. For example, split-half D1 scores from odd- 
# and even- trials by order of presentation; split-half D1 scores from 
# blocks 3/6 vs. 4/7; split-half D1 scores from first versus half of 
# each block; or various uses of cronbach's alpha.

# Known issues:
# None.

# Instructions:
# Simply set the input [line containing setwd()] and output 
# [line containing write.csv()] directories and run script.

########################################################################
# Clean workspace
########################################################################
rm(list=ls())

########################################################################
# Dependencies
########################################################################
library(plyr) #must import before dplyr
library(dplyr)
library(tidyr)
library(readr)
library(data.table)

########################################################################
# Data acquisition and cleaning
########################################################################
# Set the working directory in which to look for data files, then read them in.
setwd("~/git/IAT/data")
files <- list.files(pattern = "\\.csv$")  # Create a list of the csv files in this folder
df <- tbl_df(rbind.fill(lapply(files, fread, header=TRUE)))

# Make some variable names more transparent, plus rectify the the accuracy variable
df <- 
  rename(df,
         block = blocks.thisN, # current block
         trial = trials.thisN, # trial order of presentation within each block
         rt = requiredResponse.rt, # first correct response rt
         accuracy = feedbackResponse.corr, # accuracy of the first response (currently reversed: 0 = correct)
         trial = trials.thisN) %>% # trial by order of presentation within each block
  mutate(accuracy = abs(accuracy - 1), # recitfies the direction of accuracy so that 0 = error and 1 = correct.
         block = block + 1) # recifies block to be 1 to 7 rather than 0-6

########################################################################
# Extract demographics data
demographics_data <-
  select(df,
         participant,
         gender,
         age,
         expName,
         date) %>%
  distinct(participant)

########################################################################
# IAT D1 scores
D1_df <-  
  group_by(df, participant) %>%
  filter(rt <= 10000) %>%
  summarize(RT_block3_m = mean(rt[block == 3]),  # blocks 3 and 6
            RT_block6_m = mean(rt[block == 6]),
            RT_block3and6_SD = sd(rt[block == 3 | block == 6]),
            RT_block4_m = mean(rt[block == 4]),  # blocks 4 and 7
            RT_block7_m = mean(rt[block == 7]),
            RT_block4and7_SD = sd(rt[block == 4 | block == 7])) %>%
  mutate(difference_a = RT_block6_m - RT_block3_m,
         D1a = difference_a / RT_block3and6_SD,
         difference_b = RT_block7_m - RT_block4_m,
         D1b = difference_b / RT_block4and7_SD,
         IAT_D1 = round((D1a + D1b)/2, 2)) %>%
  select(participant, IAT_D1)

# by trial type
D1_TT_df <-
  group_by(df, participant, trial_type) %>%
  filter(rt <= 10000) %>%
  summarize(
    # blocks 3 and 6
    RT_block3_m = mean(rt[block == 3]), 
    RT_block6_m = mean(rt[block == 6]),
    RT_block3and6_SD = sd(rt[block == 3 | block == 6]),
    # blocks 4 and 7
    RT_block4_m = mean(rt[block == 4]), 
    RT_block7_m = mean(rt[block == 7]),
    RT_block4and7_SD = sd(rt[block == 4 | block == 7])
  ) %>%
  mutate(difference_a = RT_block6_m - RT_block3_m,
         D1a = difference_a / RT_block3and6_SD,
         difference_b = RT_block7_m - RT_block4_m,
         D1b = difference_b / RT_block4and7_SD,
         IAT_D1 = round((D1a + D1b)/2, 2),
         TT = trial_type) %>%
  select(participant, 
         IAT_D1,
         TT) %>%
  spread(TT, IAT_D1) %>%
  rename(IAT_D1_trial_type_1 = `1`,
         IAT_D1_trial_type_2 = `2`,
         IAT_D1_trial_type_3 = `3`,
         IAT_D1_trial_type_4 = `4`)

########################################################################
# Accuracy and latency stats
accuracy_summary_df <- 
  group_by(df, participant) %>%
  summarize(critical_blocks_percentage_accuracy = round(sum(accuracy[block == 3 |
                                                                    block == 4 | 
                                                                    block == 6 | 
                                                                    block == 7]) / 120, 2)) # 120 critical trials in the IAT

df$fast_trial <- ifelse(df$rt < .3, 1, 0)  # add new column that records if RT < 300. Should probably be done using mutate() for code consistency, but this works fine.

latency_summary_df <-
  group_by(df, participant) %>%
  filter(block == 3 | block == 4 | block == 6 | block == 7) %>%
  summarize(critical_blocks_mean_rt = round(mean(rt), 2), 
            percent_fast_trials = sum(fast_trial)/120) %>%  # 120 critical trials
  mutate(exclude_based_on_fast_trials = ifelse(percent_fast_trials>=0.1, TRUE, FALSE)) %>%  # exclusions based on too many fast trials is part of the D1 algorithm
  select(participant,
         critical_blocks_mean_rt,
         exclude_based_on_fast_trials)

########################################################################
# Join data frames
all_tasks_df <- 
  join_all(list(demographics_data,
                accuracy_summary_df,
                latency_summary_df,
                D1_df,
                D1_TT_df),
           by = "participant",
           type = "full")

########################################################################
# Write to file
write.csv(all_tasks_df, file = '~/git/IAT/data processing/IAT_data.csv', row.names=FALSE)

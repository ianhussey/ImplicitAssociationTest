########################################################################
# Calculate D1 scores and summary statistics
########################################################################
# Author: 
# Ian Hussey (ian.hussey@ugent.be)

# Notes:
# Internal reliability of the IAT is be assessed via heterogeneous 
# methods across papers. The current script produces an overall D1 score 
# for analysis, as well as D1 scores for blocks 3/6 (D1a) and 4/7 (D1b) 
# for the calculation of split-half D1 scores, e.g., using spearman brown 
# correlations or cronbach's alpha.

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
library(tidyverse)
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
         IAT_D1a = difference_a / RT_block3and6_SD,
         difference_b = RT_block7_m - RT_block4_m,
         IAT_D1b = difference_b / RT_block4and7_SD,
         IAT_D1 = round((IAT_D1a + IAT_D1b)/2, 2),
         block_order = (participant - 1) %% 2 + 1, # set block order based on modulus of the participant code, as in the psychopy script 
         IAT_D1 = ifelse(block_order == 1, IAT_D1,  # D1 score rectifications for block order. if ==2, invert D1 score
                         ifelse(block_order == 2, IAT_D1 * -1, "error"))) %>%
  select(participant, IAT_D1, IAT_D1a, IAT_D1b)

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
                D1_df),
           by = "participant",
           type = "full")

########################################################################
# Write to file
write.csv(all_tasks_df, file = '~/git/IAT/data processing/IAT_data.csv', row.names=FALSE)


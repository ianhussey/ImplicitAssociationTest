########################################################################
# Create summary stats and D scores from data produced by the 
# Implicit Association Test 
# as programmed in PsychoPy 1.82
# Ian.Hussey@ugent.be
########################################################################
# Notes:

# Likert calculations need independant validation
# Doesn't include reliability analysis

########################################################################
# Clean the workspace

rm(list=ls())

########################################################################
# Dependencies

library(plyr) #must import before dplyr
library(dplyr)
library(tidyr)
library(readr)
library(stringr)
library(data.table)

########################################################################
# Data acquisition and cleaning

# Set the working directory in which to look for data files
setwd("~/git/IAT/data")

# Create a list of these files
files <- list.files()
# Read these files into a single dplyr-style data frame. You can remove the tbl_df() to get a standard data frame if you prefer.
df <- tbl_df(rbind.fill(lapply(files, fread, header=TRUE)))

# Make some variable names more transparent, plus rectify the the accuracy variable
df <- 
  rename(
    df,
    blocks = blocks.thisN, # current block within a given task
    trial = trials.thisN, # trial order of presentation within each block
    rt = requiredResponse.rt, # first correct response rt
    #accuracy = feedbackResponse.corr # This is what would normally be used. However, some mistake in psychopy means
    # that all are recorded as wrong. The workaround is to use the presence of a feedbackResponse RT as an incorrect response.
    emmittedWrongAnswer = feedbackResponse.rt
  ) %>% # accuracy of the first response (currently reversed: 0 = correct)
  
  mutate(
    #accuracy = abs(accuracy - 1), # recitfies the direction of accuracy so that 0 = error and 1 = correct. #see above, 
    # this is broken because of a psychopy error. Instead, derive accuracy from the presence of feedback rts:
    accuracy = ifelse(is.na(emmittedWrongAnswer), 1, 0), 
    blocks = blocks + 1 
  ) # recifites block to be 1 to 7 rather than 0-6

########################################################################
# Data processing

df_output <-
  
  group_by(
    df,
    participant
  ) %>%
  
  ## D scores
  summarize(
    # mean RT in the critical blocks 
    criticalBlocksMeanRT = mean(rt[blocks == 3 | blocks == 4 | blocks == 6 | blocks == 7]),
    
    # D score blocks 3 and 6
    RT_block3_m = mean(rt[blocks == 3]), 
    RT_block6_m = mean(rt[blocks == 6]),
    difference1 = RT_block6_m - RT_block3_m,
    RT_block3and6_SD = sd(rt[blocks == 3 | blocks == 6]),
    D1a = difference1 / RT_block3and6_SD, #check that D1 is the correct name for this version of D?
    
    # D score blocks 4 and 7
    RT_block4_m = mean(rt[blocks == 4]), 
    RT_block7_m = mean(rt[blocks == 7]),
    difference2 = RT_block7_m - RT_block4_m,
    RT_block4and7_SD = sd(rt[blocks == 4 | blocks == 7]),
    D1b = difference2 / RT_block4and7_SD #check that D1 is the correct name for this version of D?
  ) %>%
  
  # Calculate D1
  mutate(
    D1 = (D1a + D1b)/2
  ) %>%
  
  # Add the condition variable
  # Condition is set by the modulo of the participant code within the task, but I forgot to write it out to the data file.
  mutate(
    condition = (participant - 1)%%4 + 1 # sets condition to between 1 and 4
  ) %>%
  
  # Recitfy the directionality of the D scores for block order B. 
  mutate(
    D1a = ifelse(condition == 2, D1a *-1, ifelse(condition == 1, D1a, 'inversion error')),
    D1b = ifelse(condition == 2, D1b *-1, ifelse(condition == 1, D1b, 'inversion error')),
    D1 = ifelse(condition == 2, D1 *-1, ifelse(condition == 1, D1, 'inversion error'))
  ) %>%

  # ADD RELIABILITY ANALYSIS HERE IN THE FUTURE
 
  # Select only the key columns
  select(
    participant,
    D1a,
    D1b,
    D1,
    condition,
    criticalBlocksMeanRT
  )

# Accuracy summary
# This code works, but the actual task isn't recording incorrect answers at all!!
df2 <- 
  filter(df, !is.na(rt)) %>% 

  group_by(participant) %>%
  
  summarize(
    criticalBlocksPercentageAccuracy = sum(accuracy[blocks == 3 | blocks == 4 | blocks == 6 | blocks == 7]) / 120 # 120 criticatl trials
  )

# Join the data frames
df_output <-
  full_join(df_output, df2, by = "participant")

# Extract demographics data
df3 <-
  select(
    df,
    participant,
    gender,
    age,
    expName,
    date
  ) %>%
  
  distinct(
    participant
  )

# Join the data frames
df_output <-
  full_join(df_output, df3, by = "participant")

# Write to file
write.csv(df_output, file = "~/git/IAT/processed_IAT_data.csv", row.names=FALSE)

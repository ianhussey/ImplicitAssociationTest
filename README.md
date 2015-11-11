# Implicit Association Test written in PsychoPy

## License
Copyright Ian Hussey (ian.hussey@ugent.be)

Distributed under an MIT license.

## Version
0.9.1 (19/10/2015)

## Notes
- The current version does not allow you to alter the order of block presentation within the task (e.g., whether participants get flowers good or insects good first). If you want a version with the alternative block order, you can create a second copy of the task folder and use the alternative stimulus file. E.g., replace the stimuli.xlsx and Instructions.xlsx files with the one in the "Alternative block order files" folder. Future versions might make this possible with a preparatory loop, but it’s more effort than it’s worth right now. The openIAT allows for this based on the "order" variable in the dialogue menu participants are presented with before the task, but it's far easier to implement there because the task uses free responding rather than contingent responding.  
- The escape key quits the task at any time. E, I, or the return key ends the task properly once it’s complete.
- You can run either the psyexp file or the py file inside psychopy. The py file should have greater cross platform support; if you run into errors with the psyexp file use the py instead.
- psydat and csv files are produced for each participant. csv file alone is sufficient to most analyses (e.g., calculation of D scores).
- All stimuli and instructions can be altered by editing the excel files. Indeed, all strings presented within the task are variables, so translating the task into other languages only requires changes to the stimuli and instructions files.
- Block length is a function of the number of rows in the stimuli.xlsx file. In order to retain the desired block lengths (e.g., 20 in the first block), 5 exemplars are needed per trial-type. If you wish to use more exemplars per trial-type this will need code changes; probably an overhaul of how each stimulus pool is sampled.
- ITI is set to 250 ms (see Nosek et al., 2007: the IAT at age 7).
- D scores can be calculated by examining the means and standard deviations of the block1.rt to block7.rt variables in the output files, and accuracy stats from the block1wrong.corr to block7wrong.corr variables. NB: the 1s refer to incorrect answers rather than correct answers as might be expected.

# Block layout
The current version follows the block layout described in Nosek et al. (2007: the IAT at age 7).

5 exemplars per stimulus class. Changing this would require us to add trial counters and “loop.finished = true” code snippets in order to preserve block lengths.

- Block 1 (categories) 20 Trials (2 loops of 10)
- Block 2 (attributes) 20 Trials (2 loops of 10)
- Block 3 (both) 20 Trials (1 loops of 20)
- Block 4 (both) 40 Trials (2 loops of 20)
- Block 5 (categories reversed) 40 Trials (4 loops of 10)
- Block 6 (both reversed) 20 Trials (1 loops of 20)
- Block 7 (both reversed) 40 Trials (2 loops of 20)

## Known issues
1. If participants get 100% of trials correct on either blocks 3&4 or 6&7 then one of two incorrect response RT columns will not be created for that participant. However, this is not a problem if you merge files across participants based on column header matching (e.g., using dplyr’s `rbind_list()` command). However, it can be problematic if your data processing workflow relies on column ORDER rather than column header NAME, e.g., a SPSS script using a GET command.

## Changelog
0.9.1
- changed the instuctions1and5 from "is trials" = true to "is trials" = false so that a superfluous line is not recorded in the data file.
- changed the endLoop from is trials" = true to "is trials" = false so that a superfluous line is not recorded in the data file.
- until now, trial blocks 3&4 and 6&7 used the same routines (repsectively) because the contents of these blocks' trials was identical. However, it makes for easier analysis if the data is output in different columns.
- renamed keyboard components in trial blocks to blockX and blockXwrong. When combined with the above, D scores can be calculated by examining the means and standard deviations of the block1.rt to block7.rt variables, and accuracy exclusions from the block1wrong.corr to block7wrong.corr variables. NB here, the 1s refer to incorrect answers rather than correct answers. The variables specified in the code components for accuracy feedback were also changed appropriately.

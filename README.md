# Implicit Association Test written in PsychoPy

## License
Copyright Ian Hussey (ian.hussey@ugent.be)

Distributed under an MIT license.

## Version
0.9.2 (11/11/2015)
Written in PsychoPy 1.82.01

## Notes
- High fidelity to the IAT procedure described in Nosek et al. (2007: the IAT at 7) and to the standard IAT script provided by Millisecond for Inquisit. IMHO, fidelity is higher than other freely available alternatives, such as the FreeIAT or OpenIAT (e.g., the latter has a different block layout, and also uses a combination of free responding and accuracy feedback, where the IAT almost invariably uses one or the other but not both).
- The order of presentation of blocks within the task (e.g., whether participants get death-self or life-self first) is determined by the "block order" variable in the popup box. Use "1" or "2". 
- The escape key quits the task at any time. E, I, or the return key ends the task properly once it’s complete.
- You can run either the psyexp file or the py file inside psychopy. The py file should have greater cross platform support; if you run into errors with the psyexp file use the py instead.
- psydat and csv files are produced for each participant. csv file alone is sufficient to most analyses (e.g., calculation of D scores).
- All stimuli and instructions can be altered by editing the excel files. Indeed, all strings presented within the task are variables, so translating the task into other languages only requires changes to the stimuli and instructions files. NB there are several empty cells in the blockOrder files: these actually contain a single space, as PsychoPy will crash if variables are left unspecified.
- Block length is a function of the number of rows in the stimuli.xlsx file. In order to retain the desired block lengths (e.g., 20 in the first block), 5 exemplars/rows must be used per category. If you wish to use more exemplars per trial-type this will need code changes; probably an overhaul of how each stimulus pool is sampled.
- ITI is set to 250 ms (see Nosek et al., 2007: the IAT at age 7).
- D scores can be calculated by examining the means and standard deviations of the block1.rt to block7.rt variables in the output files, and accuracy stats from the block1wrong.corr to block7wrong.corr variables. NB: the 1s refer to incorrect answers rather than correct answers as might be expected.

# Block layout
The current version follows the block layout described in Nosek et al. (2007: the IAT at age 7). The contents of each screen follows the standard Inquisit IAT very closely. However, the Inquisit IAT uses the older block layout of 20 trials in block 5.

5 exemplars per stimulus category. Changing this would require us to add trial counters and “loop.finished = true” code snippets in order to preserve block lengths.

- Block 1 (categories) 20 Trials (2 loops of 10)
- Block 2 (attributes) 20 Trials (2 loops of 10)
- Block 3 (both) 20 Trials (1 loops of 20)
- Block 4 (both) 40 Trials (2 loops of 20)
- Block 5 (categories reversed) 40 Trials (4 loops of 10)
- Block 6 (both reversed) 20 Trials (1 loops of 20)
- Block 7 (both reversed) 40 Trials (2 loops of 20)

## Known issues
1. If participants get 100% of trials correct throughout the whole task then three incorrect response columns will not be created for that participant. This is highly unlikely, and futhermore is not a problem if your data processing workflow merges data files across participants based on column header names (e.g., using dplyr’s `rbind_list()` command) rather than positions (e.g., a SPSS script using a GET command, or some other R commands which assume equivalene table shapes).

## Changelog
0.9.2

- Rewritten from scratch to make the data files follow Hadley Wickham's Tidy Data standards. Loops now include nested references to the stimuli files, thus allowing for a highly simplified flow and greatly decreased number of routines. The py script has also gone from 3250 lines to 450, and is far more readable. However, this change shifts complexity to the stimulus files: there are now 12 where there were 2. 
- This rewriting also allowed me to add the ability to choose the block order based on a variable entered in the popup before the experiment (i.e., block order: 1 vs 2).

0.9.1

- changed the instuctions1and5 from "is trials" = true to "is trials" = false so that a superfluous line is not recorded in the data file.
- changed the endLoop from is trials" = true to "is trials" = false so that a superfluous line is not recorded in the data file.
- until now, trial blocks 3&4 and 6&7 used the same routines (repsectively) because the contents of these blocks' trials was identical. However, it makes for easier analysis if the data is output in different columns.
- renamed keyboard components in trial blocks to blockX and blockXwrong. When combined with the above, D scores can be calculated by examining the means and standard deviations of the block1.rt to block7.rt variables, and accuracy exclusions from the block1wrong.corr to block7wrong.corr variables. NB here, the 1s refer to incorrect answers rather than correct answers. The variables specified in the code components for accuracy feedback were also changed appropriately.

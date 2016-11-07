#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Mon Nov  7 14:58:58 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'IAT'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
# Dependencies
import itertools  # for flattening lists of lists into lists
import random
import math  # for math.ceil() rounding up

# Import stimuli exemplars
exemplars_filename = 'stimuli.xlsx'
exemplars = data.importConditions(exemplars_filename)# Import stimuli exemplars

# Determine rows of examplars (i.e., max number of rows)
"""
This method creates a fully counterbalanced presentation of exemplars when there are 5
of them, but it will not present each one an equal number of times it the n diverges from 5.
"""
n_exemplars = len(exemplars)
list_multiplier = int(math.ceil(10/n_exemplars))  # math.ceil() rounds up. 10 is the derived from way block lengths are calculated. Admittedly, this comment doensn't adequately document why it's ten. Honestly, I have to work it out of my fingers every time and can't explain it.

# Trial generation function
def generate_trials(trial_type_column, multiplier):
    """Generate a shuffled list of stimuli exemplars from a column in an excel stimuli file""" 
    a = dict()  # declare a dict to be populated
    for i in range(len(exemplars)):
        a[i] = [exemplars[i][trial_type_column]] * multiplier  # populate the dict from vertical reads of the conditions
    a = a.values()  # extract only values (and not keys) from the list of dicts
    a = list(itertools.chain(*a))  # flatten the list of dicts into a list
    random.shuffle(a)  # shuffle this list, so that it can be drawn from by the trials
    return a

# declare trial rows (not sure if necessary, but can't be bothered to removed and test)
trial_rows = ""

# set block order based on participant code
participantNumber = int(expInfo['participant'])
if (participantNumber % 2) == 1: 
    block_order = 1
elif (participantNumber % 2) == 0:
    block_order = 2
else:
    print "****condition file error: please enter a numeric participant code****"

instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
leftCategoryLabel_2 = visual.TextStim(win=win, ori=0, name='leftCategoryLabel_2',
    text='default text',    font=u'Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)
rightCategoryLabel_2 = visual.TextStim(win=win, ori=0, name='rightCategoryLabel_2',
    text='default text',    font=u'Arial',
    pos=[.6, .85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
leftAttributeLabel_2 = visual.TextStim(win=win, ori=0, name='leftAttributeLabel_2',
    text='default text',    font=u'Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-5.0)
rightAttributeLabel_2 = visual.TextStim(win=win, ori=0, name='rightAttributeLabel_2',
    text='default text',    font=u'Arial',
    pos=[.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-6.0)
orLeft_2 = visual.TextStim(win=win, ori=0, name='orLeft_2',
    text='default text',    font=u'Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-7.0)
orRight_2 = visual.TextStim(win=win, ori=0, name='orRight_2',
    text='default text',    font=u'Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-8.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
#declare accuracy feedback message variable
msg=""
stimulusImageBox = visual.ImageStim(win=win, name='stimulusImageBox',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=.6,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
stimulusTextBox = visual.TextStim(win=win, ori=0, name='stimulusTextBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0)
feedback = visual.TextStim(win=win, ori=0, name='feedback',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-5.0)
leftCategoryLabel = visual.TextStim(win=win, ori=0, name='leftCategoryLabel',
    text='default text',    font=u'Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0)
rightCategoryLabel = visual.TextStim(win=win, ori=0, name='rightCategoryLabel',
    text='default text',    font=u'Arial',
    pos=[.6, .85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-7.0)
leftAttributeLabel = visual.TextStim(win=win, ori=0, name='leftAttributeLabel',
    text='default text',    font=u'Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-8.0)
rightAttributeLabel = visual.TextStim(win=win, ori=0, name='rightAttributeLabel',
    text='default text',    font=u'Arial',
    pos=[.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-9.0)
orLeft = visual.TextStim(win=win, ori=0, name='orLeft',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0)
orRight = visual.TextStim(win=win, ori=0, name='orRight',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0)

# Initialize components for Routine "end"
endClock = core.Clock()
endBox = visual.TextStim(win=win, ori=0, name='endBox',
    text='End of the task',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    #------Prepare to start Routine "instruction"-------
    t = 0
    instructionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # set the block length and the rows to pull from based on the current block 
    # this layout follows Nosek et al. 2007, "The Implicit Association Test at age 7: A methodological and conceptual review"
    if blocks.thisN == 0:
        trial_rows = "0:2" 
        n_block_repeats = 10   #2*10 = 20 trials
        modified_list_multiplier = list_multiplier
    elif blocks.thisN == 1:
        trial_rows = "2:4" 
        n_block_repeats = 10   #2*10 = 20 trials
        modified_list_multiplier = list_multiplier
    elif blocks.thisN == 2:
        trial_rows = "0:4" 
        n_block_repeats = 5   #4*5 = 20 trials
        modified_list_multiplier = list_multiplier
    elif blocks.thisN == 3:
        trial_rows = "0:4" 
        n_block_repeats = 10   #4*10 = 40 trials
        modified_list_multiplier = list_multiplier
    elif blocks.thisN == 4:
        trial_rows = "0:2" 
        n_block_repeats = 20   #2*20 = 40 trials
        modified_list_multiplier = list_multiplier * 2  # because this block has a different trials:categories ratio
    elif blocks.thisN == 5:
        trial_rows = "0:4" 
        n_block_repeats = 5   #4*5 = 20 trials
        modified_list_multiplier = list_multiplier
    elif blocks.thisN == 6:
        trial_rows = "0:4" 
        n_block_repeats = 10   #4*10 = 40 trials
        modified_list_multiplier = list_multiplier
    
    # Generate list of stimuli for the block
    text_trial_type_1_trials = generate_trials('text_trial_type_1_exemplars', modified_list_multiplier)  # function and variable determined at begin exp.
    text_trial_type_2_trials = generate_trials('text_trial_type_2_exemplars', modified_list_multiplier)
    text_trial_type_3_trials = generate_trials('text_trial_type_3_exemplars', modified_list_multiplier)
    text_trial_type_4_trials = generate_trials('text_trial_type_4_exemplars', modified_list_multiplier)
    img_trial_type_1_trials = generate_trials('img_trial_type_1_exemplars', modified_list_multiplier)
    img_trial_type_2_trials = generate_trials('img_trial_type_2_exemplars', modified_list_multiplier)
    img_trial_type_3_trials = generate_trials('img_trial_type_3_exemplars', modified_list_multiplier)
    img_trial_type_4_trials = generate_trials('img_trial_type_4_exemplars', modified_list_multiplier)
    
    # set category and attribute labels based on the block order and current block
    if block_order == 1 and blocks.thisN <= 3:
        leftCategory = categoryA
        rightCategory = categoryB
    elif block_order == 1 and blocks.thisN > 3:
        leftCategory = categoryB
        rightCategory = categoryA
    elif block_order == 2 and blocks.thisN <= 3:
        leftCategory = categoryB
        rightCategory = categoryA
    elif block_order == 2 and blocks.thisN > 3:
        leftCategory = categoryA
        rightCategory = categoryB
    instructionsBox.setText(instructions)
    instructionsKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
    instructionsKey.status = NOT_STARTED
    leftCategoryLabel_2.setText(leftCategory)
    rightCategoryLabel_2.setText(rightCategory)
    leftAttributeLabel_2.setText(leftAttribute)
    rightAttributeLabel_2.setText(rightAttribute)
    orLeft_2.setText(orStimulus)
    orRight_2.setText(orStimulus)
    # keep track of which components have finished
    instructionComponents = []
    instructionComponents.append(instructionsBox)
    instructionComponents.append(instructionsKey)
    instructionComponents.append(leftCategoryLabel_2)
    instructionComponents.append(rightCategoryLabel_2)
    instructionComponents.append(leftAttributeLabel_2)
    instructionComponents.append(rightAttributeLabel_2)
    instructionComponents.append(orLeft_2)
    instructionComponents.append(orRight_2)
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instruction"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *instructionsBox* updates
        if t >= 0.75 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *instructionsKey* updates
        if t >= 2.75 and instructionsKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsKey.tStart = t  # underestimates by a little under one frame
            instructionsKey.frameNStart = frameN  # exact frame index
            instructionsKey.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if instructionsKey.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *leftCategoryLabel_2* updates
        if t >= 0.75 and leftCategoryLabel_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftCategoryLabel_2.tStart = t  # underestimates by a little under one frame
            leftCategoryLabel_2.frameNStart = frameN  # exact frame index
            leftCategoryLabel_2.setAutoDraw(True)
        
        # *rightCategoryLabel_2* updates
        if t >= 0.75 and rightCategoryLabel_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightCategoryLabel_2.tStart = t  # underestimates by a little under one frame
            rightCategoryLabel_2.frameNStart = frameN  # exact frame index
            rightCategoryLabel_2.setAutoDraw(True)
        
        # *leftAttributeLabel_2* updates
        if t >= 0.75 and leftAttributeLabel_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftAttributeLabel_2.tStart = t  # underestimates by a little under one frame
            leftAttributeLabel_2.frameNStart = frameN  # exact frame index
            leftAttributeLabel_2.setAutoDraw(True)
        
        # *rightAttributeLabel_2* updates
        if t >= 0.75 and rightAttributeLabel_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightAttributeLabel_2.tStart = t  # underestimates by a little under one frame
            rightAttributeLabel_2.frameNStart = frameN  # exact frame index
            rightAttributeLabel_2.setAutoDraw(True)
        
        # *orLeft_2* updates
        if t >= 0.75 and orLeft_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeft_2.tStart = t  # underestimates by a little under one frame
            orLeft_2.frameNStart = frameN  # exact frame index
            orLeft_2.setAutoDraw(True)
        
        # *orRight_2* updates
        if t >= 0.75 and orRight_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRight_2.tStart = t  # underestimates by a little under one frame
            orRight_2.frameNStart = frameN  # exact frame index
            orRight_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instruction"-------
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=n_block_repeats, method='fullRandom', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('block_layout.xlsx', selection=trial_rows),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        # choose a random exemplar from the appropriate trial type list
        if trial_type == 1:
            text_stimulus = text_trial_type_1_trials.pop()
            image_stimulus = img_trial_type_1_trials.pop()
        elif trial_type == 2:
            text_stimulus = text_trial_type_2_trials.pop()
            image_stimulus = img_trial_type_2_trials.pop()
        elif trial_type == 3:
            text_stimulus = text_trial_type_3_trials.pop()
            image_stimulus = img_trial_type_3_trials.pop()
        elif trial_type == 4:
            text_stimulus = text_trial_type_4_trials.pop()
            image_stimulus = img_trial_type_4_trials.pop()
        
        # set stimulus colors based on trial type
        if trial_type == 1 or trial_type == 2:
             stimulusColor = [1, 1, 1]
        elif trial_type >2:
             stimulusColor = [-1, 1, -1]
        
        # set required and feedback responses
        # attributes are invariate across blocks so can be determined based on trial type only
        if trial_type == 3: #pos
            requiredAllowed = "i"
            requiredCorrect = "i"
            feedbackAllowed = "e"
            feedbackCorrect = "e"
        elif trial_type == 4: #neg
            requiredAllowed = "e"
            requiredCorrect = "e"
            feedbackAllowed = "i"
            feedbackCorrect = "i"
        # categories depend on block order, current block and trial type
        if block_order == 1: 
            if blocks.thisN <= 3:
                if trial_type == 1: #flowers
                    requiredAllowed = "i"
                    requiredCorrect = "i"
                    feedbackAllowed = "e"
                    feedbackCorrect = "e"
                elif trial_type == 2: #insects
                    requiredAllowed = "e"
                    requiredCorrect = "e"
                    feedbackAllowed = "i"
                    feedbackCorrect = "i"
            elif blocks.thisN >= 3:
                if trial_type == 1: #flowers
                    requiredAllowed = "e"
                    requiredCorrect = "e"
                    feedbackAllowed = "i"
                    feedbackCorrect = "i"
                elif trial_type == 2: #insects
                    requiredAllowed = "i"
                    requiredCorrect = "i"
                    feedbackAllowed = "e"
                    feedbackCorrect = "e"
        elif block_order == 2: 
            if blocks.thisN <= 3:
                if trial_type == 1: #flowers
                    requiredAllowed = "e"
                    requiredCorrect = "e"
                    feedbackAllowed = "i"
                    feedbackCorrect = "i"
                elif trial_type == 2: #insects
                    requiredAllowed = "i"
                    requiredCorrect = "i"
                    feedbackAllowed = "e"
                    feedbackCorrect = "e"
            elif blocks.thisN >= 3:
                if trial_type == 1: #flowers
                    requiredAllowed = "i"
                    requiredCorrect = "i"
                    feedbackAllowed = "e"
                    feedbackCorrect = "e"
                elif trial_type == 2: #insects
                    requiredAllowed = "e"
                    requiredCorrect = "e"
                    feedbackAllowed = "i"
                    feedbackCorrect = "i"
        stimulusImageBox.setImage(image_stimulus)
        stimulusTextBox.setColor(stimulusColor, colorSpace='rgb')
        stimulusTextBox.setText(text_stimulus)
        requiredResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        requiredResponse.status = NOT_STARTED
        feedbackResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        feedbackResponse.status = NOT_STARTED
        leftCategoryLabel.setText(leftCategory)
        rightCategoryLabel.setText(rightCategory)
        leftAttributeLabel.setText(leftAttribute)
        rightAttributeLabel.setText(rightAttribute)
        orLeft.setText(orStimulus)
        orRight.setText(orStimulus)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(stimulusImageBox)
        trialComponents.append(stimulusTextBox)
        trialComponents.append(requiredResponse)
        trialComponents.append(feedbackResponse)
        trialComponents.append(feedback)
        trialComponents.append(leftCategoryLabel)
        trialComponents.append(rightCategoryLabel)
        trialComponents.append(leftAttributeLabel)
        trialComponents.append(rightAttributeLabel)
        trialComponents.append(orLeft)
        trialComponents.append(orRight)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if len(feedbackResponse.keys)<1:
                msg=""
            else:
                msg="X"
            
            # *stimulusImageBox* updates
            if t >= 0.3 and stimulusImageBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusImageBox.tStart = t  # underestimates by a little under one frame
                stimulusImageBox.frameNStart = frameN  # exact frame index
                stimulusImageBox.setAutoDraw(True)
            
            # *stimulusTextBox* updates
            if t >= 0.3 and stimulusTextBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusTextBox.tStart = t  # underestimates by a little under one frame
                stimulusTextBox.frameNStart = frameN  # exact frame index
                stimulusTextBox.setAutoDraw(True)
            
            # *requiredResponse* updates
            if t >= 0.3 and requiredResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                requiredResponse.tStart = t  # underestimates by a little under one frame
                requiredResponse.frameNStart = frameN  # exact frame index
                requiredResponse.status = STARTED
                # AllowedKeys looks like a variable named `requiredAllowed`
                if not 'requiredAllowed' in locals():
                    logging.error('AllowedKeys variable `requiredAllowed` is not defined.')
                    core.quit()
                if not type(requiredAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(requiredAllowed, basestring):
                        logging.error('AllowedKeys variable `requiredAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in requiredAllowed: requiredAllowed = (requiredAllowed,)
                    else:  requiredAllowed = eval(requiredAllowed)
                # keyboard checking is just starting
                requiredResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if requiredResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=list(requiredAllowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if requiredResponse.keys == []:  # then this was the first keypress
                        requiredResponse.keys = theseKeys[0]  # just the first key pressed
                        requiredResponse.rt = requiredResponse.clock.getTime()
                        # was this 'correct'?
                        if (requiredResponse.keys == str(requiredCorrect )) or (requiredResponse.keys == requiredCorrect ):
                            requiredResponse.corr = 1
                        else:
                            requiredResponse.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *feedbackResponse* updates
            if t >= .3 and feedbackResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackResponse.tStart = t  # underestimates by a little under one frame
                feedbackResponse.frameNStart = frameN  # exact frame index
                feedbackResponse.status = STARTED
                # AllowedKeys looks like a variable named `feedbackAllowed`
                if not 'feedbackAllowed' in locals():
                    logging.error('AllowedKeys variable `feedbackAllowed` is not defined.')
                    core.quit()
                if not type(feedbackAllowed) in [list, tuple, np.ndarray]:
                    if not isinstance(feedbackAllowed, basestring):
                        logging.error('AllowedKeys variable `feedbackAllowed` is not string- or list-like.')
                        core.quit()
                    elif not ',' in feedbackAllowed: feedbackAllowed = (feedbackAllowed,)
                    else:  feedbackAllowed = eval(feedbackAllowed)
                # keyboard checking is just starting
                feedbackResponse.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if feedbackResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=list(feedbackAllowed))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if feedbackResponse.keys == []:  # then this was the first keypress
                        feedbackResponse.keys = theseKeys[0]  # just the first key pressed
                        feedbackResponse.rt = feedbackResponse.clock.getTime()
                        # was this 'correct'?
                        if (feedbackResponse.keys == str(feedbackCorrect )) or (feedbackResponse.keys == feedbackCorrect ):
                            feedbackResponse.corr = 1
                        else:
                            feedbackResponse.corr = 0
            
            # *feedback* updates
            if t >= .3 and feedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback.tStart = t  # underestimates by a little under one frame
                feedback.frameNStart = frameN  # exact frame index
                feedback.setAutoDraw(True)
            if feedback.status == STARTED:  # only update if being drawn
                feedback.setText(msg, log=False)
            
            # *leftCategoryLabel* updates
            if t >= 0 and leftCategoryLabel.status == NOT_STARTED:
                # keep track of start time/frame for later
                leftCategoryLabel.tStart = t  # underestimates by a little under one frame
                leftCategoryLabel.frameNStart = frameN  # exact frame index
                leftCategoryLabel.setAutoDraw(True)
            
            # *rightCategoryLabel* updates
            if t >= 0.0 and rightCategoryLabel.status == NOT_STARTED:
                # keep track of start time/frame for later
                rightCategoryLabel.tStart = t  # underestimates by a little under one frame
                rightCategoryLabel.frameNStart = frameN  # exact frame index
                rightCategoryLabel.setAutoDraw(True)
            
            # *leftAttributeLabel* updates
            if t >= 0.0 and leftAttributeLabel.status == NOT_STARTED:
                # keep track of start time/frame for later
                leftAttributeLabel.tStart = t  # underestimates by a little under one frame
                leftAttributeLabel.frameNStart = frameN  # exact frame index
                leftAttributeLabel.setAutoDraw(True)
            
            # *rightAttributeLabel* updates
            if t >= 0.0 and rightAttributeLabel.status == NOT_STARTED:
                # keep track of start time/frame for later
                rightAttributeLabel.tStart = t  # underestimates by a little under one frame
                rightAttributeLabel.frameNStart = frameN  # exact frame index
                rightAttributeLabel.setAutoDraw(True)
            
            # *orLeft* updates
            if t >= 0.0 and orLeft.status == NOT_STARTED:
                # keep track of start time/frame for later
                orLeft.tStart = t  # underestimates by a little under one frame
                orLeft.frameNStart = frameN  # exact frame index
                orLeft.setAutoDraw(True)
            
            # *orRight* updates
            if t >= 0.0 and orRight.status == NOT_STARTED:
                # keep track of start time/frame for later
                orRight.tStart = t  # underestimates by a little under one frame
                orRight.frameNStart = frameN  # exact frame index
                orRight.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if requiredResponse.keys in ['', [], None]:  # No response was made
           requiredResponse.keys=None
           # was no response the correct answer?!
           if str(requiredCorrect ).lower() == 'none': requiredResponse.corr = 1  # correct non-response
           else: requiredResponse.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('requiredResponse.keys',requiredResponse.keys)
        trials.addData('requiredResponse.corr', requiredResponse.corr)
        if requiredResponse.keys != None:  # we had a response
            trials.addData('requiredResponse.rt', requiredResponse.rt)
        # check responses
        if feedbackResponse.keys in ['', [], None]:  # No response was made
           feedbackResponse.keys=None
           # was no response the correct answer?!
           if str(feedbackCorrect ).lower() == 'none': feedbackResponse.corr = 1  # correct non-response
           else: feedbackResponse.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('feedbackResponse.keys',feedbackResponse.keys)
        trials.addData('feedbackResponse.corr', feedbackResponse.corr)
        if feedbackResponse.keys != None:  # we had a response
            trials.addData('feedbackResponse.rt', feedbackResponse.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed n_block_repeats repeats of 'trials'
    
# completed 1 repeats of 'blocks'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(3.750000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(endBox)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endBox* updates
    if t >= 0.75 and endBox.status == NOT_STARTED:
        # keep track of start time/frame for later
        endBox.tStart = t  # underestimates by a little under one frame
        endBox.frameNStart = frameN  # exact frame index
        endBox.setAutoDraw(True)
    if endBox.status == STARTED and t >= (0.75 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        endBox.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


win.close()
core.quit()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Wed Nov 11 18:30:48 2015
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
expInfo = {u'gender': u'', u'age': u'', u'participant': u'', u'block order': u'1', u'group': u''}
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
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsBox = visual.TextStim(win=win, ori=0, name='instructionsBox',
    text='default text',    font='Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
target1box_inst = visual.TextStim(win=win, ori=0, name='target1box_inst',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
target2box_inst = visual.TextStim(win=win, ori=0, name='target2box_inst',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
attribute1box_inst = visual.TextStim(win=win, ori=0, name='attribute1box_inst',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-4.0)
attribute2box_inst = visual.TextStim(win=win, ori=0, name='attribute2box_inst',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-5.0)
orLeftBox_inst = visual.TextStim(win=win, ori=0, name='orLeftBox_inst',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
orRightBox_inst = visual.TextStim(win=win, ori=0, name='orRightBox_inst',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimulusImage = visual.ImageStim(win=win, name='stimulusImage',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=.6,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
stimulusBox = visual.TextStim(win=win, ori=0, name='stimulusBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0)
msg1=""

order = int(expInfo['block order'])

if order == 1:
    taskFile = "blockOrderA.xlsx"
elif order == 2:
    taskFile = "blockOrderB.xlsx"
else:
    print "****UNRECOGNISED ORDER CODE - please use 1 or 2 only****"
accuracyFeedback = visual.TextStim(win=win, ori=0, name='accuracyFeedback',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-5.0)
target1box = visual.TextStim(win=win, ori=0, name='target1box',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
attribute1box = visual.TextStim(win=win, ori=0, name='attribute1box',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-7.0)
target2box = visual.TextStim(win=win, ori=0, name='target2box',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0)
attribute2box = visual.TextStim(win=win, ori=0, name='attribute2box',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-9.0)
orLeftBox = visual.TextStim(win=win, ori=0, name='orLeftBox',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0)
orRightBox = visual.TextStim(win=win, ori=0, name='orRightBox',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(taskFile),
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
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox.setText(instruction)
    responseContinue = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue.status = NOT_STARTED
    target1box_inst.setText(target1)
    target2box_inst.setText(target2)
    attribute1box_inst.setText(attribute1)
    attribute2box_inst.setText(attribute2)
    orLeftBox_inst.setText(orStimulus)
    orRightBox_inst.setText(orStimulus)
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(instructionsBox)
    instructionsComponents.append(responseContinue)
    instructionsComponents.append(target1box_inst)
    instructionsComponents.append(target2box_inst)
    instructionsComponents.append(attribute1box_inst)
    instructionsComponents.append(attribute2box_inst)
    instructionsComponents.append(orLeftBox_inst)
    instructionsComponents.append(orRightBox_inst)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox* updates
        if t >= 0.3 and instructionsBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox.tStart = t  # underestimates by a little under one frame
            instructionsBox.frameNStart = frameN  # exact frame index
            instructionsBox.setAutoDraw(True)
        
        # *responseContinue* updates
        if t >= 1 and responseContinue.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue.tStart = t  # underestimates by a little under one frame
            responseContinue.frameNStart = frameN  # exact frame index
            responseContinue.status = STARTED
            # keyboard checking is just starting
        if responseContinue.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *target1box_inst* updates
        if t >= 0.0 and target1box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box_inst.tStart = t  # underestimates by a little under one frame
            target1box_inst.frameNStart = frameN  # exact frame index
            target1box_inst.setAutoDraw(True)
        
        # *target2box_inst* updates
        if t >= 0.0 and target2box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box_inst.tStart = t  # underestimates by a little under one frame
            target2box_inst.frameNStart = frameN  # exact frame index
            target2box_inst.setAutoDraw(True)
        
        # *attribute1box_inst* updates
        if t >= 0.0 and attribute1box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box_inst.tStart = t  # underestimates by a little under one frame
            attribute1box_inst.frameNStart = frameN  # exact frame index
            attribute1box_inst.setAutoDraw(True)
        
        # *attribute2box_inst* updates
        if t >= 0.0 and attribute2box_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box_inst.tStart = t  # underestimates by a little under one frame
            attribute2box_inst.frameNStart = frameN  # exact frame index
            attribute2box_inst.setAutoDraw(True)
        
        # *orLeftBox_inst* updates
        if t >= 0.0 and orLeftBox_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox_inst.tStart = t  # underestimates by a little under one frame
            orLeftBox_inst.frameNStart = frameN  # exact frame index
            orLeftBox_inst.setAutoDraw(True)
        
        # *orRightBox_inst* updates
        if t >= 0.0 and orRightBox_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox_inst.tStart = t  # underestimates by a little under one frame
            orRightBox_inst.frameNStart = frameN  # exact frame index
            orRightBox_inst.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=nBlockRepeats, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(block),
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
        stimulusImage.setImage(imageStimulus)
        stimulusBox.setColor(stimulusColour, colorSpace='rgb')
        stimulusBox.setText(stimulus)
        requiredResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        requiredResponse.status = NOT_STARTED
        feedbackResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
        feedbackResponse.status = NOT_STARTED
        
        target1box.setText(target1)
        attribute1box.setColor([-1, 1, -1], colorSpace='rgb')
        attribute1box.setText(attribute1
)
        target2box.setText(target2)
        attribute2box.setText(attribute2)
        orLeftBox.setText(orStimulus)
        orRightBox.setText(orStimulus)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(stimulusImage)
        trialComponents.append(stimulusBox)
        trialComponents.append(requiredResponse)
        trialComponents.append(feedbackResponse)
        trialComponents.append(accuracyFeedback)
        trialComponents.append(target1box)
        trialComponents.append(attribute1box)
        trialComponents.append(target2box)
        trialComponents.append(attribute2box)
        trialComponents.append(orLeftBox)
        trialComponents.append(orRightBox)
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
            
            # *stimulusImage* updates
            if t >= 0.3 and stimulusImage.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusImage.tStart = t  # underestimates by a little under one frame
                stimulusImage.frameNStart = frameN  # exact frame index
                stimulusImage.setAutoDraw(True)
            
            # *stimulusBox* updates
            if t >= 0.3 and stimulusBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulusBox.tStart = t  # underestimates by a little under one frame
                stimulusBox.frameNStart = frameN  # exact frame index
                stimulusBox.setAutoDraw(True)
            
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
                        if (requiredResponse.keys == str(requiredResponse)) or (requiredResponse.keys == requiredResponse):
                            requiredResponse.corr = 1
                        else:
                            requiredResponse.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *feedbackResponse* updates
            if t >= 0.3 and feedbackResponse.status == NOT_STARTED:
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
                        if (feedbackResponse.keys == str(feedbackResponse)) or (feedbackResponse.keys == feedbackResponse):
                            feedbackResponse.corr = 1
                        else:
                            feedbackResponse.corr = 0
            if len(feedbackResponse.keys)<1:
                msg1=""
            else:
                msg1="X"
            
            # *accuracyFeedback* updates
            if t >= 0.3 and accuracyFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracyFeedback.tStart = t  # underestimates by a little under one frame
                accuracyFeedback.frameNStart = frameN  # exact frame index
                accuracyFeedback.setAutoDraw(True)
            if accuracyFeedback.status == STARTED:  # only update if being drawn
                accuracyFeedback.setText(msg1, log=False)
            
            # *target1box* updates
            if t >= 0.0 and target1box.status == NOT_STARTED:
                # keep track of start time/frame for later
                target1box.tStart = t  # underestimates by a little under one frame
                target1box.frameNStart = frameN  # exact frame index
                target1box.setAutoDraw(True)
            
            # *attribute1box* updates
            if t >= 0.0 and attribute1box.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute1box.tStart = t  # underestimates by a little under one frame
                attribute1box.frameNStart = frameN  # exact frame index
                attribute1box.setAutoDraw(True)
            
            # *target2box* updates
            if t >= 0.0 and target2box.status == NOT_STARTED:
                # keep track of start time/frame for later
                target2box.tStart = t  # underestimates by a little under one frame
                target2box.frameNStart = frameN  # exact frame index
                target2box.setAutoDraw(True)
            
            # *attribute2box* updates
            if t >= 0.0 and attribute2box.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute2box.tStart = t  # underestimates by a little under one frame
                attribute2box.frameNStart = frameN  # exact frame index
                attribute2box.setAutoDraw(True)
            
            # *orLeftBox* updates
            if t >= 0.0 and orLeftBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                orLeftBox.tStart = t  # underestimates by a little under one frame
                orLeftBox.frameNStart = frameN  # exact frame index
                orLeftBox.setAutoDraw(True)
            
            # *orRightBox* updates
            if t >= 0.0 and orRightBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                orRightBox.tStart = t  # underestimates by a little under one frame
                orRightBox.frameNStart = frameN  # exact frame index
                orRightBox.setAutoDraw(True)
            
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
           if str(requiredResponse).lower() == 'none': requiredResponse.corr = 1  # correct non-response
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
           if str(feedbackResponse).lower() == 'none': feedbackResponse.corr = 1  # correct non-response
           else: feedbackResponse.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('feedbackResponse.keys',feedbackResponse.keys)
        trials.addData('feedbackResponse.corr', feedbackResponse.corr)
        if feedbackResponse.keys != None:  # we had a response
            trials.addData('feedbackResponse.rt', feedbackResponse.rt)
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nBlockRepeats repeats of 'trials'
    
# completed 1 repeats of 'blocks'


win.close()
core.quit()

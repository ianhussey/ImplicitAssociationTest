#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Mon Oct 19 15:51:08 2015
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

# Initialize components for Routine "instructions1and5"
instructions1and5Clock = core.Clock()
instructionsBox1_2 = visual.TextStim(win=win, ori=0, name='instructionsBox1_2',
    text='default text',    font=u'Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
target1box1_inst_2 = visual.TextStim(win=win, ori=0, name='target1box1_inst_2',
    text='default text',    font=u'Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
target2box1_inst_2 = visual.TextStim(win=win, ori=0, name='target2box1_inst_2',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "trialBlock1"
trialBlock1Clock = core.Clock()
stimulusAbox1 = visual.TextStim(win=win, ori=0, name='stimulusAbox1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg1=""
accuracyFeedback1 = visual.TextStim(win=win, ori=0, name='accuracyFeedback1',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
target1box1 = visual.TextStim(win=win, ori=0, name='target1box1',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
target2box1 = visual.TextStim(win=win, ori=0, name='target2box1',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instructionsBox2 = visual.TextStim(win=win, ori=0, name='instructionsBox2',
    text='default text',    font=u'Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
attribute1box2_inst = visual.TextStim(win=win, ori=0, name='attribute1box2_inst',
    text='default text',    font=u'Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-2.0)
attribute2box2_inst = visual.TextStim(win=win, ori=0, name='attribute2box2_inst',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "trialBlock2"
trialBlock2Clock = core.Clock()
stimulusAbox2 = visual.TextStim(win=win, ori=0, name='stimulusAbox2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg1=""
accuracyFeedback2 = visual.TextStim(win=win, ori=0, name='accuracyFeedback2',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
attribute1box2 = visual.TextStim(win=win, ori=0, name='attribute1box2',
    text='default text',    font='Arial',
    pos=[-.6, 0.85], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-5.0)
attribute2box2 = visual.TextStim(win=win, ori=0, name='attribute2box2',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "instructions3467"
instructions3467Clock = core.Clock()
instructionsBox3467 = visual.TextStim(win=win, ori=0, name='instructionsBox3467',
    text='default text',    font=u'Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
target1box3467 = visual.TextStim(win=win, ori=0, name='target1box3467',
    text='default text',    font=u'Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
attribute1box3467 = visual.TextStim(win=win, ori=0, name='attribute1box3467',
    text='default text',    font=u'Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-3.0)
target2box3467 = visual.TextStim(win=win, ori=0, name='target2box3467',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
attribute2box3467 = visual.TextStim(win=win, ori=0, name='attribute2box3467',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-5.0)
orLeftBox3467 = visual.TextStim(win=win, ori=0, name='orLeftBox3467',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
orRightBox3467 = visual.TextStim(win=win, ori=0, name='orRightBox3467',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "trialBlock3and4"
trialBlock3and4Clock = core.Clock()
stimulusAbox3and4 = visual.TextStim(win=win, ori=0, name='stimulusAbox3and4',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg1=""
accuracyFeedback3and4 = visual.TextStim(win=win, ori=0, name='accuracyFeedback3and4',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
target1box3and4 = visual.TextStim(win=win, ori=0, name='target1box3and4',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
attribute1box3and4 = visual.TextStim(win=win, ori=0, name='attribute1box3and4',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
target2box3and4 = visual.TextStim(win=win, ori=0, name='target2box3and4',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
attribute2box3and4 = visual.TextStim(win=win, ori=0, name='attribute2box3and4',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-8.0)
orLeftBox3and4 = visual.TextStim(win=win, ori=0, name='orLeftBox3and4',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)
orRightBox3and4 = visual.TextStim(win=win, ori=0, name='orRightBox3and4',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "instructions3467"
instructions3467Clock = core.Clock()
instructionsBox3467 = visual.TextStim(win=win, ori=0, name='instructionsBox3467',
    text='default text',    font=u'Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
target1box3467 = visual.TextStim(win=win, ori=0, name='target1box3467',
    text='default text',    font=u'Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
attribute1box3467 = visual.TextStim(win=win, ori=0, name='attribute1box3467',
    text='default text',    font=u'Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-3.0)
target2box3467 = visual.TextStim(win=win, ori=0, name='target2box3467',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
attribute2box3467 = visual.TextStim(win=win, ori=0, name='attribute2box3467',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-5.0)
orLeftBox3467 = visual.TextStim(win=win, ori=0, name='orLeftBox3467',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
orRightBox3467 = visual.TextStim(win=win, ori=0, name='orRightBox3467',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "trialBlock3and4"
trialBlock3and4Clock = core.Clock()
stimulusAbox3and4 = visual.TextStim(win=win, ori=0, name='stimulusAbox3and4',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg1=""
accuracyFeedback3and4 = visual.TextStim(win=win, ori=0, name='accuracyFeedback3and4',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
target1box3and4 = visual.TextStim(win=win, ori=0, name='target1box3and4',
    text='default text',    font='Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
attribute1box3and4 = visual.TextStim(win=win, ori=0, name='attribute1box3and4',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
target2box3and4 = visual.TextStim(win=win, ori=0, name='target2box3and4',
    text='default text',    font='Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
attribute2box3and4 = visual.TextStim(win=win, ori=0, name='attribute2box3and4',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-8.0)
orLeftBox3and4 = visual.TextStim(win=win, ori=0, name='orLeftBox3and4',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)
orRightBox3and4 = visual.TextStim(win=win, ori=0, name='orRightBox3and4',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "instructions1and5"
instructions1and5Clock = core.Clock()
instructionsBox1_2 = visual.TextStim(win=win, ori=0, name='instructionsBox1_2',
    text='default text',    font=u'Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
target1box1_inst_2 = visual.TextStim(win=win, ori=0, name='target1box1_inst_2',
    text='default text',    font=u'Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
target2box1_inst_2 = visual.TextStim(win=win, ori=0, name='target2box1_inst_2',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "trialBlock5"
trialBlock5Clock = core.Clock()
stimulusAbox5 = visual.TextStim(win=win, ori=0, name='stimulusAbox5',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg1=""
accuracyFeedback5 = visual.TextStim(win=win, ori=0, name='accuracyFeedback5',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
target1box5 = visual.TextStim(win=win, ori=0, name='target1box5',
    text='default text',    font='Arial',
    pos=[.6, .85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
target2box5 = visual.TextStim(win=win, ori=0, name='target2box5',
    text='default text',    font='Arial',
    pos=[-.6, 0.85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "instructions3467"
instructions3467Clock = core.Clock()
instructionsBox3467 = visual.TextStim(win=win, ori=0, name='instructionsBox3467',
    text='default text',    font=u'Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
target1box3467 = visual.TextStim(win=win, ori=0, name='target1box3467',
    text='default text',    font=u'Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
attribute1box3467 = visual.TextStim(win=win, ori=0, name='attribute1box3467',
    text='default text',    font=u'Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-3.0)
target2box3467 = visual.TextStim(win=win, ori=0, name='target2box3467',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
attribute2box3467 = visual.TextStim(win=win, ori=0, name='attribute2box3467',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-5.0)
orLeftBox3467 = visual.TextStim(win=win, ori=0, name='orLeftBox3467',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
orRightBox3467 = visual.TextStim(win=win, ori=0, name='orRightBox3467',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "trialBlock6and7"
trialBlock6and7Clock = core.Clock()
stimulusBbox6and7 = visual.TextStim(win=win, ori=0, name='stimulusBbox6and7',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg1=""
accuracyFeedback6and7 = visual.TextStim(win=win, ori=0, name='accuracyFeedback6and7',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
target1box6and7 = visual.TextStim(win=win, ori=0, name='target1box6and7',
    text='default text',    font='Arial',
    pos=[.6, .85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
attribute1box6and7 = visual.TextStim(win=win, ori=0, name='attribute1box6and7',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
target2box6and7 = visual.TextStim(win=win, ori=0, name='target2box6and7',
    text='default text',    font='Arial',
    pos=[-.6, 0.85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
attribute2box6and7 = visual.TextStim(win=win, ori=0, name='attribute2box6and7',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-8.0)
orLeftBox6and7 = visual.TextStim(win=win, ori=0, name='orLeftBox6and7',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)
orRightBox6and7 = visual.TextStim(win=win, ori=0, name='orRightBox6and7',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "instructions3467"
instructions3467Clock = core.Clock()
instructionsBox3467 = visual.TextStim(win=win, ori=0, name='instructionsBox3467',
    text='default text',    font=u'Arial',
    pos=[0, -.15], height=0.05, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
target1box3467 = visual.TextStim(win=win, ori=0, name='target1box3467',
    text='default text',    font=u'Arial',
    pos=[-.6, .85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
attribute1box3467 = visual.TextStim(win=win, ori=0, name='attribute1box3467',
    text='default text',    font=u'Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-3.0)
target2box3467 = visual.TextStim(win=win, ori=0, name='target2box3467',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.85], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
attribute2box3467 = visual.TextStim(win=win, ori=0, name='attribute2box3467',
    text='default text',    font=u'Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-5.0)
orLeftBox3467 = visual.TextStim(win=win, ori=0, name='orLeftBox3467',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
orRightBox3467 = visual.TextStim(win=win, ori=0, name='orRightBox3467',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "trialBlock6and7"
trialBlock6and7Clock = core.Clock()
stimulusBbox6and7 = visual.TextStim(win=win, ori=0, name='stimulusBbox6and7',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg1=""
accuracyFeedback6and7 = visual.TextStim(win=win, ori=0, name='accuracyFeedback6and7',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
target1box6and7 = visual.TextStim(win=win, ori=0, name='target1box6and7',
    text='default text',    font='Arial',
    pos=[.6, .85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
attribute1box6and7 = visual.TextStim(win=win, ori=0, name='attribute1box6and7',
    text='default text',    font='Arial',
    pos=[-.6, 0.55], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
target2box6and7 = visual.TextStim(win=win, ori=0, name='target2box6and7',
    text='default text',    font='Arial',
    pos=[-.6, 0.85], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
attribute2box6and7 = visual.TextStim(win=win, ori=0, name='attribute2box6and7',
    text='default text',    font='Arial',
    pos=[0.6, 0.55], height=0.1, wrapWidth=None,
    color=[-1, 1, -1], colorSpace='rgb', opacity=1,
    depth=-8.0)
orLeftBox6and7 = visual.TextStim(win=win, ori=0, name='orLeftBox6and7',
    text='default text',    font='Arial',
    pos=[-.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)
orRightBox6and7 = visual.TextStim(win=win, ori=0, name='orRightBox6and7',
    text='default text',    font='Arial',
    pos=[.6, .7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "end"
endClock = core.Clock()
endMessage = visual.TextStim(win=win, ori=0, name='endMessage',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructionsLoop1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Instructions.xlsx', selection='0'),
    seed=None, name='instructionsLoop1')
thisExp.addLoop(instructionsLoop1)  # add the loop to the experiment
thisInstructionsLoop1 = instructionsLoop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstructionsLoop1.rgb)
if thisInstructionsLoop1 != None:
    for paramName in thisInstructionsLoop1.keys():
        exec(paramName + '= thisInstructionsLoop1.' + paramName)

for thisInstructionsLoop1 in instructionsLoop1:
    currentLoop = instructionsLoop1
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop1.rgb)
    if thisInstructionsLoop1 != None:
        for paramName in thisInstructionsLoop1.keys():
            exec(paramName + '= thisInstructionsLoop1.' + paramName)
    
    #------Prepare to start Routine "instructions1and5"-------
    t = 0
    instructions1and5Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox1_2.setText(instruction)
    responseContinue1_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue1_2.status = NOT_STARTED
    target1box1_inst_2.setText(targetLeft)
    target2box1_inst_2.setText(targetRight)
    # keep track of which components have finished
    instructions1and5Components = []
    instructions1and5Components.append(instructionsBox1_2)
    instructions1and5Components.append(responseContinue1_2)
    instructions1and5Components.append(target1box1_inst_2)
    instructions1and5Components.append(target2box1_inst_2)
    for thisComponent in instructions1and5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions1and5"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions1and5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox1_2* updates
        if t >= 0.3 and instructionsBox1_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox1_2.tStart = t  # underestimates by a little under one frame
            instructionsBox1_2.frameNStart = frameN  # exact frame index
            instructionsBox1_2.setAutoDraw(True)
        
        # *responseContinue1_2* updates
        if t >= 0.3 and responseContinue1_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue1_2.tStart = t  # underestimates by a little under one frame
            responseContinue1_2.frameNStart = frameN  # exact frame index
            responseContinue1_2.status = STARTED
            # keyboard checking is just starting
            responseContinue1_2.clock.reset()  # now t=0
        if responseContinue1_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseContinue1_2.keys == []:  # then this was the first keypress
                    responseContinue1_2.keys = theseKeys[0]  # just the first key pressed
                    responseContinue1_2.rt = responseContinue1_2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *target1box1_inst_2* updates
        if t >= 0.0 and target1box1_inst_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box1_inst_2.tStart = t  # underestimates by a little under one frame
            target1box1_inst_2.frameNStart = frameN  # exact frame index
            target1box1_inst_2.setAutoDraw(True)
        
        # *target2box1_inst_2* updates
        if t >= 0.0 and target2box1_inst_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box1_inst_2.tStart = t  # underestimates by a little under one frame
            target2box1_inst_2.frameNStart = frameN  # exact frame index
            target2box1_inst_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions1and5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions1and5"-------
    for thisComponent in instructions1and5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseContinue1_2.keys in ['', [], None]:  # No response was made
       responseContinue1_2.keys=None
    # store data for instructionsLoop1 (TrialHandler)
    instructionsLoop1.addData('responseContinue1_2.keys',responseContinue1_2.keys)
    if responseContinue1_2.keys != None:  # we had a response
        instructionsLoop1.addData('responseContinue1_2.rt', responseContinue1_2.rt)
    # the Routine "instructions1and5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instructionsLoop1'


# set up handler to look after randomisation of conditions etc
block1Loop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Stimuli.xlsx', selection='0:10'),
    seed=None, name='block1Loop')
thisExp.addLoop(block1Loop)  # add the loop to the experiment
thisBlock1Loop = block1Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock1Loop.rgb)
if thisBlock1Loop != None:
    for paramName in thisBlock1Loop.keys():
        exec(paramName + '= thisBlock1Loop.' + paramName)

for thisBlock1Loop in block1Loop:
    currentLoop = block1Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1Loop.rgb)
    if thisBlock1Loop != None:
        for paramName in thisBlock1Loop.keys():
            exec(paramName + '= thisBlock1Loop.' + paramName)
    
    #------Prepare to start Routine "trialBlock1"-------
    t = 0
    trialBlock1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusAbox1.setColor(stimulusColour, colorSpace='rgb')
    stimulusAbox1.setText(stimulusA)
    responseRequired1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseRequired1.status = NOT_STARTED
    responseFeedback1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseFeedback1.status = NOT_STARTED
    
    target1box1.setText(target1)
    target2box1.setText(target2)
    # keep track of which components have finished
    trialBlock1Components = []
    trialBlock1Components.append(stimulusAbox1)
    trialBlock1Components.append(responseRequired1)
    trialBlock1Components.append(responseFeedback1)
    trialBlock1Components.append(accuracyFeedback1)
    trialBlock1Components.append(target1box1)
    trialBlock1Components.append(target2box1)
    for thisComponent in trialBlock1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trialBlock1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialBlock1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusAbox1* updates
        if t >= 0.3 and stimulusAbox1.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusAbox1.tStart = t  # underestimates by a little under one frame
            stimulusAbox1.frameNStart = frameN  # exact frame index
            stimulusAbox1.setAutoDraw(True)
        
        # *responseRequired1* updates
        if t >= 0.3 and responseRequired1.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseRequired1.tStart = t  # underestimates by a little under one frame
            responseRequired1.frameNStart = frameN  # exact frame index
            responseRequired1.status = STARTED
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
            responseRequired1.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseRequired1.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowed))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseRequired1.keys == []:  # then this was the first keypress
                    responseRequired1.keys = theseKeys[0]  # just the first key pressed
                    responseRequired1.rt = responseRequired1.clock.getTime()
                    # was this 'correct'?
                    if (responseRequired1.keys == str(requiredResponse)) or (responseRequired1.keys == requiredResponse):
                        responseRequired1.corr = 1
                    else:
                        responseRequired1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *responseFeedback1* updates
        if t >= 0.3 and responseFeedback1.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseFeedback1.tStart = t  # underestimates by a little under one frame
            responseFeedback1.frameNStart = frameN  # exact frame index
            responseFeedback1.status = STARTED
            # AllowedKeys looks like a variable named `feedbackResponse`
            if not 'feedbackResponse' in locals():
                logging.error('AllowedKeys variable `feedbackResponse` is not defined.')
                core.quit()
            if not type(feedbackResponse) in [list, tuple, np.ndarray]:
                if not isinstance(feedbackResponse, basestring):
                    logging.error('AllowedKeys variable `feedbackResponse` is not string- or list-like.')
                    core.quit()
                elif not ',' in feedbackResponse: feedbackResponse = (feedbackResponse,)
                else:  feedbackResponse = eval(feedbackResponse)
            # keyboard checking is just starting
            responseFeedback1.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseFeedback1.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackResponse))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseFeedback1.keys == []:  # then this was the first keypress
                    responseFeedback1.keys = theseKeys[0]  # just the first key pressed
                    responseFeedback1.rt = responseFeedback1.clock.getTime()
                    # was this 'correct'?
                    if (responseFeedback1.keys == str(feedbackResponse)) or (responseFeedback1.keys == feedbackResponse):
                        responseFeedback1.corr = 1
                    else:
                        responseFeedback1.corr = 0
        if len(responseFeedback1.keys)<1:
            msg1=""
        else:
            msg1="X"
        
        # *accuracyFeedback1* updates
        if t >= 0.3 and accuracyFeedback1.status == NOT_STARTED:
            # keep track of start time/frame for later
            accuracyFeedback1.tStart = t  # underestimates by a little under one frame
            accuracyFeedback1.frameNStart = frameN  # exact frame index
            accuracyFeedback1.setAutoDraw(True)
        if accuracyFeedback1.status == STARTED:  # only update if being drawn
            accuracyFeedback1.setText(msg1, log=False)
        
        # *target1box1* updates
        if t >= 0.0 and target1box1.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box1.tStart = t  # underestimates by a little under one frame
            target1box1.frameNStart = frameN  # exact frame index
            target1box1.setAutoDraw(True)
        
        # *target2box1* updates
        if t >= 0.0 and target2box1.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box1.tStart = t  # underestimates by a little under one frame
            target2box1.frameNStart = frameN  # exact frame index
            target2box1.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialBlock1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trialBlock1"-------
    for thisComponent in trialBlock1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseRequired1.keys in ['', [], None]:  # No response was made
       responseRequired1.keys=None
       # was no response the correct answer?!
       if str(requiredResponse).lower() == 'none': responseRequired1.corr = 1  # correct non-response
       else: responseRequired1.corr = 0  # failed to respond (incorrectly)
    # store data for block1Loop (TrialHandler)
    block1Loop.addData('responseRequired1.keys',responseRequired1.keys)
    block1Loop.addData('responseRequired1.corr', responseRequired1.corr)
    if responseRequired1.keys != None:  # we had a response
        block1Loop.addData('responseRequired1.rt', responseRequired1.rt)
    # check responses
    if responseFeedback1.keys in ['', [], None]:  # No response was made
       responseFeedback1.keys=None
       # was no response the correct answer?!
       if str(feedbackResponse).lower() == 'none': responseFeedback1.corr = 1  # correct non-response
       else: responseFeedback1.corr = 0  # failed to respond (incorrectly)
    # store data for block1Loop (TrialHandler)
    block1Loop.addData('responseFeedback1.keys',responseFeedback1.keys)
    block1Loop.addData('responseFeedback1.corr', responseFeedback1.corr)
    if responseFeedback1.keys != None:  # we had a response
        block1Loop.addData('responseFeedback1.rt', responseFeedback1.rt)
    
    # the Routine "trialBlock1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'block1Loop'


# set up handler to look after randomisation of conditions etc
instructionsLoop2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Instructions.xlsx', selection='1'),
    seed=None, name='instructionsLoop2')
thisExp.addLoop(instructionsLoop2)  # add the loop to the experiment
thisInstructionsLoop2 = instructionsLoop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstructionsLoop2.rgb)
if thisInstructionsLoop2 != None:
    for paramName in thisInstructionsLoop2.keys():
        exec(paramName + '= thisInstructionsLoop2.' + paramName)

for thisInstructionsLoop2 in instructionsLoop2:
    currentLoop = instructionsLoop2
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop2.rgb)
    if thisInstructionsLoop2 != None:
        for paramName in thisInstructionsLoop2.keys():
            exec(paramName + '= thisInstructionsLoop2.' + paramName)
    
    #------Prepare to start Routine "instructions2"-------
    t = 0
    instructions2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox2.setText(instruction)
    responseContinue2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue2.status = NOT_STARTED
    attribute1box2_inst.setText(attributeLeft)
    attribute2box2_inst.setText(attributeRight)
    # keep track of which components have finished
    instructions2Components = []
    instructions2Components.append(instructionsBox2)
    instructions2Components.append(responseContinue2)
    instructions2Components.append(attribute1box2_inst)
    instructions2Components.append(attribute2box2_inst)
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox2* updates
        if t >= 0.3 and instructionsBox2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox2.tStart = t  # underestimates by a little under one frame
            instructionsBox2.frameNStart = frameN  # exact frame index
            instructionsBox2.setAutoDraw(True)
        
        # *responseContinue2* updates
        if t >= 0.3 and responseContinue2.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue2.tStart = t  # underestimates by a little under one frame
            responseContinue2.frameNStart = frameN  # exact frame index
            responseContinue2.status = STARTED
            # keyboard checking is just starting
            responseContinue2.clock.reset()  # now t=0
        if responseContinue2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseContinue2.keys == []:  # then this was the first keypress
                    responseContinue2.keys = theseKeys[0]  # just the first key pressed
                    responseContinue2.rt = responseContinue2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *attribute1box2_inst* updates
        if t >= 0.0 and attribute1box2_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box2_inst.tStart = t  # underestimates by a little under one frame
            attribute1box2_inst.frameNStart = frameN  # exact frame index
            attribute1box2_inst.setAutoDraw(True)
        
        # *attribute2box2_inst* updates
        if t >= 0.0 and attribute2box2_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box2_inst.tStart = t  # underestimates by a little under one frame
            attribute2box2_inst.frameNStart = frameN  # exact frame index
            attribute2box2_inst.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions2"-------
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseContinue2.keys in ['', [], None]:  # No response was made
       responseContinue2.keys=None
    # store data for instructionsLoop2 (TrialHandler)
    instructionsLoop2.addData('responseContinue2.keys',responseContinue2.keys)
    if responseContinue2.keys != None:  # we had a response
        instructionsLoop2.addData('responseContinue2.rt', responseContinue2.rt)
    # the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructionsLoop2'


# set up handler to look after randomisation of conditions etc
block2Loop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Stimuli.xlsx', selection='10:20'),
    seed=None, name='block2Loop')
thisExp.addLoop(block2Loop)  # add the loop to the experiment
thisBlock2Loop = block2Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock2Loop.rgb)
if thisBlock2Loop != None:
    for paramName in thisBlock2Loop.keys():
        exec(paramName + '= thisBlock2Loop.' + paramName)

for thisBlock2Loop in block2Loop:
    currentLoop = block2Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2Loop.rgb)
    if thisBlock2Loop != None:
        for paramName in thisBlock2Loop.keys():
            exec(paramName + '= thisBlock2Loop.' + paramName)
    
    #------Prepare to start Routine "trialBlock2"-------
    t = 0
    trialBlock2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusAbox2.setColor(stimulusColour, colorSpace='rgb')
    stimulusAbox2.setText(stimulusA)
    responseRequired2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseRequired2.status = NOT_STARTED
    responseFeedback2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseFeedback2.status = NOT_STARTED
    
    attribute1box2.setColor([-1, 1, -1], colorSpace='rgb')
    attribute1box2.setText(attribute1
)
    attribute2box2.setText(attribute2)
    # keep track of which components have finished
    trialBlock2Components = []
    trialBlock2Components.append(stimulusAbox2)
    trialBlock2Components.append(responseRequired2)
    trialBlock2Components.append(responseFeedback2)
    trialBlock2Components.append(accuracyFeedback2)
    trialBlock2Components.append(attribute1box2)
    trialBlock2Components.append(attribute2box2)
    for thisComponent in trialBlock2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trialBlock2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialBlock2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusAbox2* updates
        if t >= 0.3 and stimulusAbox2.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusAbox2.tStart = t  # underestimates by a little under one frame
            stimulusAbox2.frameNStart = frameN  # exact frame index
            stimulusAbox2.setAutoDraw(True)
        
        # *responseRequired2* updates
        if t >= 0.3 and responseRequired2.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseRequired2.tStart = t  # underestimates by a little under one frame
            responseRequired2.frameNStart = frameN  # exact frame index
            responseRequired2.status = STARTED
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
            responseRequired2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseRequired2.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowed))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseRequired2.keys == []:  # then this was the first keypress
                    responseRequired2.keys = theseKeys[0]  # just the first key pressed
                    responseRequired2.rt = responseRequired2.clock.getTime()
                    # was this 'correct'?
                    if (responseRequired2.keys == str(requiredResponse)) or (responseRequired2.keys == requiredResponse):
                        responseRequired2.corr = 1
                    else:
                        responseRequired2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *responseFeedback2* updates
        if t >= 0.3 and responseFeedback2.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseFeedback2.tStart = t  # underestimates by a little under one frame
            responseFeedback2.frameNStart = frameN  # exact frame index
            responseFeedback2.status = STARTED
            # AllowedKeys looks like a variable named `feedbackResponse`
            if not 'feedbackResponse' in locals():
                logging.error('AllowedKeys variable `feedbackResponse` is not defined.')
                core.quit()
            if not type(feedbackResponse) in [list, tuple, np.ndarray]:
                if not isinstance(feedbackResponse, basestring):
                    logging.error('AllowedKeys variable `feedbackResponse` is not string- or list-like.')
                    core.quit()
                elif not ',' in feedbackResponse: feedbackResponse = (feedbackResponse,)
                else:  feedbackResponse = eval(feedbackResponse)
            # keyboard checking is just starting
            responseFeedback2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseFeedback2.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackResponse))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseFeedback2.keys == []:  # then this was the first keypress
                    responseFeedback2.keys = theseKeys[0]  # just the first key pressed
                    responseFeedback2.rt = responseFeedback2.clock.getTime()
                    # was this 'correct'?
                    if (responseFeedback2.keys == str(feedbackAllowed)) or (responseFeedback2.keys == feedbackAllowed):
                        responseFeedback2.corr = 1
                    else:
                        responseFeedback2.corr = 0
        if len(responseFeedback2.keys)<1:
            msg1=""
        else:
            msg1="X"
        
        # *accuracyFeedback2* updates
        if t >= 0.3 and accuracyFeedback2.status == NOT_STARTED:
            # keep track of start time/frame for later
            accuracyFeedback2.tStart = t  # underestimates by a little under one frame
            accuracyFeedback2.frameNStart = frameN  # exact frame index
            accuracyFeedback2.setAutoDraw(True)
        if accuracyFeedback2.status == STARTED:  # only update if being drawn
            accuracyFeedback2.setText(msg1, log=False)
        
        # *attribute1box2* updates
        if t >= 0.0 and attribute1box2.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box2.tStart = t  # underestimates by a little under one frame
            attribute1box2.frameNStart = frameN  # exact frame index
            attribute1box2.setAutoDraw(True)
        
        # *attribute2box2* updates
        if t >= 0.0 and attribute2box2.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box2.tStart = t  # underestimates by a little under one frame
            attribute2box2.frameNStart = frameN  # exact frame index
            attribute2box2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialBlock2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trialBlock2"-------
    for thisComponent in trialBlock2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseRequired2.keys in ['', [], None]:  # No response was made
       responseRequired2.keys=None
       # was no response the correct answer?!
       if str(requiredResponse).lower() == 'none': responseRequired2.corr = 1  # correct non-response
       else: responseRequired2.corr = 0  # failed to respond (incorrectly)
    # store data for block2Loop (TrialHandler)
    block2Loop.addData('responseRequired2.keys',responseRequired2.keys)
    block2Loop.addData('responseRequired2.corr', responseRequired2.corr)
    if responseRequired2.keys != None:  # we had a response
        block2Loop.addData('responseRequired2.rt', responseRequired2.rt)
    # check responses
    if responseFeedback2.keys in ['', [], None]:  # No response was made
       responseFeedback2.keys=None
       # was no response the correct answer?!
       if str(feedbackAllowed).lower() == 'none': responseFeedback2.corr = 1  # correct non-response
       else: responseFeedback2.corr = 0  # failed to respond (incorrectly)
    # store data for block2Loop (TrialHandler)
    block2Loop.addData('responseFeedback2.keys',responseFeedback2.keys)
    block2Loop.addData('responseFeedback2.corr', responseFeedback2.corr)
    if responseFeedback2.keys != None:  # we had a response
        block2Loop.addData('responseFeedback2.rt', responseFeedback2.rt)
    
    # the Routine "trialBlock2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'block2Loop'


# set up handler to look after randomisation of conditions etc
instructionsLoop3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Instructions.xlsx', selection='2'),
    seed=None, name='instructionsLoop3')
thisExp.addLoop(instructionsLoop3)  # add the loop to the experiment
thisInstructionsLoop3 = instructionsLoop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstructionsLoop3.rgb)
if thisInstructionsLoop3 != None:
    for paramName in thisInstructionsLoop3.keys():
        exec(paramName + '= thisInstructionsLoop3.' + paramName)

for thisInstructionsLoop3 in instructionsLoop3:
    currentLoop = instructionsLoop3
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop3.rgb)
    if thisInstructionsLoop3 != None:
        for paramName in thisInstructionsLoop3.keys():
            exec(paramName + '= thisInstructionsLoop3.' + paramName)
    
    #------Prepare to start Routine "instructions3467"-------
    t = 0
    instructions3467Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox3467.setText(instruction)
    responseContinue3467 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue3467.status = NOT_STARTED
    target1box3467.setText(targetLeft)
    attribute1box3467.setColor([-1, 1, -1], colorSpace='rgb')
    attribute1box3467.setText(attributeLeft)
    target2box3467.setText(targetRight)
    attribute2box3467.setText(attributeRight)
    orLeftBox3467.setText(orStimulus)
    orRightBox3467.setText(orStimulus)
    # keep track of which components have finished
    instructions3467Components = []
    instructions3467Components.append(instructionsBox3467)
    instructions3467Components.append(responseContinue3467)
    instructions3467Components.append(target1box3467)
    instructions3467Components.append(attribute1box3467)
    instructions3467Components.append(target2box3467)
    instructions3467Components.append(attribute2box3467)
    instructions3467Components.append(orLeftBox3467)
    instructions3467Components.append(orRightBox3467)
    for thisComponent in instructions3467Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions3467"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions3467Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox3467* updates
        if t >= 0.3 and instructionsBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox3467.tStart = t  # underestimates by a little under one frame
            instructionsBox3467.frameNStart = frameN  # exact frame index
            instructionsBox3467.setAutoDraw(True)
        
        # *responseContinue3467* updates
        if t >= 0.3 and responseContinue3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue3467.tStart = t  # underestimates by a little under one frame
            responseContinue3467.frameNStart = frameN  # exact frame index
            responseContinue3467.status = STARTED
            # keyboard checking is just starting
            responseContinue3467.clock.reset()  # now t=0
        if responseContinue3467.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseContinue3467.keys == []:  # then this was the first keypress
                    responseContinue3467.keys = theseKeys[0]  # just the first key pressed
                    responseContinue3467.rt = responseContinue3467.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *target1box3467* updates
        if t >= 0.0 and target1box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box3467.tStart = t  # underestimates by a little under one frame
            target1box3467.frameNStart = frameN  # exact frame index
            target1box3467.setAutoDraw(True)
        
        # *attribute1box3467* updates
        if t >= 0.0 and attribute1box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box3467.tStart = t  # underestimates by a little under one frame
            attribute1box3467.frameNStart = frameN  # exact frame index
            attribute1box3467.setAutoDraw(True)
        
        # *target2box3467* updates
        if t >= 0.0 and target2box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box3467.tStart = t  # underestimates by a little under one frame
            target2box3467.frameNStart = frameN  # exact frame index
            target2box3467.setAutoDraw(True)
        
        # *attribute2box3467* updates
        if t >= 0.0 and attribute2box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box3467.tStart = t  # underestimates by a little under one frame
            attribute2box3467.frameNStart = frameN  # exact frame index
            attribute2box3467.setAutoDraw(True)
        
        # *orLeftBox3467* updates
        if t >= 0.0 and orLeftBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox3467.tStart = t  # underestimates by a little under one frame
            orLeftBox3467.frameNStart = frameN  # exact frame index
            orLeftBox3467.setAutoDraw(True)
        
        # *orRightBox3467* updates
        if t >= 0.0 and orRightBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox3467.tStart = t  # underestimates by a little under one frame
            orRightBox3467.frameNStart = frameN  # exact frame index
            orRightBox3467.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions3467Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions3467"-------
    for thisComponent in instructions3467Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseContinue3467.keys in ['', [], None]:  # No response was made
       responseContinue3467.keys=None
    # store data for instructionsLoop3 (TrialHandler)
    instructionsLoop3.addData('responseContinue3467.keys',responseContinue3467.keys)
    if responseContinue3467.keys != None:  # we had a response
        instructionsLoop3.addData('responseContinue3467.rt', responseContinue3467.rt)
    # the Routine "instructions3467" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructionsLoop3'


# set up handler to look after randomisation of conditions etc
block3Loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Stimuli.xlsx'),
    seed=None, name='block3Loop')
thisExp.addLoop(block3Loop)  # add the loop to the experiment
thisBlock3Loop = block3Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock3Loop.rgb)
if thisBlock3Loop != None:
    for paramName in thisBlock3Loop.keys():
        exec(paramName + '= thisBlock3Loop.' + paramName)

for thisBlock3Loop in block3Loop:
    currentLoop = block3Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3Loop.rgb)
    if thisBlock3Loop != None:
        for paramName in thisBlock3Loop.keys():
            exec(paramName + '= thisBlock3Loop.' + paramName)
    
    #------Prepare to start Routine "trialBlock3and4"-------
    t = 0
    trialBlock3and4Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusAbox3and4.setColor(stimulusColour, colorSpace='rgb')
    stimulusAbox3and4.setText(stimulusA)
    responseRequired3and4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseRequired3and4.status = NOT_STARTED
    responseFeedback3and4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseFeedback3and4.status = NOT_STARTED
    
    target1box3and4.setText(target1)
    attribute1box3and4.setColor([-1, 1, -1], colorSpace='rgb')
    attribute1box3and4.setText(attribute1
)
    target2box3and4.setText(target2)
    attribute2box3and4.setText(attribute2)
    orLeftBox3and4.setText(orStimulus)
    orRightBox3and4.setText(orStimulus)
    # keep track of which components have finished
    trialBlock3and4Components = []
    trialBlock3and4Components.append(stimulusAbox3and4)
    trialBlock3and4Components.append(responseRequired3and4)
    trialBlock3and4Components.append(responseFeedback3and4)
    trialBlock3and4Components.append(accuracyFeedback3and4)
    trialBlock3and4Components.append(target1box3and4)
    trialBlock3and4Components.append(attribute1box3and4)
    trialBlock3and4Components.append(target2box3and4)
    trialBlock3and4Components.append(attribute2box3and4)
    trialBlock3and4Components.append(orLeftBox3and4)
    trialBlock3and4Components.append(orRightBox3and4)
    for thisComponent in trialBlock3and4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trialBlock3and4"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialBlock3and4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusAbox3and4* updates
        if t >= 0.3 and stimulusAbox3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusAbox3and4.tStart = t  # underestimates by a little under one frame
            stimulusAbox3and4.frameNStart = frameN  # exact frame index
            stimulusAbox3and4.setAutoDraw(True)
        
        # *responseRequired3and4* updates
        if t >= 0.3 and responseRequired3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseRequired3and4.tStart = t  # underestimates by a little under one frame
            responseRequired3and4.frameNStart = frameN  # exact frame index
            responseRequired3and4.status = STARTED
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
            responseRequired3and4.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseRequired3and4.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowed))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseRequired3and4.keys == []:  # then this was the first keypress
                    responseRequired3and4.keys = theseKeys[0]  # just the first key pressed
                    responseRequired3and4.rt = responseRequired3and4.clock.getTime()
                    # was this 'correct'?
                    if (responseRequired3and4.keys == str(requiredResponse)) or (responseRequired3and4.keys == requiredResponse):
                        responseRequired3and4.corr = 1
                    else:
                        responseRequired3and4.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *responseFeedback3and4* updates
        if t >= 0.3 and responseFeedback3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseFeedback3and4.tStart = t  # underestimates by a little under one frame
            responseFeedback3and4.frameNStart = frameN  # exact frame index
            responseFeedback3and4.status = STARTED
            # AllowedKeys looks like a variable named `feedbackResponse`
            if not 'feedbackResponse' in locals():
                logging.error('AllowedKeys variable `feedbackResponse` is not defined.')
                core.quit()
            if not type(feedbackResponse) in [list, tuple, np.ndarray]:
                if not isinstance(feedbackResponse, basestring):
                    logging.error('AllowedKeys variable `feedbackResponse` is not string- or list-like.')
                    core.quit()
                elif not ',' in feedbackResponse: feedbackResponse = (feedbackResponse,)
                else:  feedbackResponse = eval(feedbackResponse)
            # keyboard checking is just starting
            responseFeedback3and4.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseFeedback3and4.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackResponse))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseFeedback3and4.keys == []:  # then this was the first keypress
                    responseFeedback3and4.keys = theseKeys[0]  # just the first key pressed
                    responseFeedback3and4.rt = responseFeedback3and4.clock.getTime()
                    # was this 'correct'?
                    if (responseFeedback3and4.keys == str(feedbackAllowed)) or (responseFeedback3and4.keys == feedbackAllowed):
                        responseFeedback3and4.corr = 1
                    else:
                        responseFeedback3and4.corr = 0
        if len(responseFeedback3and4.keys)<1:
            msg1=""
        else:
            msg1="X"
        
        # *accuracyFeedback3and4* updates
        if t >= 0.3 and accuracyFeedback3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            accuracyFeedback3and4.tStart = t  # underestimates by a little under one frame
            accuracyFeedback3and4.frameNStart = frameN  # exact frame index
            accuracyFeedback3and4.setAutoDraw(True)
        if accuracyFeedback3and4.status == STARTED:  # only update if being drawn
            accuracyFeedback3and4.setText(msg1, log=False)
        
        # *target1box3and4* updates
        if t >= 0.0 and target1box3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box3and4.tStart = t  # underestimates by a little under one frame
            target1box3and4.frameNStart = frameN  # exact frame index
            target1box3and4.setAutoDraw(True)
        
        # *attribute1box3and4* updates
        if t >= 0.0 and attribute1box3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box3and4.tStart = t  # underestimates by a little under one frame
            attribute1box3and4.frameNStart = frameN  # exact frame index
            attribute1box3and4.setAutoDraw(True)
        
        # *target2box3and4* updates
        if t >= 0.0 and target2box3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box3and4.tStart = t  # underestimates by a little under one frame
            target2box3and4.frameNStart = frameN  # exact frame index
            target2box3and4.setAutoDraw(True)
        
        # *attribute2box3and4* updates
        if t >= 0.0 and attribute2box3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box3and4.tStart = t  # underestimates by a little under one frame
            attribute2box3and4.frameNStart = frameN  # exact frame index
            attribute2box3and4.setAutoDraw(True)
        
        # *orLeftBox3and4* updates
        if t >= 0.0 and orLeftBox3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox3and4.tStart = t  # underestimates by a little under one frame
            orLeftBox3and4.frameNStart = frameN  # exact frame index
            orLeftBox3and4.setAutoDraw(True)
        
        # *orRightBox3and4* updates
        if t >= 0.0 and orRightBox3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox3and4.tStart = t  # underestimates by a little under one frame
            orRightBox3and4.frameNStart = frameN  # exact frame index
            orRightBox3and4.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialBlock3and4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trialBlock3and4"-------
    for thisComponent in trialBlock3and4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseRequired3and4.keys in ['', [], None]:  # No response was made
       responseRequired3and4.keys=None
       # was no response the correct answer?!
       if str(requiredResponse).lower() == 'none': responseRequired3and4.corr = 1  # correct non-response
       else: responseRequired3and4.corr = 0  # failed to respond (incorrectly)
    # store data for block3Loop (TrialHandler)
    block3Loop.addData('responseRequired3and4.keys',responseRequired3and4.keys)
    block3Loop.addData('responseRequired3and4.corr', responseRequired3and4.corr)
    if responseRequired3and4.keys != None:  # we had a response
        block3Loop.addData('responseRequired3and4.rt', responseRequired3and4.rt)
    # check responses
    if responseFeedback3and4.keys in ['', [], None]:  # No response was made
       responseFeedback3and4.keys=None
       # was no response the correct answer?!
       if str(feedbackAllowed).lower() == 'none': responseFeedback3and4.corr = 1  # correct non-response
       else: responseFeedback3and4.corr = 0  # failed to respond (incorrectly)
    # store data for block3Loop (TrialHandler)
    block3Loop.addData('responseFeedback3and4.keys',responseFeedback3and4.keys)
    block3Loop.addData('responseFeedback3and4.corr', responseFeedback3and4.corr)
    if responseFeedback3and4.keys != None:  # we had a response
        block3Loop.addData('responseFeedback3and4.rt', responseFeedback3and4.rt)
    
    # the Routine "trialBlock3and4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'block3Loop'


# set up handler to look after randomisation of conditions etc
instructionsLoop4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Instructions.xlsx', selection='3'),
    seed=None, name='instructionsLoop4')
thisExp.addLoop(instructionsLoop4)  # add the loop to the experiment
thisInstructionsLoop4 = instructionsLoop4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstructionsLoop4.rgb)
if thisInstructionsLoop4 != None:
    for paramName in thisInstructionsLoop4.keys():
        exec(paramName + '= thisInstructionsLoop4.' + paramName)

for thisInstructionsLoop4 in instructionsLoop4:
    currentLoop = instructionsLoop4
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop4.rgb)
    if thisInstructionsLoop4 != None:
        for paramName in thisInstructionsLoop4.keys():
            exec(paramName + '= thisInstructionsLoop4.' + paramName)
    
    #------Prepare to start Routine "instructions3467"-------
    t = 0
    instructions3467Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox3467.setText(instruction)
    responseContinue3467 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue3467.status = NOT_STARTED
    target1box3467.setText(targetLeft)
    attribute1box3467.setColor([-1, 1, -1], colorSpace='rgb')
    attribute1box3467.setText(attributeLeft)
    target2box3467.setText(targetRight)
    attribute2box3467.setText(attributeRight)
    orLeftBox3467.setText(orStimulus)
    orRightBox3467.setText(orStimulus)
    # keep track of which components have finished
    instructions3467Components = []
    instructions3467Components.append(instructionsBox3467)
    instructions3467Components.append(responseContinue3467)
    instructions3467Components.append(target1box3467)
    instructions3467Components.append(attribute1box3467)
    instructions3467Components.append(target2box3467)
    instructions3467Components.append(attribute2box3467)
    instructions3467Components.append(orLeftBox3467)
    instructions3467Components.append(orRightBox3467)
    for thisComponent in instructions3467Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions3467"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions3467Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox3467* updates
        if t >= 0.3 and instructionsBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox3467.tStart = t  # underestimates by a little under one frame
            instructionsBox3467.frameNStart = frameN  # exact frame index
            instructionsBox3467.setAutoDraw(True)
        
        # *responseContinue3467* updates
        if t >= 0.3 and responseContinue3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue3467.tStart = t  # underestimates by a little under one frame
            responseContinue3467.frameNStart = frameN  # exact frame index
            responseContinue3467.status = STARTED
            # keyboard checking is just starting
            responseContinue3467.clock.reset()  # now t=0
        if responseContinue3467.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseContinue3467.keys == []:  # then this was the first keypress
                    responseContinue3467.keys = theseKeys[0]  # just the first key pressed
                    responseContinue3467.rt = responseContinue3467.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *target1box3467* updates
        if t >= 0.0 and target1box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box3467.tStart = t  # underestimates by a little under one frame
            target1box3467.frameNStart = frameN  # exact frame index
            target1box3467.setAutoDraw(True)
        
        # *attribute1box3467* updates
        if t >= 0.0 and attribute1box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box3467.tStart = t  # underestimates by a little under one frame
            attribute1box3467.frameNStart = frameN  # exact frame index
            attribute1box3467.setAutoDraw(True)
        
        # *target2box3467* updates
        if t >= 0.0 and target2box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box3467.tStart = t  # underestimates by a little under one frame
            target2box3467.frameNStart = frameN  # exact frame index
            target2box3467.setAutoDraw(True)
        
        # *attribute2box3467* updates
        if t >= 0.0 and attribute2box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box3467.tStart = t  # underestimates by a little under one frame
            attribute2box3467.frameNStart = frameN  # exact frame index
            attribute2box3467.setAutoDraw(True)
        
        # *orLeftBox3467* updates
        if t >= 0.0 and orLeftBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox3467.tStart = t  # underestimates by a little under one frame
            orLeftBox3467.frameNStart = frameN  # exact frame index
            orLeftBox3467.setAutoDraw(True)
        
        # *orRightBox3467* updates
        if t >= 0.0 and orRightBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox3467.tStart = t  # underestimates by a little under one frame
            orRightBox3467.frameNStart = frameN  # exact frame index
            orRightBox3467.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions3467Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions3467"-------
    for thisComponent in instructions3467Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseContinue3467.keys in ['', [], None]:  # No response was made
       responseContinue3467.keys=None
    # store data for instructionsLoop4 (TrialHandler)
    instructionsLoop4.addData('responseContinue3467.keys',responseContinue3467.keys)
    if responseContinue3467.keys != None:  # we had a response
        instructionsLoop4.addData('responseContinue3467.rt', responseContinue3467.rt)
    # the Routine "instructions3467" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructionsLoop4'


# set up handler to look after randomisation of conditions etc
block4Loop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Stimuli.xlsx'),
    seed=None, name='block4Loop')
thisExp.addLoop(block4Loop)  # add the loop to the experiment
thisBlock4Loop = block4Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock4Loop.rgb)
if thisBlock4Loop != None:
    for paramName in thisBlock4Loop.keys():
        exec(paramName + '= thisBlock4Loop.' + paramName)

for thisBlock4Loop in block4Loop:
    currentLoop = block4Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock4Loop.rgb)
    if thisBlock4Loop != None:
        for paramName in thisBlock4Loop.keys():
            exec(paramName + '= thisBlock4Loop.' + paramName)
    
    #------Prepare to start Routine "trialBlock3and4"-------
    t = 0
    trialBlock3and4Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusAbox3and4.setColor(stimulusColour, colorSpace='rgb')
    stimulusAbox3and4.setText(stimulusA)
    responseRequired3and4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseRequired3and4.status = NOT_STARTED
    responseFeedback3and4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseFeedback3and4.status = NOT_STARTED
    
    target1box3and4.setText(target1)
    attribute1box3and4.setColor([-1, 1, -1], colorSpace='rgb')
    attribute1box3and4.setText(attribute1
)
    target2box3and4.setText(target2)
    attribute2box3and4.setText(attribute2)
    orLeftBox3and4.setText(orStimulus)
    orRightBox3and4.setText(orStimulus)
    # keep track of which components have finished
    trialBlock3and4Components = []
    trialBlock3and4Components.append(stimulusAbox3and4)
    trialBlock3and4Components.append(responseRequired3and4)
    trialBlock3and4Components.append(responseFeedback3and4)
    trialBlock3and4Components.append(accuracyFeedback3and4)
    trialBlock3and4Components.append(target1box3and4)
    trialBlock3and4Components.append(attribute1box3and4)
    trialBlock3and4Components.append(target2box3and4)
    trialBlock3and4Components.append(attribute2box3and4)
    trialBlock3and4Components.append(orLeftBox3and4)
    trialBlock3and4Components.append(orRightBox3and4)
    for thisComponent in trialBlock3and4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trialBlock3and4"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialBlock3and4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusAbox3and4* updates
        if t >= 0.3 and stimulusAbox3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusAbox3and4.tStart = t  # underestimates by a little under one frame
            stimulusAbox3and4.frameNStart = frameN  # exact frame index
            stimulusAbox3and4.setAutoDraw(True)
        
        # *responseRequired3and4* updates
        if t >= 0.3 and responseRequired3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseRequired3and4.tStart = t  # underestimates by a little under one frame
            responseRequired3and4.frameNStart = frameN  # exact frame index
            responseRequired3and4.status = STARTED
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
            responseRequired3and4.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseRequired3and4.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowed))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseRequired3and4.keys == []:  # then this was the first keypress
                    responseRequired3and4.keys = theseKeys[0]  # just the first key pressed
                    responseRequired3and4.rt = responseRequired3and4.clock.getTime()
                    # was this 'correct'?
                    if (responseRequired3and4.keys == str(requiredResponse)) or (responseRequired3and4.keys == requiredResponse):
                        responseRequired3and4.corr = 1
                    else:
                        responseRequired3and4.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *responseFeedback3and4* updates
        if t >= 0.3 and responseFeedback3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseFeedback3and4.tStart = t  # underestimates by a little under one frame
            responseFeedback3and4.frameNStart = frameN  # exact frame index
            responseFeedback3and4.status = STARTED
            # AllowedKeys looks like a variable named `feedbackResponse`
            if not 'feedbackResponse' in locals():
                logging.error('AllowedKeys variable `feedbackResponse` is not defined.')
                core.quit()
            if not type(feedbackResponse) in [list, tuple, np.ndarray]:
                if not isinstance(feedbackResponse, basestring):
                    logging.error('AllowedKeys variable `feedbackResponse` is not string- or list-like.')
                    core.quit()
                elif not ',' in feedbackResponse: feedbackResponse = (feedbackResponse,)
                else:  feedbackResponse = eval(feedbackResponse)
            # keyboard checking is just starting
            responseFeedback3and4.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseFeedback3and4.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackResponse))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseFeedback3and4.keys == []:  # then this was the first keypress
                    responseFeedback3and4.keys = theseKeys[0]  # just the first key pressed
                    responseFeedback3and4.rt = responseFeedback3and4.clock.getTime()
                    # was this 'correct'?
                    if (responseFeedback3and4.keys == str(feedbackAllowed)) or (responseFeedback3and4.keys == feedbackAllowed):
                        responseFeedback3and4.corr = 1
                    else:
                        responseFeedback3and4.corr = 0
        if len(responseFeedback3and4.keys)<1:
            msg1=""
        else:
            msg1="X"
        
        # *accuracyFeedback3and4* updates
        if t >= 0.3 and accuracyFeedback3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            accuracyFeedback3and4.tStart = t  # underestimates by a little under one frame
            accuracyFeedback3and4.frameNStart = frameN  # exact frame index
            accuracyFeedback3and4.setAutoDraw(True)
        if accuracyFeedback3and4.status == STARTED:  # only update if being drawn
            accuracyFeedback3and4.setText(msg1, log=False)
        
        # *target1box3and4* updates
        if t >= 0.0 and target1box3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box3and4.tStart = t  # underestimates by a little under one frame
            target1box3and4.frameNStart = frameN  # exact frame index
            target1box3and4.setAutoDraw(True)
        
        # *attribute1box3and4* updates
        if t >= 0.0 and attribute1box3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box3and4.tStart = t  # underestimates by a little under one frame
            attribute1box3and4.frameNStart = frameN  # exact frame index
            attribute1box3and4.setAutoDraw(True)
        
        # *target2box3and4* updates
        if t >= 0.0 and target2box3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box3and4.tStart = t  # underestimates by a little under one frame
            target2box3and4.frameNStart = frameN  # exact frame index
            target2box3and4.setAutoDraw(True)
        
        # *attribute2box3and4* updates
        if t >= 0.0 and attribute2box3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box3and4.tStart = t  # underestimates by a little under one frame
            attribute2box3and4.frameNStart = frameN  # exact frame index
            attribute2box3and4.setAutoDraw(True)
        
        # *orLeftBox3and4* updates
        if t >= 0.0 and orLeftBox3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox3and4.tStart = t  # underestimates by a little under one frame
            orLeftBox3and4.frameNStart = frameN  # exact frame index
            orLeftBox3and4.setAutoDraw(True)
        
        # *orRightBox3and4* updates
        if t >= 0.0 and orRightBox3and4.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox3and4.tStart = t  # underestimates by a little under one frame
            orRightBox3and4.frameNStart = frameN  # exact frame index
            orRightBox3and4.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialBlock3and4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trialBlock3and4"-------
    for thisComponent in trialBlock3and4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseRequired3and4.keys in ['', [], None]:  # No response was made
       responseRequired3and4.keys=None
       # was no response the correct answer?!
       if str(requiredResponse).lower() == 'none': responseRequired3and4.corr = 1  # correct non-response
       else: responseRequired3and4.corr = 0  # failed to respond (incorrectly)
    # store data for block4Loop (TrialHandler)
    block4Loop.addData('responseRequired3and4.keys',responseRequired3and4.keys)
    block4Loop.addData('responseRequired3and4.corr', responseRequired3and4.corr)
    if responseRequired3and4.keys != None:  # we had a response
        block4Loop.addData('responseRequired3and4.rt', responseRequired3and4.rt)
    # check responses
    if responseFeedback3and4.keys in ['', [], None]:  # No response was made
       responseFeedback3and4.keys=None
       # was no response the correct answer?!
       if str(feedbackAllowed).lower() == 'none': responseFeedback3and4.corr = 1  # correct non-response
       else: responseFeedback3and4.corr = 0  # failed to respond (incorrectly)
    # store data for block4Loop (TrialHandler)
    block4Loop.addData('responseFeedback3and4.keys',responseFeedback3and4.keys)
    block4Loop.addData('responseFeedback3and4.corr', responseFeedback3and4.corr)
    if responseFeedback3and4.keys != None:  # we had a response
        block4Loop.addData('responseFeedback3and4.rt', responseFeedback3and4.rt)
    
    # the Routine "trialBlock3and4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'block4Loop'


# set up handler to look after randomisation of conditions etc
instructionsLoop5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Instructions.xlsx', selection='4'),
    seed=None, name='instructionsLoop5')
thisExp.addLoop(instructionsLoop5)  # add the loop to the experiment
thisInstructionsLoop5 = instructionsLoop5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstructionsLoop5.rgb)
if thisInstructionsLoop5 != None:
    for paramName in thisInstructionsLoop5.keys():
        exec(paramName + '= thisInstructionsLoop5.' + paramName)

for thisInstructionsLoop5 in instructionsLoop5:
    currentLoop = instructionsLoop5
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop5.rgb)
    if thisInstructionsLoop5 != None:
        for paramName in thisInstructionsLoop5.keys():
            exec(paramName + '= thisInstructionsLoop5.' + paramName)
    
    #------Prepare to start Routine "instructions1and5"-------
    t = 0
    instructions1and5Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox1_2.setText(instruction)
    responseContinue1_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue1_2.status = NOT_STARTED
    target1box1_inst_2.setText(targetLeft)
    target2box1_inst_2.setText(targetRight)
    # keep track of which components have finished
    instructions1and5Components = []
    instructions1and5Components.append(instructionsBox1_2)
    instructions1and5Components.append(responseContinue1_2)
    instructions1and5Components.append(target1box1_inst_2)
    instructions1and5Components.append(target2box1_inst_2)
    for thisComponent in instructions1and5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions1and5"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions1and5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox1_2* updates
        if t >= 0.3 and instructionsBox1_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox1_2.tStart = t  # underestimates by a little under one frame
            instructionsBox1_2.frameNStart = frameN  # exact frame index
            instructionsBox1_2.setAutoDraw(True)
        
        # *responseContinue1_2* updates
        if t >= 0.3 and responseContinue1_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue1_2.tStart = t  # underestimates by a little under one frame
            responseContinue1_2.frameNStart = frameN  # exact frame index
            responseContinue1_2.status = STARTED
            # keyboard checking is just starting
            responseContinue1_2.clock.reset()  # now t=0
        if responseContinue1_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseContinue1_2.keys == []:  # then this was the first keypress
                    responseContinue1_2.keys = theseKeys[0]  # just the first key pressed
                    responseContinue1_2.rt = responseContinue1_2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *target1box1_inst_2* updates
        if t >= 0.0 and target1box1_inst_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box1_inst_2.tStart = t  # underestimates by a little under one frame
            target1box1_inst_2.frameNStart = frameN  # exact frame index
            target1box1_inst_2.setAutoDraw(True)
        
        # *target2box1_inst_2* updates
        if t >= 0.0 and target2box1_inst_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box1_inst_2.tStart = t  # underestimates by a little under one frame
            target2box1_inst_2.frameNStart = frameN  # exact frame index
            target2box1_inst_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions1and5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions1and5"-------
    for thisComponent in instructions1and5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseContinue1_2.keys in ['', [], None]:  # No response was made
       responseContinue1_2.keys=None
    # store data for instructionsLoop5 (TrialHandler)
    instructionsLoop5.addData('responseContinue1_2.keys',responseContinue1_2.keys)
    if responseContinue1_2.keys != None:  # we had a response
        instructionsLoop5.addData('responseContinue1_2.rt', responseContinue1_2.rt)
    # the Routine "instructions1and5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructionsLoop5'


# set up handler to look after randomisation of conditions etc
block5Loop = data.TrialHandler(nReps=4, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Stimuli.xlsx', selection='0:10'),
    seed=None, name='block5Loop')
thisExp.addLoop(block5Loop)  # add the loop to the experiment
thisBlock5Loop = block5Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock5Loop.rgb)
if thisBlock5Loop != None:
    for paramName in thisBlock5Loop.keys():
        exec(paramName + '= thisBlock5Loop.' + paramName)

for thisBlock5Loop in block5Loop:
    currentLoop = block5Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock5Loop.rgb)
    if thisBlock5Loop != None:
        for paramName in thisBlock5Loop.keys():
            exec(paramName + '= thisBlock5Loop.' + paramName)
    
    #------Prepare to start Routine "trialBlock5"-------
    t = 0
    trialBlock5Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusAbox5.setColor(stimulusColour, colorSpace='rgb')
    stimulusAbox5.setText(stimulusB)
    responseRequired5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseRequired5.status = NOT_STARTED
    responseFeedback5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseFeedback5.status = NOT_STARTED
    
    target1box5.setText(target1)
    target2box5.setText(target2)
    # keep track of which components have finished
    trialBlock5Components = []
    trialBlock5Components.append(stimulusAbox5)
    trialBlock5Components.append(responseRequired5)
    trialBlock5Components.append(responseFeedback5)
    trialBlock5Components.append(accuracyFeedback5)
    trialBlock5Components.append(target1box5)
    trialBlock5Components.append(target2box5)
    for thisComponent in trialBlock5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trialBlock5"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialBlock5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusAbox5* updates
        if t >= 0.3 and stimulusAbox5.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusAbox5.tStart = t  # underestimates by a little under one frame
            stimulusAbox5.frameNStart = frameN  # exact frame index
            stimulusAbox5.setAutoDraw(True)
        
        # *responseRequired5* updates
        if t >= 0.3 and responseRequired5.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseRequired5.tStart = t  # underestimates by a little under one frame
            responseRequired5.frameNStart = frameN  # exact frame index
            responseRequired5.status = STARTED
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
            responseRequired5.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseRequired5.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowed))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseRequired5.keys == []:  # then this was the first keypress
                    responseRequired5.keys = theseKeys[0]  # just the first key pressed
                    responseRequired5.rt = responseRequired5.clock.getTime()
                    # was this 'correct'?
                    if (responseRequired5.keys == str(requiredResponse)) or (responseRequired5.keys == requiredResponse):
                        responseRequired5.corr = 1
                    else:
                        responseRequired5.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *responseFeedback5* updates
        if t >= 0.3 and responseFeedback5.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseFeedback5.tStart = t  # underestimates by a little under one frame
            responseFeedback5.frameNStart = frameN  # exact frame index
            responseFeedback5.status = STARTED
            # AllowedKeys looks like a variable named `feedbackResponse`
            if not 'feedbackResponse' in locals():
                logging.error('AllowedKeys variable `feedbackResponse` is not defined.')
                core.quit()
            if not type(feedbackResponse) in [list, tuple, np.ndarray]:
                if not isinstance(feedbackResponse, basestring):
                    logging.error('AllowedKeys variable `feedbackResponse` is not string- or list-like.')
                    core.quit()
                elif not ',' in feedbackResponse: feedbackResponse = (feedbackResponse,)
                else:  feedbackResponse = eval(feedbackResponse)
            # keyboard checking is just starting
            responseFeedback5.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseFeedback5.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackResponse))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseFeedback5.keys == []:  # then this was the first keypress
                    responseFeedback5.keys = theseKeys[0]  # just the first key pressed
                    responseFeedback5.rt = responseFeedback5.clock.getTime()
                    # was this 'correct'?
                    if (responseFeedback5.keys == str(feedbackAllowed)) or (responseFeedback5.keys == feedbackAllowed):
                        responseFeedback5.corr = 1
                    else:
                        responseFeedback5.corr = 0
        if len(responseFeedback5.keys)<1:
            msg1=""
        else:
            msg1="X"
        
        # *accuracyFeedback5* updates
        if t >= 0.3 and accuracyFeedback5.status == NOT_STARTED:
            # keep track of start time/frame for later
            accuracyFeedback5.tStart = t  # underestimates by a little under one frame
            accuracyFeedback5.frameNStart = frameN  # exact frame index
            accuracyFeedback5.setAutoDraw(True)
        if accuracyFeedback5.status == STARTED:  # only update if being drawn
            accuracyFeedback5.setText(msg1, log=False)
        
        # *target1box5* updates
        if t >= 0.0 and target1box5.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box5.tStart = t  # underestimates by a little under one frame
            target1box5.frameNStart = frameN  # exact frame index
            target1box5.setAutoDraw(True)
        
        # *target2box5* updates
        if t >= 0.0 and target2box5.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box5.tStart = t  # underestimates by a little under one frame
            target2box5.frameNStart = frameN  # exact frame index
            target2box5.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialBlock5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trialBlock5"-------
    for thisComponent in trialBlock5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseRequired5.keys in ['', [], None]:  # No response was made
       responseRequired5.keys=None
       # was no response the correct answer?!
       if str(requiredResponse).lower() == 'none': responseRequired5.corr = 1  # correct non-response
       else: responseRequired5.corr = 0  # failed to respond (incorrectly)
    # store data for block5Loop (TrialHandler)
    block5Loop.addData('responseRequired5.keys',responseRequired5.keys)
    block5Loop.addData('responseRequired5.corr', responseRequired5.corr)
    if responseRequired5.keys != None:  # we had a response
        block5Loop.addData('responseRequired5.rt', responseRequired5.rt)
    # check responses
    if responseFeedback5.keys in ['', [], None]:  # No response was made
       responseFeedback5.keys=None
       # was no response the correct answer?!
       if str(feedbackAllowed).lower() == 'none': responseFeedback5.corr = 1  # correct non-response
       else: responseFeedback5.corr = 0  # failed to respond (incorrectly)
    # store data for block5Loop (TrialHandler)
    block5Loop.addData('responseFeedback5.keys',responseFeedback5.keys)
    block5Loop.addData('responseFeedback5.corr', responseFeedback5.corr)
    if responseFeedback5.keys != None:  # we had a response
        block5Loop.addData('responseFeedback5.rt', responseFeedback5.rt)
    
    # the Routine "trialBlock5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4 repeats of 'block5Loop'


# set up handler to look after randomisation of conditions etc
instructionsLoop6 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Instructions.xlsx', selection='5'),
    seed=None, name='instructionsLoop6')
thisExp.addLoop(instructionsLoop6)  # add the loop to the experiment
thisInstructionsLoop6 = instructionsLoop6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstructionsLoop6.rgb)
if thisInstructionsLoop6 != None:
    for paramName in thisInstructionsLoop6.keys():
        exec(paramName + '= thisInstructionsLoop6.' + paramName)

for thisInstructionsLoop6 in instructionsLoop6:
    currentLoop = instructionsLoop6
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop6.rgb)
    if thisInstructionsLoop6 != None:
        for paramName in thisInstructionsLoop6.keys():
            exec(paramName + '= thisInstructionsLoop6.' + paramName)
    
    #------Prepare to start Routine "instructions3467"-------
    t = 0
    instructions3467Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox3467.setText(instruction)
    responseContinue3467 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue3467.status = NOT_STARTED
    target1box3467.setText(targetLeft)
    attribute1box3467.setColor([-1, 1, -1], colorSpace='rgb')
    attribute1box3467.setText(attributeLeft)
    target2box3467.setText(targetRight)
    attribute2box3467.setText(attributeRight)
    orLeftBox3467.setText(orStimulus)
    orRightBox3467.setText(orStimulus)
    # keep track of which components have finished
    instructions3467Components = []
    instructions3467Components.append(instructionsBox3467)
    instructions3467Components.append(responseContinue3467)
    instructions3467Components.append(target1box3467)
    instructions3467Components.append(attribute1box3467)
    instructions3467Components.append(target2box3467)
    instructions3467Components.append(attribute2box3467)
    instructions3467Components.append(orLeftBox3467)
    instructions3467Components.append(orRightBox3467)
    for thisComponent in instructions3467Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions3467"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions3467Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox3467* updates
        if t >= 0.3 and instructionsBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox3467.tStart = t  # underestimates by a little under one frame
            instructionsBox3467.frameNStart = frameN  # exact frame index
            instructionsBox3467.setAutoDraw(True)
        
        # *responseContinue3467* updates
        if t >= 0.3 and responseContinue3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue3467.tStart = t  # underestimates by a little under one frame
            responseContinue3467.frameNStart = frameN  # exact frame index
            responseContinue3467.status = STARTED
            # keyboard checking is just starting
            responseContinue3467.clock.reset()  # now t=0
        if responseContinue3467.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseContinue3467.keys == []:  # then this was the first keypress
                    responseContinue3467.keys = theseKeys[0]  # just the first key pressed
                    responseContinue3467.rt = responseContinue3467.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *target1box3467* updates
        if t >= 0.0 and target1box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box3467.tStart = t  # underestimates by a little under one frame
            target1box3467.frameNStart = frameN  # exact frame index
            target1box3467.setAutoDraw(True)
        
        # *attribute1box3467* updates
        if t >= 0.0 and attribute1box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box3467.tStart = t  # underestimates by a little under one frame
            attribute1box3467.frameNStart = frameN  # exact frame index
            attribute1box3467.setAutoDraw(True)
        
        # *target2box3467* updates
        if t >= 0.0 and target2box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box3467.tStart = t  # underestimates by a little under one frame
            target2box3467.frameNStart = frameN  # exact frame index
            target2box3467.setAutoDraw(True)
        
        # *attribute2box3467* updates
        if t >= 0.0 and attribute2box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box3467.tStart = t  # underestimates by a little under one frame
            attribute2box3467.frameNStart = frameN  # exact frame index
            attribute2box3467.setAutoDraw(True)
        
        # *orLeftBox3467* updates
        if t >= 0.0 and orLeftBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox3467.tStart = t  # underestimates by a little under one frame
            orLeftBox3467.frameNStart = frameN  # exact frame index
            orLeftBox3467.setAutoDraw(True)
        
        # *orRightBox3467* updates
        if t >= 0.0 and orRightBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox3467.tStart = t  # underestimates by a little under one frame
            orRightBox3467.frameNStart = frameN  # exact frame index
            orRightBox3467.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions3467Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions3467"-------
    for thisComponent in instructions3467Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseContinue3467.keys in ['', [], None]:  # No response was made
       responseContinue3467.keys=None
    # store data for instructionsLoop6 (TrialHandler)
    instructionsLoop6.addData('responseContinue3467.keys',responseContinue3467.keys)
    if responseContinue3467.keys != None:  # we had a response
        instructionsLoop6.addData('responseContinue3467.rt', responseContinue3467.rt)
    # the Routine "instructions3467" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructionsLoop6'


# set up handler to look after randomisation of conditions etc
block6Loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Stimuli.xlsx'),
    seed=None, name='block6Loop')
thisExp.addLoop(block6Loop)  # add the loop to the experiment
thisBlock6Loop = block6Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock6Loop.rgb)
if thisBlock6Loop != None:
    for paramName in thisBlock6Loop.keys():
        exec(paramName + '= thisBlock6Loop.' + paramName)

for thisBlock6Loop in block6Loop:
    currentLoop = block6Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock6Loop.rgb)
    if thisBlock6Loop != None:
        for paramName in thisBlock6Loop.keys():
            exec(paramName + '= thisBlock6Loop.' + paramName)
    
    #------Prepare to start Routine "trialBlock6and7"-------
    t = 0
    trialBlock6and7Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusBbox6and7.setColor(stimulusColour, colorSpace='rgb')
    stimulusBbox6and7.setText(stimulusB)
    responseRequired6and7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseRequired6and7.status = NOT_STARTED
    responseFeedback6and7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseFeedback6and7.status = NOT_STARTED
    
    target1box6and7.setText(target1)
    attribute1box6and7.setColor([-1, 1, -1], colorSpace='rgb')
    attribute1box6and7.setText(attribute1
)
    target2box6and7.setText(target2)
    attribute2box6and7.setText(attribute2)
    orLeftBox6and7.setText(orStimulus)
    orRightBox6and7.setText(orStimulus)
    # keep track of which components have finished
    trialBlock6and7Components = []
    trialBlock6and7Components.append(stimulusBbox6and7)
    trialBlock6and7Components.append(responseRequired6and7)
    trialBlock6and7Components.append(responseFeedback6and7)
    trialBlock6and7Components.append(accuracyFeedback6and7)
    trialBlock6and7Components.append(target1box6and7)
    trialBlock6and7Components.append(attribute1box6and7)
    trialBlock6and7Components.append(target2box6and7)
    trialBlock6and7Components.append(attribute2box6and7)
    trialBlock6and7Components.append(orLeftBox6and7)
    trialBlock6and7Components.append(orRightBox6and7)
    for thisComponent in trialBlock6and7Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trialBlock6and7"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialBlock6and7Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusBbox6and7* updates
        if t >= 0.3 and stimulusBbox6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusBbox6and7.tStart = t  # underestimates by a little under one frame
            stimulusBbox6and7.frameNStart = frameN  # exact frame index
            stimulusBbox6and7.setAutoDraw(True)
        
        # *responseRequired6and7* updates
        if t >= 0.3 and responseRequired6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseRequired6and7.tStart = t  # underestimates by a little under one frame
            responseRequired6and7.frameNStart = frameN  # exact frame index
            responseRequired6and7.status = STARTED
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
            responseRequired6and7.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseRequired6and7.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowed))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseRequired6and7.keys == []:  # then this was the first keypress
                    responseRequired6and7.keys = theseKeys[0]  # just the first key pressed
                    responseRequired6and7.rt = responseRequired6and7.clock.getTime()
                    # was this 'correct'?
                    if (responseRequired6and7.keys == str(requiredResponse)) or (responseRequired6and7.keys == requiredResponse):
                        responseRequired6and7.corr = 1
                    else:
                        responseRequired6and7.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *responseFeedback6and7* updates
        if t >= 0.3 and responseFeedback6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseFeedback6and7.tStart = t  # underestimates by a little under one frame
            responseFeedback6and7.frameNStart = frameN  # exact frame index
            responseFeedback6and7.status = STARTED
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
            responseFeedback6and7.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseFeedback6and7.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowed))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseFeedback6and7.keys == []:  # then this was the first keypress
                    responseFeedback6and7.keys = theseKeys[0]  # just the first key pressed
                    responseFeedback6and7.rt = responseFeedback6and7.clock.getTime()
                    # was this 'correct'?
                    if (responseFeedback6and7.keys == str('feedbackResponse')) or (responseFeedback6and7.keys == 'feedbackResponse'):
                        responseFeedback6and7.corr = 1
                    else:
                        responseFeedback6and7.corr = 0
        if len(responseFeedback6and7.keys)<1:
            msg1=""
        else:
            msg1="X"
        
        # *accuracyFeedback6and7* updates
        if t >= 0.3 and accuracyFeedback6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            accuracyFeedback6and7.tStart = t  # underestimates by a little under one frame
            accuracyFeedback6and7.frameNStart = frameN  # exact frame index
            accuracyFeedback6and7.setAutoDraw(True)
        if accuracyFeedback6and7.status == STARTED:  # only update if being drawn
            accuracyFeedback6and7.setText(msg1, log=False)
        
        # *target1box6and7* updates
        if t >= 0.0 and target1box6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box6and7.tStart = t  # underestimates by a little under one frame
            target1box6and7.frameNStart = frameN  # exact frame index
            target1box6and7.setAutoDraw(True)
        
        # *attribute1box6and7* updates
        if t >= 0.0 and attribute1box6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box6and7.tStart = t  # underestimates by a little under one frame
            attribute1box6and7.frameNStart = frameN  # exact frame index
            attribute1box6and7.setAutoDraw(True)
        
        # *target2box6and7* updates
        if t >= 0.0 and target2box6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box6and7.tStart = t  # underestimates by a little under one frame
            target2box6and7.frameNStart = frameN  # exact frame index
            target2box6and7.setAutoDraw(True)
        
        # *attribute2box6and7* updates
        if t >= 0.0 and attribute2box6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box6and7.tStart = t  # underestimates by a little under one frame
            attribute2box6and7.frameNStart = frameN  # exact frame index
            attribute2box6and7.setAutoDraw(True)
        
        # *orLeftBox6and7* updates
        if t >= 0.0 and orLeftBox6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox6and7.tStart = t  # underestimates by a little under one frame
            orLeftBox6and7.frameNStart = frameN  # exact frame index
            orLeftBox6and7.setAutoDraw(True)
        
        # *orRightBox6and7* updates
        if t >= 0.0 and orRightBox6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox6and7.tStart = t  # underestimates by a little under one frame
            orRightBox6and7.frameNStart = frameN  # exact frame index
            orRightBox6and7.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialBlock6and7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trialBlock6and7"-------
    for thisComponent in trialBlock6and7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseRequired6and7.keys in ['', [], None]:  # No response was made
       responseRequired6and7.keys=None
       # was no response the correct answer?!
       if str(requiredResponse).lower() == 'none': responseRequired6and7.corr = 1  # correct non-response
       else: responseRequired6and7.corr = 0  # failed to respond (incorrectly)
    # store data for block6Loop (TrialHandler)
    block6Loop.addData('responseRequired6and7.keys',responseRequired6and7.keys)
    block6Loop.addData('responseRequired6and7.corr', responseRequired6and7.corr)
    if responseRequired6and7.keys != None:  # we had a response
        block6Loop.addData('responseRequired6and7.rt', responseRequired6and7.rt)
    # check responses
    if responseFeedback6and7.keys in ['', [], None]:  # No response was made
       responseFeedback6and7.keys=None
       # was no response the correct answer?!
       if str('feedbackResponse').lower() == 'none': responseFeedback6and7.corr = 1  # correct non-response
       else: responseFeedback6and7.corr = 0  # failed to respond (incorrectly)
    # store data for block6Loop (TrialHandler)
    block6Loop.addData('responseFeedback6and7.keys',responseFeedback6and7.keys)
    block6Loop.addData('responseFeedback6and7.corr', responseFeedback6and7.corr)
    if responseFeedback6and7.keys != None:  # we had a response
        block6Loop.addData('responseFeedback6and7.rt', responseFeedback6and7.rt)
    
    # the Routine "trialBlock6and7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'block6Loop'


# set up handler to look after randomisation of conditions etc
instructionsLoop7 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Instructions.xlsx', selection='6'),
    seed=None, name='instructionsLoop7')
thisExp.addLoop(instructionsLoop7)  # add the loop to the experiment
thisInstructionsLoop7 = instructionsLoop7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstructionsLoop7.rgb)
if thisInstructionsLoop7 != None:
    for paramName in thisInstructionsLoop7.keys():
        exec(paramName + '= thisInstructionsLoop7.' + paramName)

for thisInstructionsLoop7 in instructionsLoop7:
    currentLoop = instructionsLoop7
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop7.rgb)
    if thisInstructionsLoop7 != None:
        for paramName in thisInstructionsLoop7.keys():
            exec(paramName + '= thisInstructionsLoop7.' + paramName)
    
    #------Prepare to start Routine "instructions3467"-------
    t = 0
    instructions3467Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instructionsBox3467.setText(instruction)
    responseContinue3467 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseContinue3467.status = NOT_STARTED
    target1box3467.setText(targetLeft)
    attribute1box3467.setColor([-1, 1, -1], colorSpace='rgb')
    attribute1box3467.setText(attributeLeft)
    target2box3467.setText(targetRight)
    attribute2box3467.setText(attributeRight)
    orLeftBox3467.setText(orStimulus)
    orRightBox3467.setText(orStimulus)
    # keep track of which components have finished
    instructions3467Components = []
    instructions3467Components.append(instructionsBox3467)
    instructions3467Components.append(responseContinue3467)
    instructions3467Components.append(target1box3467)
    instructions3467Components.append(attribute1box3467)
    instructions3467Components.append(target2box3467)
    instructions3467Components.append(attribute2box3467)
    instructions3467Components.append(orLeftBox3467)
    instructions3467Components.append(orRightBox3467)
    for thisComponent in instructions3467Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions3467"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions3467Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsBox3467* updates
        if t >= 0.3 and instructionsBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionsBox3467.tStart = t  # underestimates by a little under one frame
            instructionsBox3467.frameNStart = frameN  # exact frame index
            instructionsBox3467.setAutoDraw(True)
        
        # *responseContinue3467* updates
        if t >= 0.3 and responseContinue3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseContinue3467.tStart = t  # underestimates by a little under one frame
            responseContinue3467.frameNStart = frameN  # exact frame index
            responseContinue3467.status = STARTED
            # keyboard checking is just starting
            responseContinue3467.clock.reset()  # now t=0
        if responseContinue3467.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseContinue3467.keys == []:  # then this was the first keypress
                    responseContinue3467.keys = theseKeys[0]  # just the first key pressed
                    responseContinue3467.rt = responseContinue3467.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *target1box3467* updates
        if t >= 0.0 and target1box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box3467.tStart = t  # underestimates by a little under one frame
            target1box3467.frameNStart = frameN  # exact frame index
            target1box3467.setAutoDraw(True)
        
        # *attribute1box3467* updates
        if t >= 0.0 and attribute1box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box3467.tStart = t  # underestimates by a little under one frame
            attribute1box3467.frameNStart = frameN  # exact frame index
            attribute1box3467.setAutoDraw(True)
        
        # *target2box3467* updates
        if t >= 0.0 and target2box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box3467.tStart = t  # underestimates by a little under one frame
            target2box3467.frameNStart = frameN  # exact frame index
            target2box3467.setAutoDraw(True)
        
        # *attribute2box3467* updates
        if t >= 0.0 and attribute2box3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box3467.tStart = t  # underestimates by a little under one frame
            attribute2box3467.frameNStart = frameN  # exact frame index
            attribute2box3467.setAutoDraw(True)
        
        # *orLeftBox3467* updates
        if t >= 0.0 and orLeftBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox3467.tStart = t  # underestimates by a little under one frame
            orLeftBox3467.frameNStart = frameN  # exact frame index
            orLeftBox3467.setAutoDraw(True)
        
        # *orRightBox3467* updates
        if t >= 0.0 and orRightBox3467.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox3467.tStart = t  # underestimates by a little under one frame
            orRightBox3467.frameNStart = frameN  # exact frame index
            orRightBox3467.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions3467Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions3467"-------
    for thisComponent in instructions3467Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseContinue3467.keys in ['', [], None]:  # No response was made
       responseContinue3467.keys=None
    # store data for instructionsLoop7 (TrialHandler)
    instructionsLoop7.addData('responseContinue3467.keys',responseContinue3467.keys)
    if responseContinue3467.keys != None:  # we had a response
        instructionsLoop7.addData('responseContinue3467.rt', responseContinue3467.rt)
    # the Routine "instructions3467" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructionsLoop7'


# set up handler to look after randomisation of conditions etc
block7Loop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Stimuli.xlsx'),
    seed=None, name='block7Loop')
thisExp.addLoop(block7Loop)  # add the loop to the experiment
thisBlock7Loop = block7Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock7Loop.rgb)
if thisBlock7Loop != None:
    for paramName in thisBlock7Loop.keys():
        exec(paramName + '= thisBlock7Loop.' + paramName)

for thisBlock7Loop in block7Loop:
    currentLoop = block7Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock7Loop.rgb)
    if thisBlock7Loop != None:
        for paramName in thisBlock7Loop.keys():
            exec(paramName + '= thisBlock7Loop.' + paramName)
    
    #------Prepare to start Routine "trialBlock6and7"-------
    t = 0
    trialBlock6and7Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimulusBbox6and7.setColor(stimulusColour, colorSpace='rgb')
    stimulusBbox6and7.setText(stimulusB)
    responseRequired6and7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseRequired6and7.status = NOT_STARTED
    responseFeedback6and7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseFeedback6and7.status = NOT_STARTED
    
    target1box6and7.setText(target1)
    attribute1box6and7.setColor([-1, 1, -1], colorSpace='rgb')
    attribute1box6and7.setText(attribute1
)
    target2box6and7.setText(target2)
    attribute2box6and7.setText(attribute2)
    orLeftBox6and7.setText(orStimulus)
    orRightBox6and7.setText(orStimulus)
    # keep track of which components have finished
    trialBlock6and7Components = []
    trialBlock6and7Components.append(stimulusBbox6and7)
    trialBlock6and7Components.append(responseRequired6and7)
    trialBlock6and7Components.append(responseFeedback6and7)
    trialBlock6and7Components.append(accuracyFeedback6and7)
    trialBlock6and7Components.append(target1box6and7)
    trialBlock6and7Components.append(attribute1box6and7)
    trialBlock6and7Components.append(target2box6and7)
    trialBlock6and7Components.append(attribute2box6and7)
    trialBlock6and7Components.append(orLeftBox6and7)
    trialBlock6and7Components.append(orRightBox6and7)
    for thisComponent in trialBlock6and7Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trialBlock6and7"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialBlock6and7Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulusBbox6and7* updates
        if t >= 0.3 and stimulusBbox6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulusBbox6and7.tStart = t  # underestimates by a little under one frame
            stimulusBbox6and7.frameNStart = frameN  # exact frame index
            stimulusBbox6and7.setAutoDraw(True)
        
        # *responseRequired6and7* updates
        if t >= 0.3 and responseRequired6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseRequired6and7.tStart = t  # underestimates by a little under one frame
            responseRequired6and7.frameNStart = frameN  # exact frame index
            responseRequired6and7.status = STARTED
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
            responseRequired6and7.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseRequired6and7.status == STARTED:
            theseKeys = event.getKeys(keyList=list(requiredAllowed))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseRequired6and7.keys == []:  # then this was the first keypress
                    responseRequired6and7.keys = theseKeys[0]  # just the first key pressed
                    responseRequired6and7.rt = responseRequired6and7.clock.getTime()
                    # was this 'correct'?
                    if (responseRequired6and7.keys == str(requiredResponse)) or (responseRequired6and7.keys == requiredResponse):
                        responseRequired6and7.corr = 1
                    else:
                        responseRequired6and7.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *responseFeedback6and7* updates
        if t >= 0.3 and responseFeedback6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseFeedback6and7.tStart = t  # underestimates by a little under one frame
            responseFeedback6and7.frameNStart = frameN  # exact frame index
            responseFeedback6and7.status = STARTED
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
            responseFeedback6and7.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseFeedback6and7.status == STARTED:
            theseKeys = event.getKeys(keyList=list(feedbackAllowed))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if responseFeedback6and7.keys == []:  # then this was the first keypress
                    responseFeedback6and7.keys = theseKeys[0]  # just the first key pressed
                    responseFeedback6and7.rt = responseFeedback6and7.clock.getTime()
                    # was this 'correct'?
                    if (responseFeedback6and7.keys == str('feedbackResponse')) or (responseFeedback6and7.keys == 'feedbackResponse'):
                        responseFeedback6and7.corr = 1
                    else:
                        responseFeedback6and7.corr = 0
        if len(responseFeedback6and7.keys)<1:
            msg1=""
        else:
            msg1="X"
        
        # *accuracyFeedback6and7* updates
        if t >= 0.3 and accuracyFeedback6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            accuracyFeedback6and7.tStart = t  # underestimates by a little under one frame
            accuracyFeedback6and7.frameNStart = frameN  # exact frame index
            accuracyFeedback6and7.setAutoDraw(True)
        if accuracyFeedback6and7.status == STARTED:  # only update if being drawn
            accuracyFeedback6and7.setText(msg1, log=False)
        
        # *target1box6and7* updates
        if t >= 0.0 and target1box6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            target1box6and7.tStart = t  # underestimates by a little under one frame
            target1box6and7.frameNStart = frameN  # exact frame index
            target1box6and7.setAutoDraw(True)
        
        # *attribute1box6and7* updates
        if t >= 0.0 and attribute1box6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute1box6and7.tStart = t  # underestimates by a little under one frame
            attribute1box6and7.frameNStart = frameN  # exact frame index
            attribute1box6and7.setAutoDraw(True)
        
        # *target2box6and7* updates
        if t >= 0.0 and target2box6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            target2box6and7.tStart = t  # underestimates by a little under one frame
            target2box6and7.frameNStart = frameN  # exact frame index
            target2box6and7.setAutoDraw(True)
        
        # *attribute2box6and7* updates
        if t >= 0.0 and attribute2box6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            attribute2box6and7.tStart = t  # underestimates by a little under one frame
            attribute2box6and7.frameNStart = frameN  # exact frame index
            attribute2box6and7.setAutoDraw(True)
        
        # *orLeftBox6and7* updates
        if t >= 0.0 and orLeftBox6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLeftBox6and7.tStart = t  # underestimates by a little under one frame
            orLeftBox6and7.frameNStart = frameN  # exact frame index
            orLeftBox6and7.setAutoDraw(True)
        
        # *orRightBox6and7* updates
        if t >= 0.0 and orRightBox6and7.status == NOT_STARTED:
            # keep track of start time/frame for later
            orRightBox6and7.tStart = t  # underestimates by a little under one frame
            orRightBox6and7.frameNStart = frameN  # exact frame index
            orRightBox6and7.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialBlock6and7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trialBlock6and7"-------
    for thisComponent in trialBlock6and7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if responseRequired6and7.keys in ['', [], None]:  # No response was made
       responseRequired6and7.keys=None
       # was no response the correct answer?!
       if str(requiredResponse).lower() == 'none': responseRequired6and7.corr = 1  # correct non-response
       else: responseRequired6and7.corr = 0  # failed to respond (incorrectly)
    # store data for block7Loop (TrialHandler)
    block7Loop.addData('responseRequired6and7.keys',responseRequired6and7.keys)
    block7Loop.addData('responseRequired6and7.corr', responseRequired6and7.corr)
    if responseRequired6and7.keys != None:  # we had a response
        block7Loop.addData('responseRequired6and7.rt', responseRequired6and7.rt)
    # check responses
    if responseFeedback6and7.keys in ['', [], None]:  # No response was made
       responseFeedback6and7.keys=None
       # was no response the correct answer?!
       if str('feedbackResponse').lower() == 'none': responseFeedback6and7.corr = 1  # correct non-response
       else: responseFeedback6and7.corr = 0  # failed to respond (incorrectly)
    # store data for block7Loop (TrialHandler)
    block7Loop.addData('responseFeedback6and7.keys',responseFeedback6and7.keys)
    block7Loop.addData('responseFeedback6and7.corr', responseFeedback6and7.corr)
    if responseFeedback6and7.keys != None:  # we had a response
        block7Loop.addData('responseFeedback6and7.rt', responseFeedback6and7.rt)
    
    # the Routine "trialBlock6and7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'block7Loop'


# set up handler to look after randomisation of conditions etc
endLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Instructions.xlsx', selection='7'),
    seed=None, name='endLoop')
thisExp.addLoop(endLoop)  # add the loop to the experiment
thisEndLoop = endLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisEndLoop.rgb)
if thisEndLoop != None:
    for paramName in thisEndLoop.keys():
        exec(paramName + '= thisEndLoop.' + paramName)

for thisEndLoop in endLoop:
    currentLoop = endLoop
    # abbreviate parameter names if possible (e.g. rgb = thisEndLoop.rgb)
    if thisEndLoop != None:
        for paramName in thisEndLoop.keys():
            exec(paramName + '= thisEndLoop.' + paramName)
    
    #------Prepare to start Routine "end"-------
    t = 0
    endClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    endMessage.setText(instruction)
    endResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
    endResponse.status = NOT_STARTED
    # keep track of which components have finished
    endComponents = []
    endComponents.append(endMessage)
    endComponents.append(endResponse)
    for thisComponent in endComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "end"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = endClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endMessage* updates
        if t >= 0 and endMessage.status == NOT_STARTED:
            # keep track of start time/frame for later
            endMessage.tStart = t  # underestimates by a little under one frame
            endMessage.frameNStart = frameN  # exact frame index
            endMessage.setAutoDraw(True)
        
        # *endResponse* updates
        if t >= 0.0 and endResponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            endResponse.tStart = t  # underestimates by a little under one frame
            endResponse.frameNStart = frameN  # exact frame index
            endResponse.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if endResponse.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
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
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'endLoop'








win.close()
core.quit()

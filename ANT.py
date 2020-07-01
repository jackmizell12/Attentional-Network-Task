#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Fri May 29 13:18:57 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'ANT'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/cpaterson/Documents/ANT.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instr_1 = visual.TextStim(win=win, name='instr_1',
    text='This is a task investigating attention.\n\nYou will be shown an arrow on the screen pointing to either the \nleft or the right.\n\nOn some trials, the arrow will be flanked by\ntwo arrows to the left or two arrows to the \nright. They may or may not point in the same direction as the \nCENTER arrow.\n\n\n\n\n\n\n\n\nYour task is to respond to the direction of the CENTER arrow.\n\n\n\nPress the SPACEBAR to continue.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='ANT_images/image1.png', mask=None,
    ori=0, pos=(0, -.1), size=(0.5, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instr_2 = visual.TextStim(win=win, name='instr_2',
    text="left: 'E' key                                            right: 'I' key\n\nPress the left response button ('E') if the CENTER arrow \npoints to the left.\n\n\n\n\n\nPress the right reponse arrow ('I') if the CENTER arrow \npoints to the right.\n\n\n\n\n\nPlease make your reponse as quickly and accurately as \npossible. Your reaction time and accuracy will be recorded.\n\n\n\nPress the SPACEBAR to continue.",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
image_2_1 = visual.ImageStim(
    win=win,
    name='image_2_1', 
    image='ANT_images/image2.1.png', mask=None,
    ori=0, pos=(0, .14), size=(0.5, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_2_2 = visual.ImageStim(
    win=win,
    name='image_2_2', 
    image='ANT_images/image2.2.png', mask=None,
    ori=0, pos=(0, -.1), size=(0.5, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr3"
instr3Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='There will be a cross in the center of the screen \nand the arrows will appear either above or below the cross.\n\nYou should try to fixate on the cross throughout the task.\n\n\n\nPress the SPACEBAR to continue.',
    font='Arial',
    pos=(0, .3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='ANT_images/image3.png', mask=None,
    ori=0, pos=(0, -.07), size=(0.7, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instr4"
instr4Clock = core.Clock()
instr_4 = visual.TextStim(win=win, name='instr_4',
    text='Additionally, on some trials there will be a black star \nflashed onto the screen shortly before the arrows appear.\n\nThese stars indicate where the arrow will occur:\n\n\n\n\n\n\n\n\n\nIf the star is at the center or both above and below fixation \nit indicates both that the trial will occur shortly and WHERE \nit will occur.\n\nTry to maintain fixation at all times. However, you may attend \nwhen and where indicated by the cues.\n\n\n\nPress the SPACEBAR to continue.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='ANT_images/image4.png', mask=None,
    ori=0, pos=(0, .1), size=(0.6, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "practice_instr"
practice_instrClock = core.Clock()
key_resp_5 = keyboard.Keyboard()
pract_instr = visual.TextStim(win=win, name='pract_instr',
    text="This task contains four blocks:\n\nThe first block is for practice only and takes about two minutes. After each \nblock there will be a message 'take a break' and you may take a short rest.\n\nThe whole session takes about twenty minutes.\n\n\n\nPress the SPACEBAR to start PRACTICE",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "pract_trial"
pract_trialClock = core.Clock()
fix_1 = visual.ImageStim(
    win=win,
    name='fix_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pract_warning = visual.ImageStim(
    win=win,
    name='pract_warning', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
fix_2 = visual.ImageStim(
    win=win,
    name='fix_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
pract_target = visual.ImageStim(
    win=win,
    name='pract_target', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.7, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
pract_resp = keyboard.Keyboard()

# Initialize components for Routine "feedback_2"
feedback_2Clock = core.Clock()
msg = "error"
text_3 = visual.TextStim(win=win, name='text_3',
    text=msg,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial_instr"
trial_instrClock = core.Clock()
practice_res = visual.TextStim(win=win, name='practice_res',
    text='You have completed the practice trials.\n\nAccuracy:\nAverage response speed:\n\nNow the actual task can be started.\n\nThere will be three blocks. Each block takes about\nfive minutes. Totally, you just need to spend 15 minutes.\n\n\n\nPress the SPACEBAR to start the task ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
practice_accuracy = visual.TextStim(win=win, name='practice_accuracy',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
response_time = visual.TextStim(win=win, name='response_time',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation_1 = visual.ImageStim(
    win=win,
    name='fixation_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
warning = visual.ImageStim(
    win=win,
    name='warning', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
fixation_2 = visual.ImageStim(
    win=win,
    name='fixation_2', 
    image='ANT_images/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
target = visual.ImageStim(
    win=win,
    name='target', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.7, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
post_fixation = visual.ImageStim(
    win=win,
    name='post_fixation', 
    image='ANT_images/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response = keyboard.Keyboard()

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
break_message = visual.TextStim(win=win, name='break_message',
    text='You have reached the end of this trial. You may take a short break before continuing.\n\nPlease press the SPACEBAR when you are ready to proceed.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
break_key = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation_1 = visual.ImageStim(
    win=win,
    name='fixation_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
warning = visual.ImageStim(
    win=win,
    name='warning', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
fixation_2 = visual.ImageStim(
    win=win,
    name='fixation_2', 
    image='ANT_images/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
target = visual.ImageStim(
    win=win,
    name='target', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.7, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
post_fixation = visual.ImageStim(
    win=win,
    name='post_fixation', 
    image='ANT_images/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You have completed the test.\n\nThank you for participating.\n\nPress the SPACEBAR to exit.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instrComponents = [instr_1, key_resp, image]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_1* updates
    if instr_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instr_1.frameNStart = frameN  # exact frame index
        instr_1.tStart = t  # local t and not account for scr refresh
        instr_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_1, 'tStartRefresh')  # time at next scr refresh
        instr_1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_1.started', instr_1.tStartRefresh)
thisExp.addData('instr_1.stopped', instr_1.tStopRefresh)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instr2Components = [instr_2, key_resp_2, image_2_1, image_2_2]
for thisComponent in instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr2"-------
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_2* updates
    if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.tStart = t  # local t and not account for scr refresh
        instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
        instr_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_2_1* updates
    if image_2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2_1.frameNStart = frameN  # exact frame index
        image_2_1.tStart = t  # local t and not account for scr refresh
        image_2_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2_1, 'tStartRefresh')  # time at next scr refresh
        image_2_1.setAutoDraw(True)
    
    # *image_2_2* updates
    if image_2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2_2.frameNStart = frameN  # exact frame index
        image_2_2.tStart = t  # local t and not account for scr refresh
        image_2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2_2, 'tStartRefresh')  # time at next scr refresh
        image_2_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_2.started', instr_2.tStartRefresh)
thisExp.addData('instr_2.stopped', instr_2.tStopRefresh)
thisExp.addData('image_2_1.started', image_2_1.tStartRefresh)
thisExp.addData('image_2_1.stopped', image_2_1.tStopRefresh)
thisExp.addData('image_2_2.started', image_2_2.tStartRefresh)
thisExp.addData('image_2_2.stopped', image_2_2.tStopRefresh)
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instr3Components = [text, key_resp_3, image_3]
for thisComponent in instr3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr3"-------
while continueRoutine:
    # get current time
    t = instr3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr3"-------
for thisComponent in instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)
# the Routine "instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instr4Components = [instr_4, key_resp_4, image_4]
for thisComponent in instr4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr4"-------
while continueRoutine:
    # get current time
    t = instr4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_4* updates
    if instr_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_4.frameNStart = frameN  # exact frame index
        instr_4.tStart = t  # local t and not account for scr refresh
        instr_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_4, 'tStartRefresh')  # time at next scr refresh
        instr_4.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr4"-------
for thisComponent in instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_4.started', instr_4.tStartRefresh)
thisExp.addData('instr_4.stopped', instr_4.tStopRefresh)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)
# the Routine "instr4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
practice_instrComponents = [key_resp_5, pract_instr]
for thisComponent in practice_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_instr"-------
while continueRoutine:
    # get current time
    t = practice_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *pract_instr* updates
    if pract_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pract_instr.frameNStart = frameN  # exact frame index
        pract_instr.tStart = t  # local t and not account for scr refresh
        pract_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pract_instr, 'tStartRefresh')  # time at next scr refresh
        pract_instr.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_instr"-------
for thisComponent in practice_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('pract_instr.started', pract_instr.tStartRefresh)
thisExp.addData('pract_instr.stopped', pract_instr.tStopRefresh)
# the Routine "practice_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ANT_practice.xlsx'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pract_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    fix_1.setImage('ANT_images/fixation.png')
    pract_warning.setImage(cue_file)
    fix_2.setImage('ANT_images/fixation.png')
    pract_target.setPos((0, pos))
    pract_target.setImage(flanker)
    pract_resp.keys = []
    pract_resp.rt = []
    _pract_resp_allKeys = []
    # keep track of which components have finished
    pract_trialComponents = [fix_1, pract_warning, fix_2, pract_target, pract_resp]
    for thisComponent in pract_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pract_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pract_trial"-------
    while continueRoutine:
        # get current time
        t = pract_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pract_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_1* updates
        if fix_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_1.frameNStart = frameN  # exact frame index
            fix_1.tStart = t  # local t and not account for scr refresh
            fix_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_1, 'tStartRefresh')  # time at next scr refresh
            fix_1.setAutoDraw(True)
        if fix_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_1.tStartRefresh + fix1-frameTolerance:
                # keep track of stop time/frame for later
                fix_1.tStop = t  # not accounting for scr refresh
                fix_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_1, 'tStopRefresh')  # time at next scr refresh
                fix_1.setAutoDraw(False)
        
        # *pract_warning* updates
        if pract_warning.status == NOT_STARTED and tThisFlip >= fix1-frameTolerance:
            # keep track of start time/frame for later
            pract_warning.frameNStart = frameN  # exact frame index
            pract_warning.tStart = t  # local t and not account for scr refresh
            pract_warning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pract_warning, 'tStartRefresh')  # time at next scr refresh
            pract_warning.setAutoDraw(True)
        if pract_warning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pract_warning.tStartRefresh + cue_time-frameTolerance:
                # keep track of stop time/frame for later
                pract_warning.tStop = t  # not accounting for scr refresh
                pract_warning.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pract_warning, 'tStopRefresh')  # time at next scr refresh
                pract_warning.setAutoDraw(False)
        
        # *fix_2* updates
        if fix_2.status == NOT_STARTED and pract_warning.status==FINISHED:
            # keep track of start time/frame for later
            fix_2.frameNStart = frameN  # exact frame index
            fix_2.tStart = t  # local t and not account for scr refresh
            fix_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_2, 'tStartRefresh')  # time at next scr refresh
            fix_2.setAutoDraw(True)
        if fix_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_2.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                fix_2.tStop = t  # not accounting for scr refresh
                fix_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_2, 'tStopRefresh')  # time at next scr refresh
                fix_2.setAutoDraw(False)
        
        # *pract_target* updates
        if pract_target.status == NOT_STARTED and fix_2.status==FINISHED:
            # keep track of start time/frame for later
            pract_target.frameNStart = frameN  # exact frame index
            pract_target.tStart = t  # local t and not account for scr refresh
            pract_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pract_target, 'tStartRefresh')  # time at next scr refresh
            pract_target.setAutoDraw(True)
        if pract_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pract_target.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                pract_target.tStop = t  # not accounting for scr refresh
                pract_target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pract_target, 'tStopRefresh')  # time at next scr refresh
                pract_target.setAutoDraw(False)
        
        # *pract_resp* updates
        waitOnFlip = False
        if pract_resp.status == NOT_STARTED and tThisFlip >= fixation_2.status==FINISHED-frameTolerance:
            # keep track of start time/frame for later
            pract_resp.frameNStart = frameN  # exact frame index
            pract_resp.tStart = t  # local t and not account for scr refresh
            pract_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pract_resp, 'tStartRefresh')  # time at next scr refresh
            pract_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pract_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pract_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pract_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pract_resp.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                pract_resp.tStop = t  # not accounting for scr refresh
                pract_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pract_resp, 'tStopRefresh')  # time at next scr refresh
                pract_resp.status = FINISHED
        if pract_resp.status == STARTED and not waitOnFlip:
            theseKeys = pract_resp.getKeys(keyList=['e', 'i'], waitRelease=False)
            _pract_resp_allKeys.extend(theseKeys)
            if len(_pract_resp_allKeys):
                pract_resp.keys = _pract_resp_allKeys[0].name  # just the first key pressed
                pract_resp.rt = _pract_resp_allKeys[0].rt
                # was this correct?
                if (pract_resp.keys == str(correct)) or (pract_resp.keys == correct):
                    pract_resp.corr = 1
                else:
                    pract_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pract_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pract_trial"-------
    for thisComponent in pract_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('fix_1.started', fix_1.tStartRefresh)
    practice.addData('fix_1.stopped', fix_1.tStopRefresh)
    practice.addData('pract_warning.started', pract_warning.tStartRefresh)
    practice.addData('pract_warning.stopped', pract_warning.tStopRefresh)
    practice.addData('fix_2.started', fix_2.tStartRefresh)
    practice.addData('fix_2.stopped', fix_2.tStopRefresh)
    practice.addData('pract_target.started', pract_target.tStartRefresh)
    practice.addData('pract_target.stopped', pract_target.tStopRefresh)
    # check responses
    if pract_resp.keys in ['', [], None]:  # No response was made
        pract_resp.keys = None
        # was no response the correct answer?!
        if str(correct).lower() == 'none':
           pract_resp.corr = 1;  # correct non-response
        else:
           pract_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice (TrialHandler)
    practice.addData('pract_resp.keys',pract_resp.keys)
    practice.addData('pract_resp.corr', pract_resp.corr)
    if pract_resp.keys != None:  # we had a response
        practice.addData('pract_resp.rt', pract_resp.rt)
    practice.addData('pract_resp.started', pract_resp.tStartRefresh)
    practice.addData('pract_resp.stopped', pract_resp.tStopRefresh)
    # the Routine "pract_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback_2"-------
    continueRoutine = True
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    msg = "update"
    
    if not pract_resp.keys:
        msg="No response"
    elif pract_resp.corr:
        msg="Correct"
    else:
        msg="Incorrect"
    text_3.setColor('black', colorSpace='rgb')
    # keep track of which components have finished
    feedback_2Components = [text_3]
    for thisComponent in feedback_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback_2"-------
    for thisComponent in feedback_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('text_3.started', text_3.tStartRefresh)
    practice.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice'


# ------Prepare to start Routine "trial_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
trial_instrComponents = [practice_res, key_resp_6, practice_accuracy, response_time]
for thisComponent in trial_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_instr"-------
while continueRoutine:
    # get current time
    t = trial_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_res* updates
    if practice_res.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_res.frameNStart = frameN  # exact frame index
        practice_res.tStart = t  # local t and not account for scr refresh
        practice_res.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_res, 'tStartRefresh')  # time at next scr refresh
        practice_res.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *practice_accuracy* updates
    if practice_accuracy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_accuracy.frameNStart = frameN  # exact frame index
        practice_accuracy.tStart = t  # local t and not account for scr refresh
        practice_accuracy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_accuracy, 'tStartRefresh')  # time at next scr refresh
        practice_accuracy.setAutoDraw(True)
    
    # *response_time* updates
    if response_time.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response_time.frameNStart = frameN  # exact frame index
        response_time.tStart = t  # local t and not account for scr refresh
        response_time.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response_time, 'tStartRefresh')  # time at next scr refresh
        response_time.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_instr"-------
for thisComponent in trial_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice_res.started', practice_res.tStartRefresh)
thisExp.addData('practice_res.stopped', practice_res.tStopRefresh)
thisExp.addData('practice_accuracy.started', practice_accuracy.tStartRefresh)
thisExp.addData('practice_accuracy.stopped', practice_accuracy.tStopRefresh)
thisExp.addData('response_time.started', response_time.tStartRefresh)
thisExp.addData('response_time.stopped', response_time.tStopRefresh)
# the Routine "trial_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ANT_conditions.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        fixation_1.setImage('ANT_images/fixation.png')
        warning.setImage(cue_file)
        target.setPos((0, pos))
        target.setImage(flanker)
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        trialComponents = [fixation_1, warning, fixation_2, target, post_fixation, response]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_1* updates
            if fixation_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixation_1.frameNStart = frameN  # exact frame index
                fixation_1.tStart = t  # local t and not account for scr refresh
                fixation_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_1, 'tStartRefresh')  # time at next scr refresh
                fixation_1.setAutoDraw(True)
            if fixation_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_1.tStartRefresh + fix1-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_1.tStop = t  # not accounting for scr refresh
                    fixation_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_1, 'tStopRefresh')  # time at next scr refresh
                    fixation_1.setAutoDraw(False)
            
            # *warning* updates
            if warning.status == NOT_STARTED and tThisFlip >= fix1-frameTolerance:
                # keep track of start time/frame for later
                warning.frameNStart = frameN  # exact frame index
                warning.tStart = t  # local t and not account for scr refresh
                warning.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(warning, 'tStartRefresh')  # time at next scr refresh
                warning.setAutoDraw(True)
            if warning.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > warning.tStartRefresh + cue_time-frameTolerance:
                    # keep track of stop time/frame for later
                    warning.tStop = t  # not accounting for scr refresh
                    warning.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(warning, 'tStopRefresh')  # time at next scr refresh
                    warning.setAutoDraw(False)
            
            # *fixation_2* updates
            if fixation_2.status == NOT_STARTED and warning.status==FINISHED:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(True)
            if fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_2.tStartRefresh + .4-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
                    fixation_2.setAutoDraw(False)
            
            # *target* updates
            if target.status == NOT_STARTED and fixation_2.status==FINISHED:
                # keep track of start time/frame for later
                target.frameNStart = frameN  # exact frame index
                target.tStart = t  # local t and not account for scr refresh
                target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
                target.setAutoDraw(True)
            if target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    target.tStop = t  # not accounting for scr refresh
                    target.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                    target.setAutoDraw(False)
            
            # *post_fixation* updates
            if post_fixation.status == NOT_STARTED and target.status==FINISHED:
                # keep track of start time/frame for later
                post_fixation.frameNStart = frameN  # exact frame index
                post_fixation.tStart = t  # local t and not account for scr refresh
                post_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(post_fixation, 'tStartRefresh')  # time at next scr refresh
                post_fixation.setAutoDraw(True)
            if post_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > post_fixation.tStartRefresh + x-frameTolerance:
                    # keep track of stop time/frame for later
                    post_fixation.tStop = t  # not accounting for scr refresh
                    post_fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(post_fixation, 'tStopRefresh')  # time at next scr refresh
                    post_fixation.setAutoDraw(False)
            
            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and fixation_2.status==FINISHED:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    response.tStop = t  # not accounting for scr refresh
                    response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response, 'tStopRefresh')  # time at next scr refresh
                    response.status = FINISHED
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['e', 'i'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[0].name  # just the first key pressed
                    response.rt = _response_allKeys[0].rt
                    # was this correct?
                    if (response.keys == str(correct)) or (response.keys == correct):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            timer = core.Clock()
            rt = timer.getTime()
            x = (3.5 - fix1 - rt)
            timer.reset()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('fixation_1.started', fixation_1.tStartRefresh)
        trials.addData('fixation_1.stopped', fixation_1.tStopRefresh)
        trials.addData('warning.started', warning.tStartRefresh)
        trials.addData('warning.stopped', warning.tStopRefresh)
        trials.addData('fixation_2.started', fixation_2.tStartRefresh)
        trials.addData('fixation_2.stopped', fixation_2.tStopRefresh)
        trials.addData('target.started', target.tStartRefresh)
        trials.addData('target.stopped', target.tStopRefresh)
        trials.addData('post_fixation.started', post_fixation.tStartRefresh)
        trials.addData('post_fixation.stopped', post_fixation.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('response.keys',response.keys)
        trials.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            trials.addData('response.rt', response.rt)
        trials.addData('response.started', response.tStartRefresh)
        trials.addData('response.stopped', response.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2 repeats of 'trials'
    
    
    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    break_key.keys = []
    break_key.rt = []
    _break_key_allKeys = []
    # keep track of which components have finished
    break_2Components = [break_message, break_key]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "break_2"-------
    while continueRoutine:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_message* updates
        if break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_message.frameNStart = frameN  # exact frame index
            break_message.tStart = t  # local t and not account for scr refresh
            break_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_message, 'tStartRefresh')  # time at next scr refresh
            break_message.setAutoDraw(True)
        
        # *break_key* updates
        waitOnFlip = False
        if break_key.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            break_key.frameNStart = frameN  # exact frame index
            break_key.tStart = t  # local t and not account for scr refresh
            break_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_key, 'tStartRefresh')  # time at next scr refresh
            break_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(break_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(break_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if break_key.status == STARTED and not waitOnFlip:
            theseKeys = break_key.getKeys(keyList=['space'], waitRelease=False)
            _break_key_allKeys.extend(theseKeys)
            if len(_break_key_allKeys):
                break_key.keys = _break_key_allKeys[-1].name  # just the last key pressed
                break_key.rt = _break_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('break_message.started', break_message.tStartRefresh)
    trials_2.addData('break_message.stopped', break_message.tStopRefresh)
    # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ANT_conditions.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    fixation_1.setImage('ANT_images/fixation.png')
    warning.setImage(cue_file)
    target.setPos((0, pos))
    target.setImage(flanker)
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation_1, warning, fixation_2, target, post_fixation, response]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_1* updates
        if fixation_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation_1.frameNStart = frameN  # exact frame index
            fixation_1.tStart = t  # local t and not account for scr refresh
            fixation_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_1, 'tStartRefresh')  # time at next scr refresh
            fixation_1.setAutoDraw(True)
        if fixation_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_1.tStartRefresh + fix1-frameTolerance:
                # keep track of stop time/frame for later
                fixation_1.tStop = t  # not accounting for scr refresh
                fixation_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_1, 'tStopRefresh')  # time at next scr refresh
                fixation_1.setAutoDraw(False)
        
        # *warning* updates
        if warning.status == NOT_STARTED and tThisFlip >= fix1-frameTolerance:
            # keep track of start time/frame for later
            warning.frameNStart = frameN  # exact frame index
            warning.tStart = t  # local t and not account for scr refresh
            warning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(warning, 'tStartRefresh')  # time at next scr refresh
            warning.setAutoDraw(True)
        if warning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > warning.tStartRefresh + cue_time-frameTolerance:
                # keep track of stop time/frame for later
                warning.tStop = t  # not accounting for scr refresh
                warning.frameNStop = frameN  # exact frame index
                win.timeOnFlip(warning, 'tStopRefresh')  # time at next scr refresh
                warning.setAutoDraw(False)
        
        # *fixation_2* updates
        if fixation_2.status == NOT_STARTED and warning.status==FINISHED:
            # keep track of start time/frame for later
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.tStart = t  # local t and not account for scr refresh
            fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(True)
        if fixation_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_2.tStartRefresh + .4-frameTolerance:
                # keep track of stop time/frame for later
                fixation_2.tStop = t  # not accounting for scr refresh
                fixation_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(False)
        
        # *target* updates
        if target.status == NOT_STARTED and fixation_2.status==FINISHED:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
        
        # *post_fixation* updates
        if post_fixation.status == NOT_STARTED and target.status==FINISHED:
            # keep track of start time/frame for later
            post_fixation.frameNStart = frameN  # exact frame index
            post_fixation.tStart = t  # local t and not account for scr refresh
            post_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(post_fixation, 'tStartRefresh')  # time at next scr refresh
            post_fixation.setAutoDraw(True)
        if post_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > post_fixation.tStartRefresh + x-frameTolerance:
                # keep track of stop time/frame for later
                post_fixation.tStop = t  # not accounting for scr refresh
                post_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(post_fixation, 'tStopRefresh')  # time at next scr refresh
                post_fixation.setAutoDraw(False)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and fixation_2.status==FINISHED:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                response.tStop = t  # not accounting for scr refresh
                response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(response, 'tStopRefresh')  # time at next scr refresh
                response.status = FINISHED
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['e', 'i'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[0].name  # just the first key pressed
                response.rt = _response_allKeys[0].rt
                # was this correct?
                if (response.keys == str(correct)) or (response.keys == correct):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        timer = core.Clock()
        rt = timer.getTime()
        x = (3.5 - fix1 - rt)
        timer.reset()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('fixation_1.started', fixation_1.tStartRefresh)
    trials_3.addData('fixation_1.stopped', fixation_1.tStopRefresh)
    trials_3.addData('warning.started', warning.tStartRefresh)
    trials_3.addData('warning.stopped', warning.tStopRefresh)
    trials_3.addData('fixation_2.started', fixation_2.tStartRefresh)
    trials_3.addData('fixation_2.stopped', fixation_2.tStopRefresh)
    trials_3.addData('target.started', target.tStartRefresh)
    trials_3.addData('target.stopped', target.tStopRefresh)
    trials_3.addData('post_fixation.started', post_fixation.tStartRefresh)
    trials_3.addData('post_fixation.stopped', post_fixation.tStopRefresh)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str(correct).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('response.keys',response.keys)
    trials_3.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        trials_3.addData('response.rt', response.rt)
    trials_3.addData('response.started', response.tStartRefresh)
    trials_3.addData('response.stopped', response.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials_3'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
end_key.keys = []
end_key.rt = []
_end_key_allKeys = []
# keep track of which components have finished
endComponents = [text_2, end_key]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *end_key* updates
    waitOnFlip = False
    if end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key.frameNStart = frameN  # exact frame index
        end_key.tStart = t  # local t and not account for scr refresh
        end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key, 'tStartRefresh')  # time at next scr refresh
        end_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key.status == STARTED and not waitOnFlip:
        theseKeys = end_key.getKeys(keyList=['space'], waitRelease=False)
        _end_key_allKeys.extend(theseKeys)
        if len(_end_key_allKeys):
            end_key.keys = _end_key_allKeys[-1].name  # just the last key pressed
            end_key.rt = _end_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

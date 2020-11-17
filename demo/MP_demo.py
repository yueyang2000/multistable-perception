#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Sat Jul 11 19:42:22 2020
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
expName = 'MP_demo'  # from the Builder filename that created this script
expInfo = {'participant': ''}
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
    originPath='/Users/yueyang/yiqunyang/SRT_认知/实验程序/multistable-perception/MP_demo.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
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

# Initialize components for Routine "title"
titleClock = core.Clock()
text_title = visual.TextStim(win=win, name='text_title',
    text='Multistable Perception',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import csv

# open a csv file

headers = ['id','type','name','rt','duration']

f = open(filename+'.csv','w')
f_csv = csv.writer(f)
f_csv.writerow(headers)

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='RS1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "sphere1"
sphere1Clock = core.Clock()
movie = visual.MovieStim3(
    win=win, name='movie',
    noAudio = True,
    filename='revolving_sphere.gif',
    ori=0, pos=(0, 0), opacity=1,
    loop=True,
    size=(400,400),
    depth=0.0,
    )

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='RS2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "sphere2"
sphere2Clock = core.Clock()
movie_2 = visual.MovieStim3(
    win=win, name='movie_2',
    noAudio = False,
    filename='revolving_sphere.gif',
    ori=90, pos=(0, 0), opacity=1,
    loop=True,
    size=(400,400),
    depth=0.0,
    )

# Initialize components for Routine "instr3"
instr3Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='QD',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "square"
squareClock = core.Clock()
square1 = visual.Rect(
    win=win, name='square1',
    width=[0.1, 0.1][0], height=[0.1, 0.1][1],
    ori=0, pos=[-0.2,-0.2],
    lineWidth=1, lineColor=[255,255,255], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)
square2 = visual.Rect(
    win=win, name='square2',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.2, 0.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
square3 = visual.Rect(
    win=win, name='square3',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.2, 0.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
square4 = visual.Rect(
    win=win, name='square4',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.2, -0.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
# This code will run before the experiment starts, after the window is opened and your other components are initialised but before the experiment timer starts



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "title"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
titleComponents = [text_title]
for thisComponent in titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_title* updates
    if text_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_title.frameNStart = frameN  # exact frame index
        text_title.tStart = t  # local t and not account for scr refresh
        text_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_title, 'tStartRefresh')  # time at next scr refresh
        text_title.setAutoDraw(True)
    if text_title.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_title.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_title.tStop = t  # not accounting for scr refresh
            text_title.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_title, 'tStopRefresh')  # time at next scr refresh
            text_title.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "title"-------
for thisComponent in titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_title.started', text_title.tStartRefresh)
thisExp.addData('text_title.stopped', text_title.tStopRefresh)

# ------Prepare to start Routine "instr1"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
instr1Components = [text]
for thisComponent in instr1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instr1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr1Clock)
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
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# ------Prepare to start Routine "sphere1"-------
continueRoutine = True
routineTimer.add(30.000000)
# update component parameters for each repeat
defaultKeyboard.clock.reset()

# keep track of which components have finished
sphere1Components = [movie]
for thisComponent in sphere1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sphere1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sphere1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = sphere1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sphere1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie* updates
    if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        movie.setAutoDraw(True)
    if movie.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > movie.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            movie.tStop = t  # not accounting for scr refresh
            movie.frameNStop = frameN  # exact frame index
            win.timeOnFlip(movie, 'tStopRefresh')  # time at next scr refresh
            movie.setAutoDraw(False)
    
    keys = defaultKeyboard.getKeys(['m','n'],waitRelease=True)
    for key in keys:
        # id, type, name, rt, duration
        row = [1, 'sphere1',key.name,key.rt,key.duration]
        f_csv.writerow(row)
        # print(key.name,key.rt,key.duration)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sphere1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sphere1"-------
for thisComponent in sphere1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('movie.started', movie.tStartRefresh)
thisExp.addData('movie.stopped', movie.tStopRefresh)

# ------Prepare to start Routine "instr2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
instr2Components = [text_3]
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
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
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
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# ------Prepare to start Routine "sphere2"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
sphere2Components = [movie_2]
for thisComponent in sphere2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sphere2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sphere2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = sphere2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sphere2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie_2* updates
    if movie_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_2.frameNStart = frameN  # exact frame index
        movie_2.tStart = t  # local t and not account for scr refresh
        movie_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_2, 'tStartRefresh')  # time at next scr refresh
        movie_2.setAutoDraw(True)
    if movie_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > movie_2.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            movie_2.tStop = t  # not accounting for scr refresh
            movie_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(movie_2, 'tStopRefresh')  # time at next scr refresh
            movie_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sphere2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sphere2"-------
for thisComponent in sphere2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('movie_2.started', movie_2.tStartRefresh)
thisExp.addData('movie_2.stopped', movie_2.tStopRefresh)

# ------Prepare to start Routine "instr3"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
instr3Components = [text_4]
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
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instr3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
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
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# ------Prepare to start Routine "square"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# This code will run at the start of the routine containing this component, after starting the necessary timers but before loading components

cnt = 0
s1 = 1
s2 = 1
s3 = 0
s4 = 0
# keep track of which components have finished
squareComponents = [square1, square2, square3, square4]
for thisComponent in squareComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
squareClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "square"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = squareClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=squareClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *square1* updates
    if square1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        square1.frameNStart = frameN  # exact frame index
        square1.tStart = t  # local t and not account for scr refresh
        square1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(square1, 'tStartRefresh')  # time at next scr refresh
        square1.setAutoDraw(True)
    if square1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > square1.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            square1.tStop = t  # not accounting for scr refresh
            square1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(square1, 'tStopRefresh')  # time at next scr refresh
            square1.setAutoDraw(False)
    if square1.status == STARTED:  # only update if drawing
        square1.setOpacity(s1, log=False)
    
    # *square2* updates
    if square2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        square2.frameNStart = frameN  # exact frame index
        square2.tStart = t  # local t and not account for scr refresh
        square2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(square2, 'tStartRefresh')  # time at next scr refresh
        square2.setAutoDraw(True)
    if square2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > square2.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            square2.tStop = t  # not accounting for scr refresh
            square2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(square2, 'tStopRefresh')  # time at next scr refresh
            square2.setAutoDraw(False)
    if square2.status == STARTED:  # only update if drawing
        square2.setOpacity(s2, log=False)
    
    # *square3* updates
    if square3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        square3.frameNStart = frameN  # exact frame index
        square3.tStart = t  # local t and not account for scr refresh
        square3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(square3, 'tStartRefresh')  # time at next scr refresh
        square3.setAutoDraw(True)
    if square3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > square3.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            square3.tStop = t  # not accounting for scr refresh
            square3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(square3, 'tStopRefresh')  # time at next scr refresh
            square3.setAutoDraw(False)
    if square3.status == STARTED:  # only update if drawing
        square3.setOpacity(s3, log=False)
    
    # *square4* updates
    if square4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        square4.frameNStart = frameN  # exact frame index
        square4.tStart = t  # local t and not account for scr refresh
        square4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(square4, 'tStartRefresh')  # time at next scr refresh
        square4.setAutoDraw(True)
    if square4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > square4.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            square4.tStop = t  # not accounting for scr refresh
            square4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(square4, 'tStopRefresh')  # time at next scr refresh
            square4.setAutoDraw(False)
    if square4.status == STARTED:  # only update if drawing
        square4.setOpacity(s4, log=False)
    # This code will run on each frame refresh during the routine containing this component, after iterating the frame but before the screen flip
    
    cnt += 1
    
    if cnt%30==0:
        s1 = 1-s1
        s2 = 1-s2
        s3 = 1-s3
        s4 = 1-s4
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in squareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "square"-------
for thisComponent in squareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('square1.started', square1.tStartRefresh)
thisExp.addData('square1.stopped', square1.tStopRefresh)
thisExp.addData('square2.started', square2.tStartRefresh)
thisExp.addData('square2.stopped', square2.tStopRefresh)
thisExp.addData('square3.started', square3.tStartRefresh)
thisExp.addData('square3.stopped', square3.tStopRefresh)
thisExp.addData('square4.started', square4.tStartRefresh)
thisExp.addData('square4.stopped', square4.tStopRefresh)
# This code will run at the end of the routine containing this component, after breaking the frame loop but before resetting the timer


f.close()
# This code will run at the end of the experiment, just before saving the data and closing the window



# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

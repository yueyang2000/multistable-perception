
from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os
import sys
import csv
from psychopy.hardware import keyboard

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# info dialog
expName = 'MP' 
expInfo = {'participant': '', 'session': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName

# dataFileName
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])


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

# open a csv file
headers = ['id','type','name','rt','duration']
f = open(filename+'.csv','w')
f_csv = csv.writer(f)
f_csv.writerow(headers)

# components
text_stim = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

RS1 = visual.MovieStim3(
    win=win, name='RS1',
    noAudio = True,
    filename='revolving_sphere.gif',
    ori=0, pos=(0, 0), opacity=1,
    loop=True,
    size=(400,400),
    depth=0.0,
    )

RS2 = visual.MovieStim3(
    win=win, name='RS2',
    noAudio = False,
    filename='revolving_sphere.gif',
    ori=90, pos=(0, 0), opacity=1,
    loop=True,
    size=(400,400),
    depth=0.0,
    )

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
clk = core.Clock() # clock for each routine
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


# before and after each routine
def init_routine(components):
    for thisComponent in components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
def end_routine(components):
    for thisComponent in components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


def show_text(text, time=1.0):
    '''
    show a piece of text
    '''
    continueRoutine = True
    routineTimer.add(time)
    text_stim.setText(text)
    
    components = [text_stim]
    init_routine(components)
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    clk.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = clk.getTime()
        tThisFlip = win.getFutureFlipTime(clock=clk)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if text_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_stim.frameNStart = frameN  # exact frame index
            text_stim.tStart = t  # local t and not account for scr refresh
            text_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_stim, 'tStartRefresh')  # time at next scr refresh
            text_stim.setAutoDraw(True)
        if text_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_stim.tStartRefresh + time -frameTolerance:
                # keep track of stop time/frame for later
                text_stim.tStop = t  # not accounting for scr refresh
                text_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_stim, 'tStopRefresh')  # time at next scr refresh
                text_stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False  # will revert to True if at least one component still running
        
        for thisComponent in components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  
                
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    end_routine(components)


def show_RS(movie, time=30.0, id=1):
    '''
    show RS stimuli
    '''
    continueRoutine = True
    routineTimer.add(time)
    # update component parameters for each repeat
    defaultKeyboard.clock.reset()

    # keep track of which components have finished
    components = [movie]
    init_routine(components)
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    clk.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = clk.getTime()
        tThisFlip = win.getFutureFlipTime(clock=clk)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            movie.frameNStart = frameN  # exact frame index
            movie.tStart = t  # local t and not account for scr refresh
            movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
            movie.setAutoDraw(True)
        if movie.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > movie.tStartRefresh + time -frameTolerance:
                # keep track of stop time/frame for later
                movie.tStop = t  # not accounting for scr refresh
                movie.frameNStop = frameN  # exact frame index
                win.timeOnFlip(movie, 'tStopRefresh')  # time at next scr refresh
                movie.setAutoDraw(False)
        
        # key monitor
        keys = defaultKeyboard.getKeys(['m','n'],waitRelease=True)
        for key in keys:
            # id, type, name, rt, duration
            row = [id, movie.name ,key.name,key.rt,key.duration]
            f_csv.writerow(row)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            
    end_routine(components)


def show_QD(time=30.0, freq=30, id=1):
    '''
    show QD stimuli
    '''
    continueRoutine = True
    routineTimer.add(time)
    # visibility of each square
    cnt = 0
    s1 = 1
    s2 = 1
    s3 = 0
    s4 = 0
    
    # keep track of which components have finished
    components = [square1, square2, square3, square4]
    init_routine(components)
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    clk.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = clk.getTime()
        tThisFlip = win.getFutureFlipTime(clock=clk)
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
            if tThisFlipGlobal > square1.tStartRefresh + time -frameTolerance:
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
            if tThisFlipGlobal > square2.tStartRefresh + time -frameTolerance:
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
            if tThisFlipGlobal > square3.tStartRefresh + time -frameTolerance:
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
            if tThisFlipGlobal > square4.tStartRefresh + time-frameTolerance:
                # keep track of stop time/frame for later
                square4.tStop = t  # not accounting for scr refresh
                square4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(square4, 'tStopRefresh')  # time at next scr refresh
                square4.setAutoDraw(False)
        if square4.status == STARTED:  # only update if drawing
            square4.setOpacity(s4, log=False)
        # This code will run on each frame refresh during the routine containing this component, after iterating the frame but before the screen flip
        
        # update visibility
        cnt += 1
        if cnt % freq ==0:
            s1 = 1-s1
            s2 = 1-s2
            s3 = 1-s3
            s4 = 1-s4
        
        # key monitor
        keys = defaultKeyboard.getKeys(['m','n'],waitRelease=True)
        for key in keys:
            # id, type, name, rt, duration
            row = [id, 'QD',key.name,key.rt,key.duration]
            f_csv.writerow(row)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have 
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    end_routine(components)


def run_trial(type, id):
    '''
    run a single trial
    '''
    if type == 'RS1':
        show_text('RS1 instruction', time=1.0)
        show_text('prepare', time=1.0)
        show_RS(RS1, time=30.0, id=id)
    elif type == 'RS2':
        show_text('RS2 instruction', time=1.0)
        show_text('prepare', time=1.0)
        show_RS(RS2, time=30.0,id=id)   
    elif type == 'QD':
        show_text('QD instruction', time=1.0)
        show_text('prepare', time=1.0)
        show_QD(time=30.0,id=id)
    
    show_text('rest', time = 25.0) # rest for 25s


# example: a single block
show_text('Multistable Perception', time=3.0)
for i in range(9):
    run_trial('QD', id=i)


# after experiment
f.close()
win.flip()
win.close()
core.quit()

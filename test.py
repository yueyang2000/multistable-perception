
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.hardware import keyboard
win = visual.Window(
    size=(800, 600), fullscr=False, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
    
routineTimer = core.CountdownTimer()
routineTimer.add(10.000000)
kb = keyboard.Keyboard()
kb.clock.reset()
while routineTimer.getTime() > 0:
    keys = kb.getKeys(None, waitRelease=True)
    for key in keys:
        print(key.name, key.rt, key.duration)

win.close()
core.quit()
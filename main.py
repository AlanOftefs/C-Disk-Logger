import tkinter
from tkinter import simpledialog
import threading
import timer as ti
import keyListener
import writer
import logInfo
import spaceDetector
import timer
import datetime

logInfo = logInfo.LogInfo()

writer = writer.Writer(logInfo)
timer = timer.Timer(1)
kL = keyListener.KeyListener()

kL.start()
timer.start()
log = ""
while True:
    tk = tkinter.Tk()
    tk.withdraw()
    while True:
        if timer.clock >= 1:
            
            logInfo.datetime = "%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            logInfo.cSpace = round(spaceDetector.GetDiskInfo() / 1024 / 1024 / 1024 * 100) / 100
            logInfo.logContent = log
            writer.Write()
            log = ""
            timer.clock = 0 # -> timer.Reset()
        if kL.keyFlag == True:
            log = simpledialog.askstring(title = "Log", prompt = "Content: ")
            kL.keyFlag = False
    tk.mainloop()


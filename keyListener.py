from pynput.keyboard import Listener, Key
import threading

class KeyListener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.keyFlag = False
    def OnPress(self, key):        
        try:
            if key.char == 'p':
                self.keyFlag = True
            else:
                self.keyFlag = False
        except:
            self.keyFlag = False
    def run(self):        
        with Listener(on_press = self.OnPress) as listener:            
            listener.join()     

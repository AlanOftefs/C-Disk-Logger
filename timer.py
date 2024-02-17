import time
import threading as thr
class Timer(thr.Thread):
    def __init__(self, interval):
        thr.Thread.__init__(self)
        self.clock = 0
        self.interval = interval
    def run(self):
        while True:
            time.sleep(self.interval)
            self.clock += 1

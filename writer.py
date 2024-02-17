import threading as thr
import timer
import logInfo
class Writer():
    def __init__(self, logInfo : logInfo.LogInfo):
        self.logInfo = logInfo
    def Write(self):
        with open("log.txt", "a+", encoding = "utf-8") as log:
            log.write(self.logInfo.datetime)
            log.write(" : ")
            log.write("\n")
            log.write(str(self.logInfo.cSpace) + "GB")
            log.write("\n")
            log.write(self.logInfo.logContent)
            log.write("\n")
            log.write("\n")
            log.close()
#a = logInfo.LogInfo(15, "hello")
#writer = Writer(a, 1)
#writer.start()


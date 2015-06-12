#coding=utf-8
'''
Created on 20150612
@author: Jiademing   iesool@163.com 
'''
import time;

class Shutdown:
    def __init__(self):
        print time.strftime("%Y-%m-%d %A %X", time.localtime())
    def Shutdownnow(self):
        pass
    def Delayshutdown(self, seconds):
        pass
    def Fixedtimeshutdown(self, times):
        pass
    def Rebootnow(self):
        pass
    def Delayreboot(self, seconds):
        pass
    def Fixedtimesreboot(self, times):
        pass
    def Cancel(self):
        pass
    def __del__(self):
        pass
    
if __name__ == "__main__":
    S = Shutdown()
    S.Shutdownnow()
    
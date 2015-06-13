#coding=utf-8
'''
Created on 20150612
@author: Jiademing   iesool@126.com 
'''
import time;
import os;
import sys;
import io;

class Shutdown:
    def __init__(self):
        print time.strftime("%Y-%m-%d %A %X", time.localtime())
    def Shutdownnow(self):
        ret = self.Delayshutdown(00)
        return ret
    
    def Delayshutdown(self, seconds):
        if seconds < 0:
            print "Delay time should >= 0 !"
            return False
        try:
            os.system("shutdown -s -t " + str(seconds))
        except:
            print("Opreation System error in Delayshutdown()")
        if seconds == 0 :
            print "You are poweroff the PC NOW!!"
        else:
            print "You will poweroff the PC aflter " + str(seconds) + " seconds.."
        return True
    def Fixedtimeshutdown(self, times):
        data = times;
        data = data.split(':')
        if len(data) != 2:
            print "times format error, like hour:minu!"
            return False
        if int(data[0]) > 24 or int(data[0]) < 0 :
            print "times format error, hour should in 00--->24!"
            return False
        if int(data[1]) >= 60 or int(data[1]) < 0:
            print "times format error, minu should in 00--->60!"
            return False
        try:
            os.system("at "+times+" shutdown -s")
        except :
            print("Opreation System error in Fixedtimeshutdown()")
            return False
        print "You plan to shutdown the PC at " + times
        return True
    
    def Rebootnow(self):
        return self.Delayreboot(00)

    def Delayreboot(self, seconds):
        if seconds < 0:
            print "Delay time should >= 0 !"
            return False
        try:
            os.system("shutdown -r -t " + str(seconds))
        except:
            print("Opreation System error in Delayreboot()")
        if seconds == 0 :
            print "You are rebooting the PC NOW!!"
        else:
            print "You will reboot the PC aflter " + str(seconds) + " seconds.."
        return True
    
    def Fixedtimesreboot(self, times):
        data = times;
        data = data.split(':')
        if len(data) != 2:
            print "times format error, like hour:minu!"
            return False
        if int(data[0]) > 24 or int(data[0]) < 0 :
            print "times format error, hour should in 00--->24!"
            return False
        if int(data[1]) >= 60 or int(data[1]) < 0:
            print "times format error, minu should in 00--->60!"
            return False
        try:
            os.system("at "+times+" shutdown -r")
        except :
            print("Opreation System error in Fixedtimeshutdown()")
            return False
        print "You plan to reboot the PC at " + times
        return True
    
    def Cancel(self):

        try:
            os.system("shutdown -a")
        except:
            print("Maybe Opration System error in Cancell()")
            return False
        print "Your shutdown plan have be cancel...."
        return True
    def __del__(self):
        pass
    
#Only test       
if __name__ == "__main__":
    S = Shutdown()
#   S.Shutdownnow()
    
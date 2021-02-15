
# importing time module 
import time 

def fileName():
    obj = time.localtime() 
    today = str(obj.tm_year)+'-'+str(obj.tm_mon)+'-'+str(obj.tm_mday)+'-'+str(obj.tm_hour)+'-'+str(obj.tm_min)+'-'+str(obj.tm_sec)+".csv"
    return today

def timeStamp():
    obj = time.localtime() 
    today = str(obj.tm_hour)+':'+str(obj.tm_min)+':'+str(obj.tm_sec)
    return today
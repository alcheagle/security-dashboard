from django.db import models
from scanner import scanner
import threading, datetime

class timed_scan:
    def __init__(tm):
        self.timer=tm

    def set_scan(tm, scn_type, domains): #import threading
        threading.Timer(self.timer, set_scan, args=[tm, scn_type, domains]).start()#Create new thread avery timer seconds
        scanner.scan(scn_type, domains)
        save_metrics()

    # def set_scan(tm, scn_type, domains): #TODO import time
        # while(true):
        #     time.sleep(tm); #tm is in seconds
        #     scanner.scan(scn_type, domains)

    # def save_metrics():
    #     year=datetime.now().year
    #     month=datetime.now().month
    #     day=datetime.now().day
    #     hour=datetime.now().hour
    #     up_date=datetime(year, month, day, hour, minute, second)

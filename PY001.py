from datetime import datetime
import time
import random
even = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 32, 
        34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]
for i in range (10):
    now_min = datetime.today().minute
    if now_min in even:
        print("its an even minute")
    else:
        print("its an odd minute")    
    wait_time = random.randint(1, 60) 
    time.sleep(wait_time)

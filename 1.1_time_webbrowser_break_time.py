# Repeat these steps 3 times:
# (1) wait for 2 hours
# (2) open browsers

import time
import webbrowser

print('This program started on',time.ctime())
# print the current time on the computer

total_breaks = 3
break_count = 0
while (break_count < total_breaks):
    # suspend the program for a given number of seconds
    time.sleep(10) # 2hrs here
    # then open a web browser
    url = "https://www.baidu.com/"
    webbrowser.open(url)
    break_count = break_count + 1

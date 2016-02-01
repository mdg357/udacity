#!/c/Python27/python
import webbrowser
import time
import sys

sleep_time = 10
break_count = 0
total_breaks = 3

print "Program started on {0}".format(time.ctime())
sys.stdout.flush()

while(break_count < total_breaks):
    time.sleep(sleep_time)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count += 1
    print "Take a break ({0} of {1})".format(break_count, total_breaks)

# Time to Stream - www.ilbak.it

# A simple timer that creates a text file to link to your stream software to automatically generate a countdown to the stream start.

import time
  
def streamtimer(t):
    t = t * 60
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        f = open("timetostream.txt", "w")
        f.write(timer)
        f.close()
        time.sleep(1)
        t -= 1
      
    print('Ready')
  
# input time
t = input("Enter the time in minutes: ")
  
# call
streamtimer(int(t))

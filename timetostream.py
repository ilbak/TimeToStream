# Time to Stream - www.ilbak.it

# A simple timer that creates a text file to link to your stream software to automatically generate a countdown to the stream start.

# For OBS: "Sources" > "Add" > "Text" > Enable "Read from file" > Browse "Text File" to timetostream.txt in TimeToStream.py path

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
    f = open("timetostream.txt", "w")
    f.write("")
    f.close()
    
# input time
t = input("How many minutes before the broadcast starts? ")
  
# call
streamtimer(int(t))

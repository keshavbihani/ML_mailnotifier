from classifier import *
import time
starttime=time.time()
"""
regular triggering of 60 seconds send to my mail box to check
for any latest mail got updated. If yes it check for that in the classifier and based on that it notify
"""
while True:

  print("start")

  #mail_msg = getmailbody()

  flag=checkforspam()

  time.sleep(60.0 - ((time.time() - starttime) % 60.0))

  print("end")

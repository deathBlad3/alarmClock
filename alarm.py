import argparse
import datetime
import time
from random import randint
import webbrowser

parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-H', '--hour', help='Hour', action='store', dest='hour', type=int, required=True)
requiredNamed.add_argument('-M','--minute', help='Minute', action='store', dest='minute', type=int, required=True)
requiredNamed.add_argument('-t', help='AM/PM', action='store', dest='ap', required=True)
args = parser.parse_args()

#Waits the specified amount of seconds and plays a random video on YouTube
def playVideo(secondsNeeded):
    print "Alarm Set"
    time.sleep(secondsNeeded)
    links = 'links.txt'
    with open(links) as f:
        linksList = f.read().splitlines()
    id = randint(0,len(linksList)-1)
    webbrowser.open(linksList[id])
    
now = datetime.datetime.now()
if args.ap=='PM':
    args.hour+=12
neededTime = now.replace(hour=args.hour,minute=args.minute,second=0,microsecond=0)
if now > neededTime:
    print "Its over man!"
else:
    secondsNeeded = int((neededTime-now).total_seconds())
    playVideo(secondsNeeded)
    

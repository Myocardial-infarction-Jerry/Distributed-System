from time import sleep
from sys import stdout

count = 0
id = '21307289'

while True:
    print('%04d -> %s' % (count, id))
    count += 1
    sleep(1)
    stdout.flush()

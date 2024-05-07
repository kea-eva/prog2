# daemon thread running in the background
from time import sleep
from random import random
from threading import Thread

# Background process
def data_in_background():
    global data
    # update state of data
    status_update = data
    while True:
        # check for change
        if data != status_update:
            # report the change
            print(f'Monitor: data has changed to {data}')
            # update status data
            status_update = data
        # let it wait
        sleep(0.1)
 
# global variable of data
data =  0
# create the daemon thread and start() it
daemon = Thread(target=data_in_background, daemon=True, name='Monitor')
daemon.start()
print('Daemon process in background --------------------***')

for i in range(10):
    value = random() * 0.5
    # wait
    sleep(value)
    # update the data variable
    data = value
print("Main thread ends here")

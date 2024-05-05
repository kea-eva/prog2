# Tråder med synkronisering
import threading     #import the threading module

def print_Sensor_1():
    print('\n'"Sensor One"'\n')
    pass

def print_Sensor_nr2():
    print('\n'"Sensor Two"'\n')
    pass

def print_Sensor_nr3():
    print('\n'"Sensor Three"'\n')
    pass

t1 = threading.Thread(target = print_Sensor_1)  #create the thread t1
t1.start() 
t1.join()     # metoden join() ser til at t1 køres ferdig før t2 starter

t2 = threading.Thread(target = print_Sensor_nr2)  #create the thread t2
t2.start() 
t2.join()

t3 = threading.Thread(target = print_Sensor_nr3)  #create the thread t3
t3.start() 
t3.join()

print('\n'"* --- End Main Loop --- *"'\n')



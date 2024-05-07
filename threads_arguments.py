# sending arguments with threads
import threading

mylist = [1,2,3]
my_list = (1,2,3)

# Creating a thread and passing arguments
t1 = threading.Thread(target=print, args=(100*3,5,1024,))  
t2 = threading.Thread(target=print,args=[mylist])
t3 = threading.Thread(target=print,args=(my_list,))  

# Starting the thread, and join() to synchronize with main thread
t1.start()    
t1.join()

t2.start() 
t2.join()

t3.start() 
t3.join()

print("\n--- end main thread ---\n")
print("Is it running?", {t1.is_alive()}, {t2.is_alive()}, {t3.is_alive()},"\n")  



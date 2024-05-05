from threading import Thread
import time

def show_timer():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f'Tœller {count} sek ...\n')

t = Thread(target=show_timer, daemon=True)
t.start()
stop_deamon = input(' > Exit? Indtast noget + ENTER \n')

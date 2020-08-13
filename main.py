import os
import threading

def send_script():
    os.system('start python ./sender/sender.py')

def middle_script():
    os.system('start python ./middlebox/middlebox.py')

def receive_script():
    os.system('start python ./receiver/receiver.py')

if __name__ == '__main__':
    send_script()
    middle_script()
    receive_script()

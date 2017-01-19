#Author=Brandon Ellington

import os
import datetime
import random

def countdown(n):
    while n > 0:
        print (n)
        n = n - 1
    print('Blastoff')

# countdown(200)

def countdown_till_chanukkah():
     
    chanukkah = datetime.datetime(2016, 12, 24)
    now = datetime.datetime.now()
    delta = chanukkah - now
    print(delta)
'''
while True:
    try:
        n = 0
        countdown_till_chanukkah()
        while n < 10000:
            n = n + 1
        
    except KeyboardInterrupt:
        exit()

'''
    

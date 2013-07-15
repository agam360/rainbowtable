'''
Author: Agam More
Description: This program illustrates a rainbow table mechanism
'''

import random
#import pickle
import cPickle as pickle
import hashlib
import string

def save(path, data):
    ''' Save data to a .pkl file in specific path '''
    output = open(path, 'w')
    pickle.dumps(data, output)
    output.close()
    
def load(path):
    ''' Load .pkl file from path '''
    pkl = open(path, 'r')
    data = pickle.load(pkl)
    pkl.close()
    return data

def md5(plaintext):
    ''' Return the MD5 calculated hash of a text '''
    return hashlib.md5(str(plaintext)).hexdigest()

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    ''' Credit: jellyfishtree (http://stackoverflow.com/questions/2267362/convert-integer-to-a-string-in-a-given-numeric-base-in-python)'''
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def strToNum(strData, num=0 ,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((len(strData)==0) and num) or (strToNum(strData[0:-1], num+numerals.index(strData[-1])**len(strData)))

def reducef(hashData):
    return baseN(hashData[0:6], 10)

l = 3 #Max size of rainbow table items
test = random.random()* 100 //1
hashTest = md5(test)
print test
print hashTest
print strToNum('test')
#print reducef(hashTest)

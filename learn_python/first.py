#!/usr/local/bin/python3

#A first Python script
import sys  #import sys module for mutile module
print ( sys.platform )
print ( 2 ** 100 ) # 2^100
x = 'Spam!'
print ( x * 8 )

#load myfile module
import myfile
print ( myfile.title )

#index
S = "Spam"
print ( "S=" + S[:] )
print ( 'S[0]=' + S[0] + ' S[-1]=' + S[-1] + ' S[1:3]=' + S[1:3] )
print ( "S[1:]=" + S[1:] )
print ( "S[:3]=" + S[:3] )
print ( "S[:-1]=" + S[:-1] )
#S[0] = 's'
#Traceback (most recent call last):
#  File "./first.py", line 21, in <module>
#    S[0] = 's'
#TypeError: 'str' object does not support item assignment

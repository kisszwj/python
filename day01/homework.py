#!/usr/local/bin/python3

print ( '---------------Python-------------------' )
temp  = input("Input data for guess:")
guess = int(temp)

if 1 <= guess <= 100:
	print ( "You are right!" )
else:
	print ( "You are wrong! ")



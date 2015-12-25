#!/usr/local/bin/python3

print ( '---------------Python-------------------' )
temp  = input("Input data for guess:")
guess = int(temp)

if 8 == guess:
	print ( "You are right!" )
	print ( "but you can\'t get anything!" )
else:
	print ( "You are wrong! ")

print ( "^_^ Game Over ^_^" )

print ( dir ( __builtins__ ) )
#print ( help ( print ) )
#print ( help ( int ) )
#print ( help ( input ) )

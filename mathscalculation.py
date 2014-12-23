#Maths Function Call Page
def mathscall(x,y):
	from mathspack import mymaths
	MathsObject = mymaths(x,y)
	return MathsObject.MathsOperations()
a = raw_input('Enter First Number : ')
b = raw_input('Enter Second Number: ')
ans = mathscall(a,b)
print (ans)

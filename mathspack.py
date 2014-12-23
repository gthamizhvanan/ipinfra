# Maths Package Class File
class mymaths:
	def __init__ (params, x, y):
	   	params.x = x
		params.y = y
	def addnum(params):
		z = int(params.x)+int(params.y)
		return z
	def subnum(params):
		z = int(params.x)-int(params.y)
		return z
	def mulnum(params):
		z = int(params.x)*int(params.y)
		return z
	def divnum(params):
		z = int(params.x)/int(params.y)
		return z
	def moddivnum(params):
        	z = int(params.x)%int(params.y)
        	return z
	def MathsOperations(params):
		result = ''
		result += str('Addition Of X,Y        : ')+str(mymaths.addnum(params))+'\n'
		result += str('Subtraction Of X,Y     : ')+str(mymaths.subnum(params))+'\n'
		result += str('Multiplication Of X,Y  : ')+str(mymaths.mulnum(params))+'\n'
		result += str('Division Of X,Y        : ')+str(mymaths.divnum(params))+'\n'
		result += str('Modulo Division Of X,Y : ')+str(mymaths.moddivnum(params))+'\n'
		return result

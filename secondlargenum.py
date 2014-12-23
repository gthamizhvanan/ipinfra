print ("Write a program to implement a method which takes a list as an argument and returns second largest number. Read from standard input and write to standard output.")

# FIRST WAY #
il = [14,13,15,10]
print (str('LIST ITEM  = ')+str(il))
res = il[0]
for i,j in enumerate(il):
	if (il[i] > res):
		res = il[i]
for i,j in enumerate(il):
	if (il[i] < res):
		res = il[i]
		break	
print (str('FIRST WAY  = ')+str(res)+(' Loop Condition Based'))

# SECOND WAY #
il = [14,13,15,10]
maxval2 = max(il)
il.remove(maxval2)
res = max(il)
print (str('SECOND WAY = ')+str(res)+(' Max Function Based'))

# THIRD WAY #
il = [14,13,15,10]
il.sort()
res = il[-2]
print (str('THIRD WAY  = ')+str(res)+(' Sort Function Based'))

# FOURTH WAY #
#isl  = [14,13,15,10]
#ress = isl[0]
#results = []
#def funsecondlargenum(isl):
#	for i,j in enumerate(isl):
#		if(isl[i] > ress):
#			ress = isl[i]
#		else:
#			results.append(isl[i])
#
#for i,j in enumerate(isl):
#	resultval = funseconlargenum(isl)

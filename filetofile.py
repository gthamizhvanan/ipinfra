print('Write a program which will read a file from given path, calculate the size of the file and write it to another file. Also append timestamp, if the size of the file is greater than 1 MB then throw an error. Implement using try catch. ')

#with open('docs/textcontent.odt', 'r') as content_file:
#    content = content_file.read

from datetime import datetime
utc_time = datetime.utcnow()
try:
	r_document = open('docs/textcontent.odt','r')
	r_content  = r_document.read()
	r_size     = r_document.tell()
	r_content  = str(r_content)+str('\nFile Created Time : ')+str(utc_time)+str('\nFile Size : ')+str(r_size)
	if(r_size > 1000000):
		raise Exception()
	else:
		w_document = open('docs/textcontent_py.odt','w+')
		w_content  = w_document.write(r_content)
		rw_document = open('docs/textcontent_py.odt','r')
		print ('File Created And Write The Content Successfully !!')
		print (utc_time)
except:
	print 'File Size Should Be Less Than 1 MB'

#Actions Of Book
import time
import booklib

## FUNCTION CALL FOR BOOK##
def funBook(bookdetails,condition,action):
	if(action == 'add'):
		booklib.createBook(bookdetails)
	if(action == 'edit'):
                booklib.updateBook(bookdetails,condition)
	if(action == 'view'):
                booklib.readBook(condition)
	if(action == 'delete'):
                booklib.deleteBook(condition)


def funBookAction(actionFor):
	if(actionFor == 'a' or actionFor == 'A'):
		## ADD BOOK DETAILS ##
		bname = raw_input('Enter book name            ? ')
		bauthor = raw_input('Enter author af the book ? ')
		bversion = raw_input('Enter book version      ? ')
		createdon = time.strftime('%Y-%m-%d %H:%M:%S')
		modifiedon = time.strftime('%Y-%m-%d %H:%M:%S')
		booklist = funBook([bname,bauthor,bversion,createdon,modifiedon],'','add')
		#addBook(['1','test','testa','1.0','34','43'])

	if(actionFor == 'v' or actionFor == 'V'):
		## VIEW BOOK DETAILS ##
		bid = raw_input('Enter book id ? ')
		booklist = funBook('',bid,'view')

	if(actionFor == 'd' or actionFor == 'D'):
		## DELETE BOOK DETAILS ##
		bid = raw_input('Enter book id ? ')
		booklist = funBook('',bid,'delete')

	# if(actionFor == 'u' or actionFor == 'U'):
	# 	## EDIT BOOK DETAILS ##
	# 	bname = raw_input('Enter book name            ? ')
	# 	bauthor = raw_input('Enter author af the book ? ')
	# 	bversion = raw_input('Enter book version      ? ')
	# 	modifiedon = time.strftime('%Y-%m-%d %H:%M:%S')
	# 	bid = raw_input('Enter book id                ? ')
	# 	booklist = funBook([('bname',bname),('bauthor',bauthor),('bversion',bversion),('modifiedon',modifiedon)],[('bid',bid)],'edit')



print ('Which Action Do You Want From Below ? ')
print ('Add Book Press a and Enter            ')
print ('Edit Book Press u and Enter           ')
print ('View Book Press v and Enter           ')
print ('Delete Book Press d and Enter         ')
useraction = raw_input('Your Option Please ?  ')

print funBookAction(useraction)



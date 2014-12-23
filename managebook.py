#Actions Of Book
import time
import booklib

## FUNCTION CALL FOR BOOK##
def funBook(bookdetails,condition,action):
	if(action == 'add'):
		return booklib.createBook(bookdetails)
	if(action == 'edit'):
                return booklib.updateBook(bookdetails,condition)
	if(action == 'view'):
                return booklib.readBook(condition)
	if(action == 'delete'):
                return booklib.deleteBook(condition)


def funBookAction(actionFor):
	if(actionFor == 'a' or actionFor == 'A'):
		## ADD BOOK DETAILS ##
		bname = raw_input('Enter book name            : ')
		bauthor = raw_input('Enter author af the book : ')
		bversion = raw_input('Enter book version      : ')
		createdon = time.strftime('%Y-%m-%d %H:%M:%S')
		modifiedon = time.strftime('%Y-%m-%d %H:%M:%S')
		result = funBook([bname,bauthor,bversion,createdon,modifiedon],'','add')
		if(result>0):
			return 'Book Inserted Successfully !!!'
		#addBook(['1','test','testa','1.0','34','43'])

	if(actionFor == 'u' or actionFor == 'U'):
                ## EDIT BOOK DETAILS ##
		booklibval = booklib.listBook()
		for i,j in enumerate(booklibval):
			print j
		bid = raw_input('Enter book id                : ')
                bname = raw_input('Enter book name            : ')
                bauthor = raw_input('Enter author af the book : ')
                bversion = raw_input('Enter book version      : ')
                modifiedon = time.strftime('%Y-%m-%d %H:%M:%S')
                booklist = str("bname='")+str(bname)+str("',")+str("bauthor='")+str(bauthor)+str("',")+str("bversion='")+str(bversion)+str("',")+str("modifiedon='")+str(modifiedon)+str("'")
		result = funBook(booklist,bid,'edit')
		if(result>0):
                        return 'Book Updated Successfully !!!'		

	if(actionFor == 'v' or actionFor == 'V'):
		## VIEW BOOK DETAILS ##
		bid = raw_input('Enter book id : ')
		result = funBook('',bid,'view')
		if result!='':
			return result

	if(actionFor == 'd' or actionFor == 'D'):
		## DELETE BOOK DETAILS ##
		bid = raw_input('Enter book id : ')
		result = funBook('',bid,'delete')
		if(result>0):
                        return 'Book Deleted Successfully !!!'
	
	if(actionFor == 'l' or actionFor == 'L'):
		## ALL BOOK DETAILS ##
		print ('All Book Details')
                booklibval = booklib.listBook()
		result = ''
                for i,j in enumerate(booklibval):
                        result += str(j)
		return result

print ('Which Action Do You Want From Below:')
print ('Add Book Press a and Enter         :')
print ('Edit Book Press u and Enter        :')
print ('View Book Press v and Enter        :')
print ('Delete Book Press d and Enter      :')
print ('All Book Details Press l and Enter :')
useraction = raw_input('Your Option Please :')

print funBookAction(useraction)



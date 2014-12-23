#Library Functions For Book
import MySQLdb as mdb
#def addBook(book):
dbcon = mdb.connect('localhost', 'root', 'password', 'test1');

with dbcon:
	def createBook(book):
		cur = dbcon.cursor()
		strvalues = ''
		for i,j in enumerate(book):
			strvalues += str("'")+str(book[i])+str("',")
		strvalues = str("(")+strvalues.rstrip(',')+str(")")	
		insertqry = str("INSERT INTO book (bname,bauthor,bversion,createdon,modifiedon) VALUES ")+strvalues
		cur.execute(insertqry)
		dbcon.commit()
		return dbcon.insert_id()
	def readBook(bookid):
                cur = dbcon.cursor()
                qry = str("SELECT * FROM book WHERE bid = ")+str(bookid)
		cur.execute(qry)
		ver = cur.fetchone()
		print ver
                dbcon.commit()
	def deleteBook(bookid):
                cur = dbcon.cursor()
                qry = str("DELETE FROM book WHERE bid = ")+str(bookid)
                cur.execute(qry)
                ver = cur.fetchone()
                print (ver)
                dbcon.commit()
	#def editBook(bookVal,whereCon):
		#cur = dbcon.cursor()
                #strvalues = ''
                #for i,j in enumerate(book):
              	#	strvalues += str("(")+str(i+str('=')+book[j]+str(')')
		#whereConlength = len(whereCon)
		#if whereConlength>0:
		#	for i,j in enumerate(whereCon):
		#		condition += str(i+str('=')+book[j]+str(' AND ')
		#condition = condition.rstrip(' AND ')
                #qry = str("UPDATE book")+strvalues+condition
		#print (qry)
                #cur.execute(qry)
		#dbcon.commit()

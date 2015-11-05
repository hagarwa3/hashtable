from hashtable import *

table = hash(5)		#test build
table.set("hi",1)	#test insert
table.set("hi",2)	#test insert with overwrite
table.set("hii",1)	#test insert2
table.set("hi4",1)	#test insert 3
print str(table)	#print table
table.set("hi2",1)	#test resize
table.set("hi3",1)	#test insert         
print str(table)        #print table
table.delete("hi")	#test delete
print str(table)	#print table
print table.get("hii")	#test get
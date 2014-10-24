#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, shelve

database = shelve.open("phoneinfo")


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
name = form.getvalue('name')
status = form.getvalue('phone')
num = form.getvalue('key')

print '''\
Content-Type: text/html\n
<html><body>
'''




print '''<form method="get" action="/cgi-bin/tel-database.py">
Command:
<input type="radio" name="phone" value="found">Find
<input type="radio" name="phone" value="inserted">Insert
<input type="radio" name="phone" value="deleted">Delete<br>
key/search: <textarea rows="1" cols="50" name="key"></textarea><br>'''

#adds name and phone number into the database phoneinfo and then prints out that the name was added inside the textarea box
if status == 'inserted':
	database[num] = name
	print 'Value: <textarea rows="1" cols="50" name="name"> Name added: '+database[num]+'</textarea><br>'

#looks for the key and returns the name associated with the key inside the text box, else prints nothing inside
elif status == 'found':
	for e in database.keys():
		if e == num:
			print 'value: <textarea rows="1" cols="50" name="name">Name found: '+database[e]+'</textarea><br>' 
			break
		else:
			print 'value: <textarea rows="1" cols="50" name="name"></textarea><br>'
			break
				
#searches for the key and then deletes the name associated with the key			
elif status == 'deleted':
    for e in database.keys():
		if e == num:
			print 'value: <textarea rows="1" cols="50" name="name" >Name Deleted: '+database[num]+'</textarea><br>'
			del database[e] 
#if nothing is selected then do nothing
else: 			
	print 'value: <textarea rows="1" cols="50" name="name"></textarea><br>' 
	
#finishes printing the html syntax	
print '''
<input type="submit" value="Submit">
</form>

</body></html>'''

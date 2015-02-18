# -*- coding: utf-8 -*-

# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

# contacts = {
#     'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },

#     'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},

#     'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
# }

# Goal 1: Loop through that dictionary to print out everyone's contact information.

# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
#   Github: @shannonturner 

# Beyonce's contact information is:
#   Phone: 303-404-9876
#   Twitter: @beyonce
#   Github: @bey

# for contact, info in contacts.items():
# 	print "{0}'s contact information is:".format(contact)
# 	print "\tPhone: {0}".format(info['phone'])
# 	print "\tTwitter: {0}".format(info['twitter'])
# 	print "\tGithub: {0}\n".format(info['github'])

# Goal 2:  Display that information as an HTML table.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>

# for contact, info in contacts.items():

# 	print '<table border="1">'
# 	print '<tr>'
# 	print 'td colspan="2"> {0} </td>'.format(contact)
# 	print '</tr>'
# 	print '<tr>'
# 	print '<td> {0} </td>'.format(info['phone'])
# 	print '<td> {0} </td>'.format(info['twitter'])
# 	print '<td> {0} </td>'.format(info['github'])
# 	print '</tr>'
# 	print '</table>'

# ...

# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

# with open("contacts.html", "w") as people:

# 	people.write("<p><b>Contact Information</b></p>")
		
# 	for contact, info in contacts.items():

# 		people.write('<table border="1">')
# 		people.write('<tr>')
# 		people.write('<td colspan="3"> {0} </td>'.format(contact))
# 		people.write('</tr>')
# 		people.write('<tr>')
# 		people.write('<td> {0} </td>'.format(info['phone']))
# 		people.write('<td> {0} </td>'.format(info['twitter']))
# 		people.write('<td> {0} </td>'.format(info['github']))
# 		people.write('</tr>')
# 		people.write('</table>')

# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).

with open("contacts.csv", "r") as contacts_csv:

	contacts = contacts_csv.read().split("\n")

with open("contacts.html", "w") as people:

	people.write("<p><b>Contact Information</b></p>")
	
	for index, contact in enumerate(contacts):
		contacts[index] = contact.split(",")

		people.write('<table border="1">')
		people.write('<tr>')
		people.write('<td colspan="3"> {0} </td>'.format(contacts[index][0]))
		people.write('</tr>')
		people.write('<tr>')
		people.write('<td> {0} </td>'.format(contacts[index][1]))
		people.write('<td> {0} </td>'.format(contacts[index][2]))
		people.write('<td> {0} </td>'.format(contacts[index][3]))
		people.write('</tr>')
		people.write('</table>')

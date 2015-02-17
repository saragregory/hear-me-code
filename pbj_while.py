# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

bread = 6
pb = 4
jelly = 10
sandwiches = 0

while bread >= 2 and pb > 0 and jelly > 0:
	bread = bread - 2
	pb = pb - 1
	jelly = jelly - 1
	sandwiches = sandwiches + 1
	print "I just made sandwich #{0}.".format(sandwiches)
	# print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more and enough jelly for {2} more".format(bread/2,pb,jelly)


# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

if bread == 0 and pb == 0 and jelly == 0:
	print "All done, I ran out of ingredients."
elif bread <= 1 and pb >= 1 and jelly >= 1:
	print "All done, I ran out of bread."
elif pb <= 1 and bread >= 2 and jelly >= 1:
	print "All done, I ran out of peanut butter."
elif jelly <= 1 and bread >= 2 and pb >= 1:
	print "I ran out of jelly but I can make a peanut butter sandwich."

print "I had enough ingredients to make {0} sandwiches.".format(sandwiches)


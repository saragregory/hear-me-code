# Goal 1: Change your Lesson 2 playtime states.py to use file handling to create your lists.

# Open states.txt or states.csv
# How to get the abbreviations into one list, and the state names into the other?

# Break everything into smaller steps, run and test often!

with open("states.txt", "r") as states_file:

	states = states_file.read().split("\n")

# Goal 2: Instead of printing out to the screen, write to a file

with open("states.html", "w") as dropdown:

	dropdown.write("<p>Select a state:</p>\n")
	dropdown.write("<select>")

	for index, state in enumerate(states):
		states[index] = state.split("\t")

# for states, abbrev in zip(states, states_abbrev):
		dropdown.write('\t<option value="{0}">{1}</option>\n'.format(states[index][0], states[index][1]))

		# dropdown.write('\t<option value="{0}">{1}</option>\n'.format(states[index][0], states[index][1]))

	dropdown.write("</select>")

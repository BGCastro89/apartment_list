import random

def familyfri(names):
	"""
	Generates random groupings of 3-5 names each

	args: List of Strings, representing names of people to be grouped
	return: List of List of Strings, representing the randomized grouping
	"""

	random.shuffle(names)

	groupings = []
	group = []


	for i in xrange(len(names)):

		group.append(names[i])
		if i%3 == 2:
			groupings.append(group)
			group = []
		
	if groupings:
		for n in group:
			groupings[0].append(n)

	else:
		groupings = [group]

	return groupings




names = ["bob","jane","sue","dan","john","paul","george","ringo"]
print "\n", familyfri(names)

names = ["bob","jane"]
print "\n", familyfri(names)

names = []
print "\n", familyfri(names)

names = ["jane","sue","dan","paul","john","ringo"]
print familyfri(names)

names = ["dan","paul","john","george","ringo"]
print familyfri(names)

names = ["bob","jane","dan","paul","john","george","ringo"]
print familyfri(names)

# All people in a group
# No one in 2 groups
# Groups must 3 - 5







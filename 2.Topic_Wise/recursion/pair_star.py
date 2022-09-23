## Read input as specified in the question.
## Print output as specified in the question.
# Recursive CPP program to insert * between
# two consecutive same characters.

# Function to insert * at desired position
def pairStar(Input, Output, i = 0) :
	
	# Append current character
	Output = Output + Input[i]

	# If we reached last character
	if (i == len(Input) - 1) :
		print(Output)
		return;

	# If next character is same,
	# append '*'
	if (Input[i] == Input[i + 1]) :
		Output = Output + '*';

	pairStar(Input, Output, i + 1);


Input = input()
Output = ""
pairStar(Input, Output);
	
# This code is contributed by Ryuga

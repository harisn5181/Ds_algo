#Testing on 15-09



n=4
i=1

while i<=n:
	j=1
	start_char=chr(ord('A')+i-1)
	while j<=i:
		charp=chr(ord(start_char)+j-1)
		print(charp,end='')
		j=j+1
	i=i+1
	print()
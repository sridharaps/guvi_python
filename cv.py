j = int(input(" "))
 
for i in range(2, j):
	if j% i  == 0:
		print("no")
		break
else:
	print("yes")
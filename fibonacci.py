# Defining a function which creates first n fibonacci numbers 

def fibonacci(n):
	'''
	prints first n numbers of fibanacci series

	parameters n: It is number of terms
	precondition:It is integers 

	>>> fibonacci(3)
	0
	1
	1
	'''
	# 
	if n == 0 :
		print("Sorry it doesn't make sense ")
		quit()
	elif n == 1 :
		print(0)
		quit()
	print(0)
	print(1)
	lst = [0, 1]   # accumulator to store previous value 0,1,1,2,3  
	for x in range(n - 2):
		next_val = lst[x] + lst[x + 1]
		print(next_val)
		lst.append(next_val)
	print(f"The {n} th term of fibonacci is : ", next_val)
# Propmpting user to enter a integer value
integer_n = int(input("Enter a integer value > 0 : "))
fibonacci(integer_n)
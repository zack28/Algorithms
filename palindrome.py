def palindrome(n):
	num=n
	d=0
	rev=0
	while n>0:
		d=n%10
		n=n//10
		rev=rev*10+d
	if num==rev:
		return True
	else:
		return False
a=int(input("Enter a number:"))
if palindrome(a):
	print(a,"is a Palindrome")
else:
	print(a,"is not a Palindrome")

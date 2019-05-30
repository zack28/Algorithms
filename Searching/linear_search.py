def search(a,key):
	i=0
	while i< len(a):
		if a[i] == key:
			return True
			globals()['pos']=i
		i=i+1
	return False

a=[]
n=int(input("Enter No Of Elements in the list: "))

for i in range(0,n):
	ele=int(input())
	a.append(ele)

print(a[0])

key=int(input("Enter The No To Be Searched: "))
if search(a,key):
	print("Found at",pos+1)
else:
	print("Not Found")
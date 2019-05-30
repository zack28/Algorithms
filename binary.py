def search(a,key):
	l=0 #lower bound
	u=len(a)-1

	while l<=u:
		mid = (l+u)//2

		if a[mid] == key:
			globals()['pos']=mid
			return True
		else:
			if a[mid]<key:
				l=mid
			else:
				u=mid



a=[]
n=int(input("Enter No Of Elements in the list: "))

for i in range(0,n):
	ele=int(input())
	a.append(ele)

print(a)

key=int(input("Enter The No To Be Searched: "))
if search(a,key):
	print("Found at",pos+1)
else:
	print("Not Found")
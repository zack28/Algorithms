def sort(a):
	for i in range(len(a)-1,0,-1):
		for j in range(i):
			if a[j]>a[j+1]:
				temp=a[j]
				a[j]=a[j+1]
				a[j+1]=temp

a=[]
n=int(input("Enter No Of Elements in the list: "))

for i in range(0,n):
	ele=int(input())
	a.append(ele)

print(a)

sort(a)
print("Sorted List",a)
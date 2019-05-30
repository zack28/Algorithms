def sort(a):
	for i in range(len(a)-1):
		min_pos=i
		for j in range(i,len(a)):
			if a[j]<a[min_pos]:
				min_pos=j

		temp=a[i]
		a[i]=a[min_pos]
		a[min_pos]=temp

		print(a)

a=[]
n=int(input("Enter No Of Elements in the list: "))

for i in range(0,n):
	ele=int(input())
	a.append(ele)

print(a)

sort(a)
print("Sorted List",a)
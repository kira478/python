#Definisemo bubble sort
def bubbleSort(alist):  #Za svaki broj iz liste...
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):    
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = list()
num = raw_input("\nEnter number of elements: ") #Uneti broj elemenata koje treba poslagati

for i in range(int(num)):   
    n = raw_input("num: ")  
    alist.append(int(n))    #Kada se unese broj automatski se pojavljuje u alist-i i sortira se na osnovu velicine

print("\nThe unsorted array: ")     #Ovde se pojavljuje niz redom kojim ste pisali brojeve
print(alist)

bubbleSort(alist)

print("\nThe sorted array: ")   #Ovde se pojavljuje sortiran niz od najmanjeg ka najvecem
print(alist)

#Kira.

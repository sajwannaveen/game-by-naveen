# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i]),

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i]),


import pygame
import random
def game(var,s,power,gl):
    screen = pygame.display.set_mode((640, 480), 0, 32)

    def cir(c,p,r,p1,p2,color):
        screen.fill((0,0,0))
        pygame.draw.line(screen,color,p1,p2)
        pygame.draw.circle(screen,c,p,r)
        pygame.display.update()
    def line(p1,p2,color,c,p,r):
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen,c,p,r)
        pygame.draw.line(screen,color,p1,p2)
        pygame.display.update()
    def call(s,power,point1=[0,450],point2=[25,450]):
        global L
        
        x,y=0,0
        ch=0
        total=0
        global points
        points=0
        end=1
        ank=0
        while(end==1 and ank< gl):
            ank+=1
    
            global har
            ch+=1
            cir_cor=(random.randrange(256),random.randrange(256),random.randrange(256))
            cir_pos=[random.randrange(1,100),0]
            i=1
            while(1==1):
                cir(cir_cor,tuple(cir_pos),10,point1,point2,[255,255,255])
                for event in pygame.event.get():
                    if(event.type==pygame.KEYDOWN):
                        if(event.key==pygame.K_RIGHT ):
                            x=s
                        elif(event.key==pygame.K_LEFT ):
                            x=-s
                        elif(event.key==pygame.K_ESCAPE):
                            quit()
                    if(event.type==pygame.KEYUP):
                        if(event.key==pygame.K_RIGHT):
                            x=0
                        elif(event.key==pygame.K_LEFT):
                            x=0
                        elif(event.key==pygame.K_ESCAPE):
                            quit()
                    point1[0]+=x
                    point2[0]+=x
                    line(tuple(point1),tuple(point2),[255,255,255],cir_cor,tuple(cir_pos),10)
                    break
                if(cir_pos[1]==440):
                    break
                if(i%(var-power)==0):
                    cir_pos[1]+=1            
                i+=1
                if(cir_pos[1]==440 and cir_pos[0]>=point1[0] and cir_pos[0]<=point2[0] ):
                    points+=1
                if(cir_pos[1]==440):
                    if(cir_pos[0]<point1[0] or cir_pos[0]>point2[0]):
                        end=0
            if(end==0 or ank==gl-1):
                print("your Point is ",points)
    L=[[0,450],[25,450]]
    call(10,0,L[0],L[1])
print("+---------------------+")
print("| MAIN MENU  |")
print("+---------------------+")
print("+--------------------------------------------------------------------------+")
print("|            1)Game with constant speed                |")
print("|            2)Game with variable speed                  |")
print("|            0)Exit                                                       |")
print("+---------------------------------------------------------------------------+")
choice=int(input("Enter your choice"))
if(choice==1):
    sp=int(input("Enter your speed between 0-4"))
    game(5,10,sp,100)
elif(choice==2):
    for x in range(10):
        print("Level           :-",x+1,end="                        ")
        game(10,10,x,3)
elif(choice==0):
    quit()
else:
           print("asfjk")

  
import math 

def primeFactors(n):

    list1 = []
    
    while n % 2 == 0: 
        list1.append(2) 
        n = n / 2
          
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        while n % i== 0: 
            list1.append(i) 
            n = n / i 
              
    if n > 2: 
        list1.append(n)
        
    string = "*".join(map(str,list1))
    print string    

while "true":
	n = input("Dwse ari8mo mexri to 1000000:  ")
	if n < 1000000:
		break
primeFactors(n)


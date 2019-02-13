from sys import maxsize 
  
def maxSubArraySum(a,size): 
  
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
    end = end+1
  
    print ("Maximum contiguous sum is %d"%(max_so_far)) 
    print (a[start:end])
  
a = [-1, -3, 4, 6, -2, 1, -3, 5, 1] #den hmoun sigouros an eprepe na dinete h lista san input apo ton xrhsth h oxi
maxSubArraySum(a,len(a)) 

#how to find the index of array by searching operation

def linearSearch(arr, search_element, n):
    for i in range(n):
        if arr[i] == search_element:
            return i
      
       
arr = [12,23,11,13,343]
search_element=1111
n=len(arr)
result=linearSearch(arr, search_element, n)  
print("search element index is",result)

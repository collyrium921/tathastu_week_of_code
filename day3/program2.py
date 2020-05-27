from itertools import permutations 
  
def allPermutations(str): 
    permList = permutations(str) 
    for perm in list(permList):
        print (''.join(perm)) 
        
# Driver program 
if __name__ == "__main__": 
    sr = str(input("Enter string  "))
    print("Permutations are-----")
    allPermutations(sr) 

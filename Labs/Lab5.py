print("Enter a number and you will get all of the prime numbers of it!") 
endNumber = int(input())                                         

Beginning = 0                            
Conclusion = endNumber                   

for prime in range(Beginning , Conclusion + 1):         
 if prime > 1:                                       
 for x in range(2, prime):
 if (prime % x) == 0:
 break
 else:
 print(prime)                  

print(endNumber)                       

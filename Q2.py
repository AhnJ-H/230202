# Q2 Answer template

N = int(input())
count=0
value=N
while True:    
        N=(N%10)*10+(((N%10)+(N//10))%10)
        count+=1
        if value==N:
            break
        
print(count)
   
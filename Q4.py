# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')
sum=1
for i in range(len(data)):
    if int(data[i])!=0:
        sum*=int(data[i])
    if int(data)==0:
        sum=0
result = sum

print(result)
a= 5454
copy=a
answer=0
while(a!=0):
    digit=a%10
    a=a//10
    answer=answer*10+digit
if(copy==answer):
    print("yes" + str(answer))
else:
    print("not" + str(answer))

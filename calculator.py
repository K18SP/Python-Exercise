a = int(input("Enter one value: "))
print(a)

b = int(input("Enter another value: "))
print(b)

print("0 - addition, 1-subtraction, 2-multiplication, 3-division, 4-modulus")
c = input("Enter the operation to perform on values: ")
print(c)

def switch(c,a,b):
    if c == '0':
        return a+b
    elif c=='1':
        return a-b
    elif c=='2':
        return a*b
    elif c=='3':
        return a/b
    elif c=='4':
        return a%b
    else:
        return "Given operation is wrong"
    
result = switch(c,a,b)
print("Result: ",result)
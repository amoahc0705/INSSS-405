# num1=20
# num2=40
# num3=50
def request():
    num1=input('Enter Variable num1')
    num2=input('Enter variable num 2')
    num3=input('Enter Variable num3')
    print(addition(num1,num2,num3))
    print(average(num1,num2,num3))
    print(max(num1,num2,num3))
    print(min(num1,num2,num3))
    print(product(num1,num2,num3))
def addition(num1,num2,num3):
    sum=int(num1)+int(num2)+int(num3)
    return sum
def average(num1,num2,num3):
    mean=(int(num1)+int(num2)+int(num3))/3
    return mean
def maximum(num1,num2,num3):
    highest=int(num1),int(num2),int(num3)
    return highest
def minimum(num1,num2,num3):
    lowest=int(num1),int(num2),int(num3)
    return lowest
def product(num1,num2,num3):
    multiplication=int(num1)*int(num2)*int(num3)
    return multiplication
request()


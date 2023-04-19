#collect input from the user
#determine if the given number is odd or even

def request():
 num=int(input('Enter variable num'))
 print(even(num))
def even(num) :
    if(int(num)%2==0):
        return 'Even number'
    else:
        return 'Odd number'
request()


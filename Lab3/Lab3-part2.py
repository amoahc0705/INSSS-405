
Score1=input('Enter Score for INS405:')
Score2=input('Enter Score for BUIS 360')
Score3=input('Enter Score for DANL 470')

sum=int(Score1)+int(Score2)+int(Score3)
average=int(sum)/3
print(sum)
print(average)

#>100-A
#70-89-B
#60-69- C
#<59-F

if(int(average)>90):
    print('A')
elif(int(average)>=70 and int(average)<=89):
    print('B')
elif(int(average)>=60 and int(average)<=69):
    print('C')
else:
    print('F')

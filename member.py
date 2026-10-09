print("enter 3 marks")
m1=int(input())
m2=int(input())
m3=int(input())

t=m1+m2+m3
av=int(t/3)
vr=range(0,101)

if av not in vr:
    print('invalid input')
elif av in range(91,101):
    print("Grade a1")    
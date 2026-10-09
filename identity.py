x=5
if type(x) is int:
    print("true")
else:
    print("false")

a=5.5
if type(a) is not float:
    print("true")
else:
    print("false")

y=20
q=20
if y is q:
    print("both r same")
q=50
if y is not q:
    print("they are different.")            
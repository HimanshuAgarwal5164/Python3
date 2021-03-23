d={10:'xyz',1:'abc',15:'aaa',7:'zzz',0:'mno',9:'def'}

def f(k):
    return d[k]


print("Sorting wrt keys")
d1=sorted(d)
for x in d1:
    print(x,'\t',d[x])

print("\n---------------------------------------\n")
print("Sorting wrt values")
d2=sorted(d,key=f)
for x in d2:
    print(x,'\t',d[x])

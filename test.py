a = {1: 10, 2: 20}

for k,v in a.items():
    print(k,v)
    del a[k]

print(a)
import string
s = string.ascii_lowercase

l = [c for c in s]

def f2(l): 
    i=0
    while i < len(l):
        print(l[i])
        i+=1

f2(l)
def dec(leng):
    def new_leng(*args,**kwargs):
        print('Running function: ', leng.name)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', kwargs)
        result = leng(*args, **kwargs)
        print('Result: ', result)
        return result

    return new_leng

print(dec(f2))
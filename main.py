def myfunc(args):
    out = []
    for i in range(len(args)):
        if i % 2 == 0:
            out.append(args[i].lower())
        else:
            out.append(args[i].upper())
    return ''.join(out)


print(myfunc("HELLO"))

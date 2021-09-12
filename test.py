def foo():
    bar = 1
    return bar

def tree(baz):
    resalt = baz + 1 
    print(resalt)

while True:
    baz = foo()
    tree(baz)
    break


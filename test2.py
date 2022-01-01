def a(c):
    return 2*c > 10
def b(c):
    if a(c):
        print('yes!')
    else:
        print('nooooo...')
b(int(input()))
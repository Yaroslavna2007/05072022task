g = int(input('введите натуральное число'))
v = int(input('введите натуральное число'))
n = int(input('введите натуральное число'))
if n==v==g:
    print(3)
elif n!=v!=g:
    print(0)
elif g==n and g!=v and n!=v:
    print(2)
elif g==v and g!=n and v!=n:
    print(2)
elif v==n and v!=g and n!=g:
    print(2)

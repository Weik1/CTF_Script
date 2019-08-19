str = input('input str:')
urlencode = ''
for c in str:
    c = ord(c)
    c = hex(c)
    c = c.replace('0x','%')
    urlencode+=c
print(urlencode)

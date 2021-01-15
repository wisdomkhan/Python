def swap_equipos(l):  # sawpping equiposition alphabets
    x = ''
    for k in l:
        x += k.replace(k, chr(219 - ord(k)))
    return x


s = input('enter a string\t')
print(swap_equipos(s))

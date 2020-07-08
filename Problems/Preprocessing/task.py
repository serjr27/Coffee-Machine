i_str = input().split()
o_str = ''

for s in i_str:
    o_str += s.strip('!,.?') + ' '

print(o_str.lower())

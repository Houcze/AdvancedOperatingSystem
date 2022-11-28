with open('vinput.c') as f:
    src = f.read()

src = src.split('\n')

newsrc = []
newsrc.append(src[0])
for lindex in range(1, len(src)):
    newsrc.append(src[lindex][(len(str(lindex+1))+1):])


s = ''
for line in newsrc:
    s += line
    s += '\n'

with open('vinput2.c', 'w') as f:
    f.write(s)

    

f = open('kasstheme.txt', 'r')
lines = f.readlines()
f.close()

mystr = ' '.join([line.strip() for line in lines])
data = bytearray.fromhex(mystr)

f = open('kasstheme.mid', 'a')
f.write(data)
f.close()

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src, 'r')
tab_content = f.read()
f.close()

space_contect = tab_content.replace("\t", "a"*4)
print(space_contect)

f = open(dst, 'w')
f.write(space_contect)
f.close()

import codecs

enc = codecs.getencoder("rot-13")
a = "ABC"
b = enc(a)[0]

print(b)


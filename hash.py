b={}
b[1]=1
for k in b.keys:
	print b[k]

#Traversing a dictionare
for k,v in b.items:
	print k,":",v

#Two create a combination of list into dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
hash = {k:v for k, v in zip(keys, values)}
hash
#{'a': 1, 'c': 3, 'b': 2}

#Python provides hashlib for secure hashes and message digest
import hashlib
hashlib.md5('a')
hashlib.sha512('a')
hashlib.md5('a').digest()#Prints the hash digest 

import hashlib
filename = input("enter file path:") 
data=open(filename,'rb').read()
md5_hash=hashlib.md5(data).hexdigest()
print(md5_hash)
sh_256=hashlib.sha256(data).hexdigest()
print(sh_256)
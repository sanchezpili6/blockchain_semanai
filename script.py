# import sha256
from hashlib import sha3_256
# text to hash
text='I am excited to learn about blockchain!'
hash_result= sha3_256(text.encode())
# print result
print(hash_result.hexdigest())
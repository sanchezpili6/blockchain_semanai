from datetime import datetime
from hashlib import sha3_256


class Block:
# default constructor for block class
  def __init__(self, transactions, previous_hash, nonce=0):
    self.transactions=transactions
    self.previous_hash=previous_hash
    self.nonce=nonce
    self.timestamp=datetime.now()
    self.hash=self.generate_hash()
  def print_block(self):
    print('timestamp: ', self.timestamp)
    print('transactions: ', self.transactions)
    print('current hash: ', self.generate_hash())

  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
    block_hash= sha3_256(block_contents.encode())
    return block_hash.hexdigest()

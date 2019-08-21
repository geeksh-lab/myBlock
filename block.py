import datetime
from hashlib import sha256
#la class Block qui permet de generer un hash et de faire l horodatage avec un constructeur qui nous permet de stockeur
class Block:
  def __init__(self, transactions, previous_hash):
    self.timestamp = datetime.datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.hash = self.generate_hash()
   #fonction qui nous affiche le block 
  def print_block(self):
    # prints block contents le contenu du block
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
   #fonction de hashage de la block 
  def generate_hash(self):
	  #le hash generer par le bloc
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()

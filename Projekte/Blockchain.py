'''
Blockchain

Reversed Linked List
Man kann keine Transaktion ändern, weil sich der Hashwert sonst ändert!

Beispiel: PBCoin (PBC)

Transaktion 1 (t1): Anna sends Bob 2 PBC
Transaktion 2 (t2): Bob sends Alice 4.3 PBC
Transaktion 3 (t3): Mark sends Daniel 3.2 PBC

InitialBlock B1 (kennt alle 3 Transaktionen)
B1("AAA", t1, t2, t3) -> Hash 76fd89
B2("76fd89", t4, t5, t6) -> Hash 8923ff
B3("8923ff", t7)
'''
import hashlib

class PBCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = " # ".join(transaction_list) + " # " + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() # hash berechnen


t1 = "Anna sends Mike 2 PBC"
t2 = "Bob sends Mike 4.1 PBC"
t3 = "Mike sends Bob 3.2 PBC"
t4 = "Daniel sends Anna 0.3 PBC"
t5 = "Mike sends Charlie 1 PBC"
t6 = "Mike sends Daniel 5.4 PBC"

# erstelle Initialblock mit initial hash und einer Liste an Transaktionen
initial_block = PBCoinBlock("initial String", [t1, t2])
print(initial_block.block_data)
print(initial_block.block_hash)

second_block = PBCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = PBCoinBlock(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash)

# wird nun in einer Transaktion etwas geändert, ändert sich sukzessive der
# Hashwert und man erkennt eine Veränderung
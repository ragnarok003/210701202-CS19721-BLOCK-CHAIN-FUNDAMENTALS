import hashlib

class JCoinBlock:
    def __init__(self,previous_block_hash,transaction_list):
        self.previous_block_hash=previous_block_hash
        self.transaction_list=transaction_list

        self.block_data='-'.join(transaction_list) +'-'+previous_block_hash
        self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()

    
t1="Roku send 1 JC to Jack"        
t2="Stark send 2 JC to Steve"        
t3="Bruce send 3 JC to Thor"        
t4="Rohdey send 1 JC to Scott"        
t5="Will send 2 JC to Hector"        
t6="Peter send 3 JC to Ned"        
t=[t1,t2,t3,t4,t5,t6]

def blockprint(block):
    print(block.block_data)
    print(block.block_hash,"\n")

initial_hash="InitialString"
for i in range(0,len(t)-1):
    blockprint(JCoinBlock(initial_hash,t[i:i+2]))
import time
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(1, "0")
        
    def create_block(self, proof, previous_hash):
        block = dict(
            index = len(self.chain),
            timestamp = time.time(),
            proof = proof,
            previous_hash = previous_hash
        )
        
        self.chain.append(block)
        return block
    
    def print_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        
        while True:
            if self.__validate_proof(previous_proof, new_proof):
                break
            
            new_proof += 1
            
        return new_proof
    
    @staticmethod
    def hash(self, block):
        sha256 = hashlib.sha256()        
        json_block = json.dumps(block, sort_keys=True).encode()
        sha256.update(json_block)
        
        return sha256.hexdigest()
    
    @staticmethod
    def chain_valid(self, chain):
        genesis = chain[0]
        
        if genesis != self.chain[0]:
            return False
        
        for i in range(1, len(chain) - 1):
            curr, prev = chain[i], chain[i-1]
            
            actual_prev_hash = self.hash(prev)
            prev_hash = curr["previous_hash"]
            
            if prev_hash != actual_prev_hash:
                return False
            
            prev_proof = prev["proof"]
            proof = curr['proof']
            
            if not self.__validate_proof(prev_proof, proof):
                return False
            
        return True
    
    @staticmethod
    def __validate_proof(self, previous_proof, new_proof):
        sha256 = hashlib.sha256()
        sha256.update(str(previous_proof**2 - new_proof**2).encode())
        hash_value = sha256.hexdigest()
        
        return hash_value.startswith("f")
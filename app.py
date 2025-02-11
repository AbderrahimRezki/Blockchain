from flask import Flask
from blockchain import Blockchain
import json

app = Flask(__name__)
blockchain = Blockchain()

@app.route("/mine_block", methods=["GET"])
def mine_block():
    prev_block = blockchain.print_previous_block()
    
    prev_proof = prev_block['proof']
    new_proof = Blockchain.proof_of_work(previous_proof=prev_proof)
    
    prev_hash = Blockchain.hash(prev_block)
    new_block = blockchain.create_block(new_proof, prev_hash)
    
    response = json.dumps({
        "message": "Block mined successfully.",
        **new_block
    })
    
    return response, 200

@app.route("/get_chain", methods=["GET"])
def display_chain():
    response = json.dumps({
        "chain": blockchain.chain,
        "chain_len": len(blockchain.chain)
    })
    
    return response, 200

@app.route("/valid", methods=["GET"])
def validate_chain():
    validity = "valid" if Blockchain.chain_valid(blockchain.chain) else "invalid"
    
    response = json.dumps({
        "message": f"Your chain is {validity}." 
    })
    
    return response, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
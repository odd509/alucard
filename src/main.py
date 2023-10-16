from blockchain import Blockchain
from flask import Flask, jsonify, request


app = Flask(__name__)
blockchain = Blockchain()

# Endpoint to mine a new block
@app.route('/mine', methods=['GET'])
def mine():
    blockchain.mine_block()

# Endpoint to create a new transaction
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    transaction_data = {
    'transaction_type': 'create',
    'sender': 'user123',
    'recipient': 'password_manager',
    'password_info': {
        'website': 'example.com',
        'password': 'password123'
    }
}
    """
    transaction_data = request.get_json()  # Get transaction data from the request

    # Extract transaction details
    transaction_type = transaction_data.get('transaction_type')
    sender = transaction_data.get('sender')
    recipient = transaction_data.get('recipient')
    password_info = transaction_data.get('password_info')

    # Add the transaction to the blockchain
    block_index = blockchain.new_transaction(transaction_type, sender, recipient, password_info)

    response = {
        'message': f'Transaction will be added to Block {block_index}'
    }
    return jsonify(response), 201

# Endpoint to view the full blockchain
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.to_dict(),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    # Run multiple nodes on different ports
    app.run()
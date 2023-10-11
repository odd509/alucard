from blockchain import Blockchain
from miner import Miner

# Example usage
if __name__ == "__main__":
    # Create a blockchain
    blockchain = Blockchain()

    # Add transactions
    blockchain.new_transaction("create", "user123", "password_manager", {"website": "example.com", "password": "password123"})
    blockchain.new_transaction("update", "user123", "password_manager", {"website": "example.com", "password": "newpassword123"})

    # Mine a new block
    proof, new_block = Miner.mine(blockchain)

    # Display the mined block
    print("Mined Block Index:", new_block.index)
    print("Mined Block Hash:", new_block.hash())
    print("Mined Block Transactions:", new_block.transactions)
    print("Mined Block Previous Hash:", new_block.previous_hash)
    print("Mined Block Proof of Work:", proof)

    user_id = "user123"
    website = "example.com"
    encrypted_passwords = blockchain.retrieve_user_data(user_id, website)
    print("Encrypted Passwords for", website, ":", encrypted_passwords)
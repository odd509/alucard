from blockchain import Blockchain

# Example usage
if __name__ == "__main__":
    # Create a blockchain
    blockchain = Blockchain()

    # Add transactions
    blockchain.new_transaction("create", "user123", "password_manager", {"website": "example.com", "password": "password123"})
    blockchain.new_transaction("update", "user123", "password_manager", {"website": "example.com", "password": "newpassword123"})
    blockchain.new_transaction("create", "user123", "password_manager", {"website": "example2.com", "password": "password12345"})

    new_block = blockchain.last_block

    # Display the mined block
    print("Mined Block Index:", new_block.index)
    print("Mined Block Hash:", new_block.hash())
    print("Mined Block Transactions:", new_block.transactions)
    print("Mined Block Previous Hash:", new_block.previous_hash)
    print("Mined Block Proof of Work:", new_block.proof)

    user_id = "user123"
    website = "example.com"
    encrypted_passwords = blockchain.retrieve_user_data(user_id, website)
    print("Encrypted Passwords for", website, ":", encrypted_passwords)
    
    encrypted_passwords = blockchain.retrieve_user_data(user_id, "example2.com")
    print("Encrypted Passwords for", "example2.com", ":", encrypted_passwords)

    for block in blockchain.chain:
        print(block.to_dict())
        print()
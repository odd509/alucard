class Wallet:
    def __init__(self, private_key):
        self.private_key = private_key

    def sign_transaction(self, transaction):
        """
        Sign a transaction using the wallet's private key

        :param transaction: Transaction to sign
        :return: The signed transaction
        """
        # Implement your signing logic using the wallet's private key
        # For simplicity, we'll just return the transaction as-is
        return transaction

# Example usage
if __name__ == "__main__":
    # Example private key (replace with your actual private key)
    private_key = "example_private_key"
    wallet = Wallet(private_key)
    transaction_to_sign = {
        "transaction_type": "create",
        "sender": "user123",
        "recipient": "password_manager",
        "password_info": {"website": "example.com", "password": "password123"}
    }
    signed_transaction = wallet.sign_transaction(transaction_to_sign)
    print("Signed Transaction:", signed_transaction)

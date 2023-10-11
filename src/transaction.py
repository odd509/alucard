class Transaction:
    def __init__(self, transaction_type, sender, recipient, password_info):
        self.transaction_type = transaction_type
        self.sender = sender
        self.recipient = recipient
        self.password_info = password_info

    def to_dict(self):
        """
        Convert the transaction to a dictionary

        :return: Dictionary representation of the transaction
        """
        return {
            "transaction_type": self.transaction_type,
            "sender": self.sender,
            "recipient": self.recipient,
            "password_info": self.password_info
        }

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
            "transaction_type": str(self.transaction_type),
            "sender": str(self.sender),
            "recipient": str(self.recipient),
            "password_info": self.password_info
        }
    
class TransactionPool:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, sender, recipient, transaction_type, password_info):
        transaction = Transaction(sender, recipient, transaction_type, password_info)
        self.transactions.append(transaction)

    def get_transactions_by_sender(self, sender):
        return [tx for tx in self.transactions if tx.sender == sender]

    def get_transactions_by_recipient(self, recipient):
        return [tx for tx in self.transactions if tx.recipient == recipient]

    def fetch_transactions(self, max_transactions):
        """
        Fetch a specified number of transactions from the transaction pool and remove them.

        :param max_transactions: Maximum number of transactions to fetch
        :return: List of fetched transactions
        """
        fetched_transactions = self.transactions[:max_transactions]
        self.transactions = self.transactions[max_transactions:]
        return fetched_transactions

    def clear_transactions(self, included_transactions):
        self.transactions = [tx for tx in self.transactions if tx not in included_transactions]


    def to_dict(self):
        """
        Convert the transaction pool to a dictionary.

        :return: Dictionary representation of the transaction pool
        """
        transactions = [transaction.to_dict() for transaction in self.transactions]
        return {'transactions': transactions}
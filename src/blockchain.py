import hashlib
import json
import pickle
import sys
from time import time
from block import Block
from miner import Miner
from transaction import Transaction, TransactionPool

class Blockchain:
    MAX_BLOCK_SIZE = 1000000    # 1 MB
    MAX_TRANSACTIONS_PER_BLOCK = 1
    def __init__(self):
        self.chain = []
        self.transaction_pool = TransactionPool()

        # Create the genesis block
        self.new_block(previous_hash="1", proof=100)


    def new_block(self, proof, previous_hash=None, transactions=[]):
        """
        Create a new block in the blockchain.

        :param proof: Proof of work
        :param previous_hash: Hash of the previous block
        :return: The new block
        """
        block = Block(
            index=len(self.chain) + 1,
            timestamp=time(),
            transactions=[tx.to_dict() for tx in transactions] if transactions else [],
            proof=proof,
            previous_hash=previous_hash or self.hash(self.chain[-1]) if self.chain else None
        )

        print(block.to_dict())
        self.chain.append(block)
        return block
    

    def is_valid_block(self, block):
        """
        Check if a block is valid.

        :param block: The block to be validated
        :return: True if the block is valid, False otherwise
        """
        if sys.getsizeof(pickle.dumps(block)) > Blockchain.MAX_BLOCK_SIZE:
            return False
        # Add more validation rules as needed
        return True
    

    def mine_block(self):
        """
        Mine a new block and add it to the blockchain.

        :return: The newly mined block
        """
        # Mine a new block using proof of work
        proof, new_block = Miner.mine(self)

        # Remove the transactions from the transaction pool
        transactions = self.transaction_pool.fetch_transactions(Blockchain.MAX_TRANSACTIONS_PER_BLOCK)
        self.new_block(proof, transactions=transactions)
        return new_block
    

    def new_transaction(self, transaction_type, sender, recipient, password_info):
        """
        Add a new transaction to the list of transactions.

        :param transaction_type: Type of transaction (e.g., "create", "update", "delete", "access")
        :param sender: Address of the sender (user ID or public key)
        :param recipient: Address of the recipient (e.g., password manager)
        :param password_info: Information related to the password
        :return: The index of the block that will hold this transaction
        """
        self.transaction_pool.add_transaction(sender, recipient, transaction_type, password_info)

        # If the transaction pool exceeds the maximum transactions per block, mine a new block
        if len(self.last_block.transactions) >= Blockchain.MAX_TRANSACTIONS_PER_BLOCK:
            print(transaction_type)
            return self.mine_block().index
            
    
    def retrieve_user_data(self, user_id, website):
        """
        Retrieve encrypted password data for a specific user and website

        :param user_id: User's unique identifier (e.g., user ID)
        :param website: Website associated with the password
        :return: Encrypted password data
        """
        encrypted_data_list = []
        for block in self.chain:
            for transaction in block.transactions:
                if transaction["recipient"] == "password_manager" and \
                        transaction["sender"] == user_id and \
                        transaction["password_info"]["website"] == website:
                    encrypted_data_list.append(transaction["password_info"])

        return encrypted_data_list
    
    @staticmethod
    def hash(block):
        block_string = json.dumps(block.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
    
    def to_dict(self):
        """
        Convert the blockchain and related data to a dictionary.

        :return: Dictionary representation of the blockchain
        """
        blocks = [block.to_dict() for block in self.chain]
        return {
            'chain': blocks,
            'transaction_pool': self.transaction_pool.to_dict(),
            'max_block_size': self.MAX_BLOCK_SIZE,
            'max_transactions_per_block': self.MAX_TRANSACTIONS_PER_BLOCK
        }
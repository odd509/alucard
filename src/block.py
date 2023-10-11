import hashlib
import json
from time import time


class Block:
    def __init__(self, index, timestamp, transactions, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def to_dict(self):
        """
        Convert the block to a dictionary

        :return: Dictionary representation of the block
        """
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "proof": self.proof,
            "previous_hash": self.previous_hash
        }

    def hash(self):
        """
        Compute the hash of the block

        :return: Hash of the block
        """
        block_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


# Example usage
if __name__ == "__main__":
    # Create a sample block
    block = Block(index=1, timestamp=time(), transactions=[], proof=123, previous_hash='abc123')

    # Display block details
    print("Block Index:", block.index)
    print("Block Hash:", block.hash())

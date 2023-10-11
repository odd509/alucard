import hashlib


class Miner:
    @staticmethod
    def mine(blockchain, difficulty=4):
        """
        Mine a new block for the blockchain using proof of work

        :param blockchain: The blockchain
        :param difficulty: The number of leading zeros required for a valid proof
        :return: The proof and the new block
        """
        last_block = blockchain.last_block
        last_proof = last_block.proof
        new_proof = 0

        while not Miner.is_valid_proof(last_proof, new_proof, difficulty):
            new_proof += 1
        print()
        return new_proof, blockchain.new_block(new_proof)

    @staticmethod
    def is_valid_proof(last_proof, new_proof, difficulty):
        """
        Check if a proof is valid by verifying the leading zeros

        :param last_proof: The previous proof
        :param new_proof: The new proof to be validated
        :param difficulty: The number of leading zeros required for a valid proof
        :return: True if the proof is valid, False otherwise
        """

        proof=hashlib.sha256(f"{last_proof}{new_proof}".encode()).hexdigest()
        print("Trying proof hash:", proof, end="\r")
        return proof[:difficulty] == '0' * difficulty

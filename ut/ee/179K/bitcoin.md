# Bitcoin Whitepaper Notes

- In a transaction, hash created using previous transaction and public key of next owner
- In order to avoid double-spend, everyone must be aware of all transactions
- **Proof of work**: Once the block hash is given the required amount of 0 bits, the block is added to the chain, and all previous blocks become immutable
  - Based off of CPU power, not # of IPs consensus
  - Difficulty is adjusted continually based on the number of new blocks being generated

## Network Process

1. New transactions broadcast to all nodes
2. Each node collects new transactions onto a block
3. Each node works on finding difficult proof-of-work hash for its block
4. When has found, broadcast block to all nodes
5. Nodes accept block if all transactions are valid and not already spent
6. Race onto the next block, using the block just created as the previous hash

In the case of a tie (multiple correct hashes broadcast) every node saves the first-received previous hash, but will save the other branch in case it becomes longer, and then will begin to work on that one if it does

## Incentive

- A new coin is created at the beginning of every block
- Once a certain number of coins have entered circulation, transaction fees can serve as the incentive to continue mining
- Someone who obtains 51% of CPU power has more of an incentive to use it to generate new coins than to defraud all previous transactions

## Reclaiming Disk Space

- Just store root hashes instead of the many hashes that go into making the root at some point in the tree

## Simplified Payment Verification

- Instead of downloading the entire blockchain, find the node in the network with the longest chain and rely on it

## Combining and Splitting Value

- Transaction allows multiple in and multiple out rather than keeping track of every "cent"

## Privacy

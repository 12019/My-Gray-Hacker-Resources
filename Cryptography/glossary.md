
# Cryptography Glossary

* Block Chaining (CBC): the only appropriate fixed-block cipher in use. If performs an XOR operation with the previous block of data.

* Stream Ciphers: block ciphers can run in modes that allow them to operate arbitrary size chunks of data. The counter CTR mode cipher is the best choice for a stream cipher.

* Initialization Vector: is a dummy block used to start a block cipher. It's necessary to force the cipher to produce a unique stream of output. It doesn't need to be kept private but it must be different for every new cipher initialization with the same key.

* Standard key exchange protocol: RSA, Diffie-Hellman, El Gamal.

* Symmetric encryption (shared key encryption): all authorized parties have the same key. It has no means for verifying the sender of a message among any group of shared key users.

* Asymmetric encryption (public key encryption): each party has a different set of keys for accessing the same encrypted data.

* Hash functions: accepts a variable-length input and generates a fixed-sized output. It must be non-reversible and should have no collisions. The simplest forms are the cyclic redundancy check (CRC) and the cryptographic hash functions (SHA-1, SHA-256, MD5).

* Salt: random value added to a message so that two messages don't generate the same hash value. It must not be duplicated between messages. It must be stored in addition to the hash so that the digest can be reconstructed. It must be protected. A salt of 23 buts increase of the password pre-computation dictionary by 4bi times (2^32).

* Rainbow tables: example of how a lack of  salt value leaves password hashes vulnerable to pre-computation attacks.

* Hash-based message authentication code (HMAC): It's an originator validation, it validates the source of a message by incorporating some form of private key into the hash operation. Same weakness of any shared key system.

* Cryptographic signature: associating a message digest with a specific public key by encrypting the message digest with the sender's public and private key.

* Bait-and-switch attack: weakness found in an aging hash function. The attacker takes advantage of a weak hash function's tendency to generate collisions over certain ranges of input. By doing this, an attacker can create two inputs that generate the same value.

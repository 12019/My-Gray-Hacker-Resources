# Cryptography



## MD5


### Scripts

- Hash length extension attack
- Brute force hex digest chars



------

## SHA


### Scripts
- SHA-256 brute force


--------

## Rotation Ciphers


### Scripts
- Caesar
- Brute force rotation
- Pygenere
- Frequency analysis


### Online tools:

- Frequency analysis: [here](http://www.simonsingh.net/The_Black_Chamber/hintsandtips.html) and [here](http://www.xarg.org/tools/caesar-cipher)

### In the command line

```sh
$ VAR=$(cat data.txt)
$ echo "$VAR"
$ alias rot13="tr A-Za-z N-ZA-Mn-za-m"
$ echo "$VAR" | rot13
```
### In Python

In Python [we can use decoding](https://docs.python.org/2/library/codecs.html#codec-base-classes): 

```python
"YRIRY GJB CNFFJBEQ EBGGRA".decode(encoding="ROT13")
```
----

## Pailier Cryptosystem

### Scripts

- POC
- Primes

---

## Tools

### Scripts:

- Finding GDC
- Finding if prime
- Generate prime
- Quick Select
- XORtool


### Online

- [Cryptol](https://www.cryptool.org/en/cryptool1-en)

-----


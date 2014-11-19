# Cryptography



## MD5

- The MD5 hashing algorithm always returns 128 bit values, so the chance that two randomly chosen objects have the same hash is 1:2**128.

### Scripts

- Hash length extension attack
- Brute force hex digest chars


### Command Line
```
$ echo -n password | md5sum
5f4dcc3b5aa765d61d8327deb882cf99
```

- 32 chars

```
7e1321b3c8423b30c1cb077a2e3ac4f0a2a551a6458a8de22446cc76d639a9e98fc42c6cddf9966db3b09e843650343578b04d5e377d298e78455efc5ca404d5f4c9385f1902f7334b00b9b4ecd164de8bf8854bebe108183caeb845c7676ae48fc42c6ddf9966db3b09e84365034357327a6c4304ad5938eaf0efb6cc3e53dc7ff9ea9a069bd793691c422fb818
```

- Use Python's md5.md5().digest()

- md5 hashes: [here](http://hash-killer.com/) and [here](http://www.md5this.com/)


------

## SHA

- SHA-1 has output size of 160 bits, so chances of collisions are 2**160.

### Scripts
- SHA-256 brute force


### Command Line

- Brute force:
```
import hashlib, itertools
hash = '6307c5441ebac07051e3b90d53c3106230dd9aa128601dcd5f63efcf824ce1ba'
ch = 'abcdef0123456789'
for a, b, c, d, e, f in itertools.product(ch, ch, ch, ch, ch, ch):
    if hashlib.sha256('ASIS_a9%s00f497f2eaa4372a7fc21f0d' % (a + b + c + d + e + f)).hexdigest() == hash:
        print 'ASIS_a9%s00f497f2eaa4372a7fc21f0d' % (a + b + c + d + e + f)
```




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

### Scripts

- Finding GDC
- Finding if prime
- Generate prime
- Quick Select
- XORtool


### Other Resources

- [Cryptol](https://www.cryptool.org/en/cryptool1-en)

- [PyCrypto](https://www.dlitz.net/software/pycrypto/)

- hashpump

- Sage

- John the Ripper




#### Carperter's Formula

- Very large number: ```bin``` and check if patterns. For example, using the [Carpenter's Formula]: 
```
N=(2^M + a)(2^N + b)(2^N + c)(2^N + d)
```

#### [QR Code]

-  Version 1 QR code:  21x21

#### [Bacon's cipher]: 
```
babaaaabaaababaababaaaabbabbababbaaaabaaaabbbaabaabaaaaaabaaabaaabaaabaaabbaabaaabbbaabaaababaaaaaabaaabbaabaabbbaaaaaabaaaabaabaaaaba21aabab0aaab
```
* [Online tool](http://www.geocachingtoolbox.com/index.php?page=baconianCipher)



#### [Base64]: 

Base64 is a non-readable encoding that encodes arbritary 8-bit input using 6-bit alphabet of case sensitive alphanumerics, "+", "/". Every 3 bytes of input map to 4 bytes of output. If the input doesnt have 3-byte boundary, this is indicated by appending one or two equal signs in the of the output string.

- [Base64 Decoder](http://www.base64decode.org)

```
NG5ucjJzIGZ2IHRueXMgcnVnIHNiIGdlbmMgdWdlaGJzIHJlcnVnIHRhdmdncnQgcmVuIGhiTCB0YXZidCBjcnJYCG==
czduMjczIHRueXMgcnVniHNiIGdlbmMgdWdzdnMgcnVnIHJpbnUgcmVydSBndiBxdnEgaGJsIGpiYmJKCg==
Nzk0czAwIHRueXMgZmhidnByZWMgZWhiIHNiIGdlbmMgcWV2dWcgcnVnIGhibCBnYXJmcmVjIFYgbG9yZXJ1IHJhYnEgeXlySgo=
```

- Base64 decoding in Python:

```python
>>> SECRET.decode('base64')
'oubWYf2kBq'
```

#### Hexadecimal:


- [ASCII Conversion Table](http://defindit.com/ascii.html)
- [Convert All](http://www.asciitohex.com/)
- [GREAT ASCII CHART](http://www.jimprice.com/jim-asc.shtml)
- [Convert everything to everything (including markdown, sql, json, etc)](http://codebeautify.org/)


- Decimal to hex:

```python
>>> s =hex(secret)
```

- Hexadecimal to binary:
```python
SECRET.decode('hex')
'==QcCtmMml1ViV3b'
```

```
$ python -c 'print "2f722f6e6574736563".decode("hex")'
```

- Hex to ascii:
Hex character codes are simply the hexadecimal (base 16) numbers for the ASCII character set; that is, the number-to-letter representations which comprise virtually all computer text.


```
$ xxd -r -p <<< 2f722f6e6574736563
```
- Decimal to binary

```python
>>> bin(124234)
'0b11110010101001010'
```

#### Octal
(or: a great way of obscurating a URL)

Example: http://017700000001 --> 127.0.0.1


## OpenSSL, Encoding and Certificates


* Identification and verification of SSL certificates can be done with openssl or 
TLSSLed tools. They allow us to verify this information automatically SSL.

To determine the period of validity of licenses:

```
$ ./openssl s_client --connect <WEBSITE>:443
```

Testing SSLv2:
```
$ ./openssl s_client --no_tls1 --no_ssl3 --connect <WEBSITE>:443
```

* For Identification and verification of encoding supported by the Website we can use  **EcoScan34**.






[SHA]:http://en.wikipedia.org/wiki/Secure_Hash_Algorithm
[MD5]: http://en.wikipedia.org/wiki/MD5
[Base64]: http://en.wikipedia.org/wiki/Base64
[Bacon's cipher]:http://en.wikipedia.org/wiki/Bacon's_ciphe
[Carpenter's Formula]:http://security.cs.pub.ro/hexcellents/wiki/writeups/asis_rsang
[pngcheck]: http://www.libpng.org/pub/png/apps/pngcheck.html
[karmadecay]: http://karmadecay.com/
[tineye]:  https://www.tineye.com/
[images.google.com]: https://images.google.com/?gws_rd=ssl
[base64 decoding]: http://www.motobit.com/util/base64-decoder-encoder.asp
[pnginfo]: http://www.stillhq.com/pngtools/
[namechk]: http://namechk.com
[QR Code]: http://en.wikipedia.org/wiki/QR_code


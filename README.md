# My-Gray-Hacker-Resources

All in one big bag. For fun, profits, or CTFs.


## * CTFs and WARGAMES
## * CRYPTOGRAPHY
## * FORENSICS
## * LINUX HACKING
## * MEMORY EXPLOITS
## * NETWORK and 802.11
## * REVERSE ENGINEERING
## * RUBBER DUCK
## * STEGANOGRAPHY
## * WEB EXPLOITS
## * OTHER HACKINGS




![](http://i.imgur.com/4WNqTJS.png)


---- 

### Useful

#### Searching
 
 
```
grep word f1
 
sort | uniq -c
 
diff f1 f2
 
find -size f1
```
 


 
#### Compressed Files
 
 
```
zcat f1 > f2
 
gzip -d file
 
bzip2 -d f1
 
tar -xvf file
```
 
 
 
#### Connecting to a Server/Port
 
```
echo 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e | nc localhost 30000
 
openssl s_client -connect localhost:30001 -quiet
 
nmap -p 31000-32000 localhost
 
telnet localhost 3000
```
 


#### Decoders

[Base64](http://www.base64decode.org)

[ASCII Conversion Table](http://defindit.com/ascii.html)

[Convert All](http://www.asciitohex.com/)


- In Python:

- Decimal to binary

```python
>>> bin(124234)
'0b11110010101001010'
```

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

```
$ xxd -r -p <<< 2f722f6e6574736563
```

- Base64 decode:

```python
>>> SECRET.decode('base64')
'oubWYf2kBq'
```

- md5 hashes
http://hash-killer.com/
http://www.md5this.com/

----



### Recon



#### Searching the Internets

The recon problems usually give you someone/something's name and a task or a hint to find some specific information about it. So the first thing is of course google it.

Google anything using keywords such as ```filetype:cgi inurl:cgi-bin```


#### In addition we can look at:

- Facebook, Twitter, Linkedin, Google+, reddit,  /r/netsec.
- IRC: with **/whois **.
- [namechk] 
- Github: check in the commit history.


#### Finding pictures:

- [karmadecay]
- [tineye]
- [images.google.com]



-----------------
[FireBug]: http://getfirebug.com/
[Burp Suite]: http://portswigger.net/burp/
[pngcheck]: http://www.libpng.org/pub/png/apps/pngcheck.html
[karmadecay]: http://karmadecay.com/
[tineye]:  https://www.tineye.com/
[images.google.com]: https://images.google.com/?gws_rd=ssl
[base64 decoding]: http://www.motobit.com/util/base64-decoder-encoder.asp
[subbrute.py]: https://github.com/SparkleHearts/subbrute
[pnginfo]: http://www.stillhq.com/pngtools/
[namechk]: http://namechk.com


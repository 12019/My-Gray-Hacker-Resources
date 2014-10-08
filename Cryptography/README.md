# TOOLS:

- https://www.cryptool.org/en/cryptool1-en

- frequency analyses online: 
http://www.simonsingh.net/The_Black_Chamber/hintsandtips.html
http://www.xarg.org/tools/caesar-cipher/


## ROT13

In the command line
```
VAR=$(cat data.txt)
echo "$VAR"
alias rot13="tr A-Za-z N-ZA-Mn-za-m"
echo "$VAR" | rot13
```
----


In Python we can use: ```"YRIRY GJB CNFFJBEQ EBGGRA".decode(encoding="ROT13")```
https://docs.python.org/2/library/codecs.html#codec-base-classes

---

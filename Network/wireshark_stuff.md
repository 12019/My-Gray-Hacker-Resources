#

## Recon

* Statistics -> Conversations
	-> Some SSH, HTTP


## Filters
* Filer on HTTP:

```
ip.addr==172.16.133.133 && tcp.port==52694 && ip.addr==172.16.133.149 && tcp.port==80
```

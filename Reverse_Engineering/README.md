# Reverse Engineering


## Tools Folder

- X86 Win32 Cheat sheet
- Intro X86
- base conversion
- Command line tricks



## Other Tools

- gdb
- IDA Pro
- Immunity Debugger
- OllyDbg
- Radare2
- nm
- objdump
- strace
- ILSpy (.NET)
- JD-GUI (Java)
- FFDec (Flash)
- dex2jar (Android)
- uncompyle2 (Python)
- unpackers, hex editors, compilers


## Encondings/ Binaries
 
```
file f1
 
ltrace bin
 
strings f1
 
base64 -d
 
xxd -r

nm

objcopy

binutils
```
 
 



## Online References

[Reverse Engineering, the Book]: http://beginners.re/



## IDA

- Cheat sheet
- [IDA PRO](https://www.hex-rays.com/products/ida/support/download_freeware.shtml)




## gdb

- Commands and cheat sheet


```sh
$ gcc -ggdb -o <filename> <filename>.c

```

Starting with some commands:
```sh
$ gdb <program name> -x <command file>
```

For example:
```sh
$ cat command.txt
set disassembly-flavor intel
disas main
```


## objdump 

Display information from object files: Where object file can be an intermediate file
created during compilation but before linking, or a fully linked executable

```sh
$ objdump -d  <bin>
```

## hexdump & xxd

For canonical hex & ASCII view:
```
$hexdump -C 
```

## xxd 
Make a hexdump or do the reverse:
```
xxd hello > hello.dump
xxd -r hello.dump > hello
```

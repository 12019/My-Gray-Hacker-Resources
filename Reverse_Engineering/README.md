# Tools

[Reverse Engineering, the Book]: http://beginners.re/


# Dissasembly


#### gdb
```
$ gcc -ggdb -o <filename> <filename>.c

```

Starting with some commands:
```
$ gdb <program name> -x <command file>
```

For example:
```
$ cat command.txt
```
set disassembly-flavor intel
disas main
```


#### objdump 

Display information from object files:
•  Where object file can be an intermediate file
created during compilation but before linking, or a
fully linked executable

```
$ objdump -d  <bin>
```

#### hexdump & xxd

For canonical hex & ASCII view:
```
$hexdump -C 
```

#### xxd 
Make a hexdump or do the reverse:
```
xxd hello > hello.dump
xxd -r hello.dump > hello
```

# Tools

[Reverse Engineering, the Book]: http://beginners.re/


# Dissasembly


#### gdb
```
$ gcc -ggdb -o <filename> <filename>.c

```

#### objdump 

Display information from object files:
•  Where object file can be an intermediate file
created during compilation but before linking, or a
fully linked executable

```
$ objdump -d  <bin>
```


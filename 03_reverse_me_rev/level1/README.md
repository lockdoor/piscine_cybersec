1. Use gdb to debuging the program
```
gdb ./level1
```

2. Use disassembly main to read code in main function (entry point) as assembly code
```
disas main
```

3. Add break point to *main+124
```
b *main+124
```

4. Run debuging
```
r
```

5. When it promtp "Please enter key:", enter key then the program will break

6. disassembly again it show address of strcmp function, the assembly code prepare two value as argument to use in strcmp eg. edx and ecx we can see string value like this
```
x/s $edx 
x/s $ecx
```
7. $edx and $ecx , one for secret password one for your input password
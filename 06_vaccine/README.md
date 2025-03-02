# VACCINE

This project is path of Piscine cyber-security of 42Bangkok.

I make server with Fastapi and contain 3 type database mysql, postgres, sqlite.

Becouse this is project for learn I don't store credential in ENV.

To initial server and vaccine
```
make
```
To run vaccine
```
make run
```

To use vacine
```
./vacine http://fastapi:800
```

Parameter
- -X --method // post, head default get
- -o --output // output file .tar
- -H --header // can add header for request eg: header=value

I write Makefile for sample command in vaccine src directory.

## Cradit
[invicti](https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/) have a lot of ton to learn how to sql injection

[viruskizz](https://github.com/viruskizz/42bangkok-cybersecurity-piscine) I get concept form him, thank you so much.

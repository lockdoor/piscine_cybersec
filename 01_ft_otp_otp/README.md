# FT_OTP

[RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238)

Hash Message Authtication Code [HMAC](https://en.wikipedia.org/wiki/HMAC)

[HOTP](https://datatracker.ietf.org/doc/html/rfc4226)

OTP gennerator(client), OTP validator(server)

https://www.youtube.com/watch?v=XYVrnZK5MAU

[Two-Factor Authentication (2FA) in Python](https://www.youtube.com/watch?v=o0XZZkI69E8)

[How Hackers Bypass Two-Factor Authentication (2FA)?!](https://www.youtube.com/watch?v=e8KZTCM2B8Q)

[How Does SHA-1 Work - Intro to Cryptographic Hash Functions and SHA-1](https://www.youtube.com/watch?v=kmHojGMUn0Q)

| Algorithm | Output Length (Bits) | Output Length (Bytes) | Hexadecimal String Length |
| --- | --- | --- | --- |
| SHA-1	| 160 bits |	20 bytes |	40 characters (hex) |
| SHA-256 |	256 bits |	32 bytes |	64 characters (hex) |

for *.hex can use
```
echo -n $(echo hello |  sha256) > somefile.txt
```
or
```
echo -n hello1 | openssl sha256 -hex | awk '{printf "%s", $2}' > somefile.txt
```

This project not require third-party library

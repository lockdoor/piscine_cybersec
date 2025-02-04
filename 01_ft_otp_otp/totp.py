import time
import pyotp

# base32 secret key for pyotp required
# key = "JBSWY3DPEHPK3PXP"
# key = "JBSWY3DPEHPK3PXPUUII3XQK3PXPH" # len = 29
key = "JBSWY3DPEHPK3PXPUUII3XQK3PXPHX" # len = 30
# key = "JB1"

# totp = pyotp.TOTP(key)

# hotp = pyotp.HOTP(key)

# for i in range(10):
#     # print(totp.now())
#     print(f'{i}: {hotp.at(i)}')
#     time.sleep(3)
# print(hotp.provisioning_uri(name="test", issuer_name="test"))
# print(hotp.verify("143627", 4))

def test1():
    try:
        with open("test_keys/success.hex", "r") as f:
            key = f.read()
        hotp = pyotp.HOTP(key)
        for i in range(5):
            print(f'{i}: {hotp.at(i)}')
            time.sleep(1)
    except Exception as e:
        print(e)

def test2():
    try:
        hotp = pyotp.HOTP(key)
        for i in range(5):
            value = hotp.at(i)
            print(f'{i}: {value}')
            time.sleep(1)
    except Exception as e:
        print(e)

def test3():
    try:
        hotp = pyotp.HOTP(key)
        print (f'secret: {key}, len: {len(key)}')
        print(hotp.provisioning_uri(name="test", issuer_name="test"))     
    except Exception as e:
        print(e)

if __name__ == "__main__":
    # test1()
    test2()
    test3()

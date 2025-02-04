import argparse
import re
import hashlib
import base64
import hmac
import time
import struct

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate OTP key')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-g', type=str, help='File text to hash as key')
    group.add_argument('-k', type=str, help='File Key to generate OTP')
    return parser.parse_args()

def is_hexadecimal(s: str) -> bool:
    return bool(re.fullmatch(r'^[0-9a-fA-F]+$', s))

def generate_key(key: str) -> None:
    try:
        with open(key, 'r') as f:
            data = f.read()
        # Step 1: Check if the key is hexadecimal and more than 64 characters
        if not is_hexadecimal(data) or len(data) < 64:
            raise ValueError("Key must be hexadecimal")
        
        # Step 2: Compute SHA-265 hash
        sha265_hash = hashlib.sha256(data.encode('utf-8')).digest()
        # print(sha265_hash)

        # Step 3: encode hash as base32
        base32_hash = base64.b32encode(sha265_hash).decode('utf-8').rstrip('=')[:29]
        # print(base32_hash)

        # Step 4: Write base32 hash to file
        with open('key.hex', 'w') as f:
            f.write(base32_hash[:16])

    except Exception as e:
        print(f"Error: {e}")

# generate TOTP from base32 key
def generate_otp(file: str) -> None:
    try:
        with open(file, 'r') as f:
            secret = f.read()
        
        # Step 1: Get the current time step (30 seconds interval)
        time_step = int(time.time()) // 30 # floor division
        # print(1, time_step)

        # Step 2: Convert the time step to an 8-byte counter (big-endian)
        time_step_bytes = struct.pack('>Q', time_step) # > = big-endian, Q = unsigned long long
        # print(2, time_step_bytes)

        # Step 3: Decode the base32 secret (OTP standard uses base32) 
        key = base64.b32decode(secret.upper() + "=" * ((8 - len(secret) % 8) % 8))
        # print(3, key)

        # Step 4: Generate HMAC-SHA1 20 byte (160 block of bit) digest
        hmac_digest = hmac.new(key, time_step_bytes, hashlib.sha1).digest()
        print(4.1, f'len: {len(hmac_digest)}, {hmac_digest}')
        for i in hmac_digest:
            print(i, end=' ')
        print()
        # print(4.2, hmac_digest.hex())

        # Step 5: Extract dynamic offset from last byte ( it return random index 0 - 15)
        print(5.1, hmac_digest[-1])
        offset = hmac_digest[-1] & 0x0F
        print(5.2, offset)
        binary_code = struct.unpack(">I", hmac_digest[offset:offset + 4])[0] & 0x7FFFFFFF  # 31-bit integer
        print(5.3, struct.unpack(">I", hmac_digest[offset:offset + 4]))
        print(5.4, struct.unpack(">I", hmac_digest[offset:offset + 4])[0])

        # Step 6: Get the final OTP (6 or more digits)
        otp = str(binary_code % (10 ** 6)).zfill(6)
        print(otp)
        return otp


    except Exception as e:
        print(f"Error: {e}")

    pass

if __name__ == '__main__':
    args = parse_args()
    if args.g:
        generate_key(args.g)
    else:
        # while True:
        #     generate_otp(args.k)
        #     time.sleep(30)

        generate_otp(args.k)

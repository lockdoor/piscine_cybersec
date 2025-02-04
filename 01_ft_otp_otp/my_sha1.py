def sha1(text: str) -> str:
    # 1. Convert string to bytes
    # ascii = [ord(c) for c in text]
    ascii = bytearray(text, 'utf-8') # [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]

    # 2. Convert bytes to binary and pad to 8 bits
    binary = [format(byte, '08b') for byte in ascii]
    # print (binary)  # 0100100001100101011011000110110001101111001000000010111101101111011100100110110001100100

    # 3. join binary list into a single string
    binary_str: str = ''.join(binary)
    # print(binary_str)  # 0100100001100101011011000110110001101111001000000010111101101111011100100110110001100100

    # 4. Append a single '1' bit
    binary_str += '1'

    # 5. Pad with '0' bits until length is 448 bits (56 bytes)
    while len(binary_str) % 512 != 448:
        binary_str += '0'
    
    print(len(binary_str))  # 448
    print(binary_str)  # 010010000110010101101100011011000110111100100000001011110110111101110010011011000110010

    # 6. Append the original message length as a 64-bit binary string





if __name__ == '__main__':
    sha1("A Test")
    # print(sha1("Hello, World!"))  # 2ef7bde608ce5404e97d5f042f95f89f1c232871
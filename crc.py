def xor(a, b):
    """Performs XOR operation between two binary strings."""
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    """Performs Modulo-2 division for CRC."""
    pick = len(divisor)
    tmp = dividend[:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def encode_crc(data, key):
    """Generates CRC code by appending remainder to the data."""
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

def verify_crc(received, key):
    """Checks the received data using the same CRC divisor."""
    remainder = mod2div(received, key)
    return remainder == '0' * (len(key) - 1)

# Get input from the user
data = input("Enter the binary data (message) to be transmitted: ")
key = input("Enter the generator polynomial (binary): ")

# Encode the data
print("\nOriginal Data: ", data)
encoded_data = encode_crc(data, key)
print("Encoded Data (with CRC): ", encoded_data)

# Simulate transmission (user can optionally introduce an error)
received_data = input(f"\nEnter the received data (default: {encoded_data}): ")
if not received_data:
    received_data = encoded_data  # No changes if user just presses enter

# Verify the received data
if verify_crc(received_data, key):
    print("No error detected, CRC passed.")
else:
    print("Error detected, CRC failed.")

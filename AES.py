def xor_byte(data,key):
    return bytes(a ^ b for a, b in zip(data,key))

def pad(data):
    block_size = 16
    padding_length = block_size - (len(data) % block_size)
    
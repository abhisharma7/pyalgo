def count_bits(num):
    bit_count = 0
    while num:
        bit_count += num & 1
        num >>= 1
    return bit_count
import struct

def fast_inverse_square_root(number):
    threehalfs = 1.5

    x2 = number * 0.5
    y = number

    packed_y = struct.pack('f', y)              # pack the float into 4 bytes
    i = struct.unpack('i', packed_y)[0]         # interpret the bytes as an integer
    i = 0x5f3759df - (i >> 1)                   # magic constant and bit shift
    packed_i = struct.pack('i', i)              # pack the integer back into 4 bytes
    y = struct.unpack('f', packed_i)[0]         # unpack as float

    y = y * (threehalfs - (x2 * y * y))         # Newton's method iteration

    return y
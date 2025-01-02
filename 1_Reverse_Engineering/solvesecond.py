import itertools

table = [
    0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38,
    0x39, 0x30, 0x71, 0x77, 0x65, 0x72, 0x74, 0x79,
    0x75, 0x69, 0x6F, 0x70, 0x61, 0x73, 0x64, 0x66,
    0x67, 0x68, 0x6A, 0x6B, 0x6C, 0x7A, 0x78, 0x63,
    0x76, 0x62, 0x6E, 0x6D, 0x51, 0x57, 0x45, 0x52,
    0x54, 0x59, 0x55, 0x49, 0x4F, 0x50, 0x41, 0x53,
    0x44, 0x46, 0x48, 0x4A, 0x4B, 0x4C, 0x5A, 0x58,
    0x43, 0x56, 0x42, 0x4E, 0x4D, 0x2D, 0x2B, 0x2F
]

result = 'xw0t'
characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for sa in itertools.product(characters, repeat=4):
    sa = ''.join(sa)
    try:
        v = [0]*8
        v11 = 5
        v[4] = table[(ord(sa[0]) >> 2) & 0x3F]
        for j in range(1, 4):
            v5 = v11
            v11 += 1
            v[v5] = table[((ord(sa[j]) >> 2) ^ (ord(sa[j-1]) >> 2)) & 0x3F]
        computed = ''.join(chr(v[i]) for i in range(4,8))
        if computed == result:
            print(f'{sa}')
    except:
        continue
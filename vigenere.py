def Encrypt (plaintext, key):
    dictt={"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8,"j":9,
           "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19,
           "u":20, "v":21, "w":22, "x":23, "y":24, "z":25
           }
    ciphertext = " "
    if (len(plaintext) > len (key)):
        n = len(plaintext) - len (key)
        for i in range (0,n):
            key = key + key[i]
    for p, k in zip (plaintext, key):
        c = (dictt[p] + dictt[k]) %26
        for v,k in dictt.items():
            if c == k :
                ciphertext = (ciphertext + v).upper()
    return ciphertext


def Decrypt(ciphertext, key):
    dictt={"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8,"j":9,
           "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19,
           "u":20, "v":21, "w":22, "x":23, "y":24, "z":25
           }
    plaintext = " "
    ciphertext = ciphertext.lower()
    if (len(ciphertext) > len (key)):
        n = len(plaintext) - len (key)
        for i in range (0,n):
            key = key + key[i]
    for p, k in zip (plaintext, key):
        c = (dictt[p] - dictt[k]) %26
        for v,k in dictt.items():
            if c == k :
                plaintext = plaintext + v
    return plaintext
def Encrypt(plantext, key):
    Ctext=" "
    dictt={"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8,"j":9,
           "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19,
           "u":20, "v":21, "w":22, "x":23, "y":24, "z":25
           }
    for x in plantext :
        c = (dictt[x] + key) %26
        for v,k in dictt.items():
            if c == k :
                Ctext = (Ctext + v).upper()
    print(Ctext)


def Decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    Ptext= " "
    dictt={"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8,"j":9,
           "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19,
           "u":20, "v":21, "w":22, "x":23, "y":24, "z":25
           }
    for x in ciphertext:
        p = (dictt[x] - key) %26
        for v,k in dictt.items():
            if p == k :
                Ptext = (Ptext + v)
    print(Ptext)
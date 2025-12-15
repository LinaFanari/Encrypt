import string
import math
def create_matrix(key):
    alphabet = string.ascii_lowercase + string.digits
    seen = set()
    temp = []
    for char in key:
        if char not in seen and char in alphabet:
            seen.add(char)
            temp.append(char)
    for char in alphabet:
        if char not in seen:
            temp.append(char)
    matrix = [[None for _ in range (7)] for _ in range (7)]
    ADFGVX = "ADFGVX"
    k = 0
    for i in range (0,7):
        for j in range (0,7):
            if (i==0 and j==0):
                matrix[i][j] = " "
            elif (i==0 and j>0):
                matrix[i][j] = ADFGVX[j-1]
            elif (i>0 and j==0):
                matrix[i][j] = ADFGVX[i-1]
            elif (i>0 and j>0):
                matrix[i][j] = temp[k]
    return (matrix)

def encrypt (text, key1, key2):
    matrix = create_matrix(key1)
    ciphertext = ' '
    for char in text:
        for i in range (7):
            for j in range (7):
                if (char == matrix[i][j]):
                    row = matrix[i][0]
                    col = matrix[0][j]
                    ciphertext += row + col
                    break
    nr = len(key2)
    ss = len(ciphertext) + nr
    nc = math.ceil(ss/nr)
    m = [[None for _ in range (nc)] for _ in range (nr)]
    fullsize = (nr*nc) - ss
    if (fullsize > 0):
        for i in range(fullsize):
            ciphertext += "A"



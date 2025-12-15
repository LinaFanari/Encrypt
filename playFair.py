def processKey (key):
    seen = set()
    res = []
    ress = ''
    matrixkey = []
    a = "abcdefghijklmnopqrstuvwxyz"
    for x in key :
        if x not in seen :
            seen.add(x)
            res.append(x)
    key = ress.join(res)

    for i in key :
        if i not in matrixkey:
            matrixkey.append(i)
    for i in a:
        if i not in matrixkey:
            matrixkey.append(i)
    matrixkey = [matrixkey[i:i + 5] for i in range(0, 25,)]


def preprocess_text(text):
    text = text.lower().replace("j", "i")
    processed = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i+1]:
            processed.append(text[i])
            processed.append('x')
            i += 1
        else:
            processed.append(text[i])
            i += 1
    if len(processed) % 2 != 0:
        processed.append('z')
    return ' '.join(processed)
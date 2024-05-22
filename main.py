def cryptagecesar(cle, txt):
    txtcrypte = []

    for i in range(len(txt)):

        a = txt[i]
        a = ord(a)

        if a > 96:

            a = a - 97
            b = ((a - cle) % 26)
            b = b + 97
            c = chr(b)
            txtcrypte.append(c)

        else:

            b = (a - cle)
            c = chr(b)
            txtcrypte.append(c)

    return ''.join(txtcrypte)


txt = tuple(input("Quel mot souhaitez-vous crypter ?"))
cle = int(input("Quel est la clé de cryptage ?"))

print(cryptagecesar(cle, txt))


def decryptagecesar(cle, txt):
    txtdecrypte = []

    for i in range(len(txt)):

        a = txt[i]
        a = ord(a)

        if a > 96:

            a = a - 97
            b = ((a + cle) % 26)
            b = b + 97
            c = chr(b)
            txtdecrypte.append(c)

        else:

            b = (a + cle)
            c = chr(b)
            txtdecrypte.append(c)

    return ''.join(txtdecrypte)


txt = tuple(input("Quel mot souhaitez-vous décrypter ?"))
cle = int(input("Quel est la clé de cryptage ?"))

print(decryptagecesar(cle, txt))
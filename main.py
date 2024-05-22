import string
alphabet = string.ascii_lowercase

def cryptagecesar(cle, txt):
    txtcrypte = []

    for i in range(len(txt)):

        a = alphabet.find(txt[i])

        if a >= 0:

            b = ((a - cle) % 26)
            c = alphabet[b]
            txtcrypte.append(c)

        else:

            txtcrypte.append(txt[i])

    return ''.join(txtcrypte)


txt = tuple(input("Quel mot souhaitez-vous crypter ?"))
cle = int(input("Quel est la clé de cryptage ?"))

print(cryptagecesar(cle, txt))


def decryptagecesar(cle, txt):
    txtdecrypte = []

    for i in range(len(txt)):

        a = alphabet.find(txt[i])

        if a >= 0:

            b = ((a + cle) % 26)
            c = alphabet[b]
            txtdecrypte.append(c)

        else:

            txtdecrypte.append(txt[i])

    return ''.join(txtdecrypte)


txt = tuple(input("Quel mot souhaitez-vous décrypter ?"))
cle = int(input("Quel est la clé de cryptage ?"))

print(decryptagecesar(cle, txt))
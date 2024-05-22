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


#txt = tuple(input("Quel mot souhaitez-vous décrypter ?"))
#cle = int(input("Quel est la clé de cryptage ?"))

#print(decryptagecesar(cle, txt))


def test_plausiblilite(texte, mots_courants):
    mots = texte.split()
    nombre_de_mots_courants = sum(1 for mot in mots if mot.lower() in mots_courants)
    return nombre_de_mots_courants >= len(mots) * 0.1  # ajustez le seuil selon les besoins

def force_brute_cesar(txtcrypte, mots_courants):
    for cle in range(26):
        texte_decrypte = decryptagecesar(cle, cryptagecesar(cle, txtcrypte))
        if test_plausiblilite(txtdecrypte, mots_courants):
            return texte_decrypte_sans_cles, cle
    return None, None

# Liste de mots courants (à étendre selon les besoins)
mots_courants = ["le", "et", "avoir", "que", "pour", "vous", "avec", "pas", "ce", "mais"]




# Déchiffrer le texte chiffré en utilisant la force brute
texte_decrypte_sans_cles, cle = force_brute_cesar(cryptagecesar(cle, txtcrypte), mots_courants)

if message_decrypte:
    print(f"Message décrypté : {texte_decrypte_sans_cles}")
    print(f"Clé : {cle}")
else:
    print("Aucun déchiffrement plausible trouvé.")
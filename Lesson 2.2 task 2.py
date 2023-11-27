import simplecrypt


with open("encrypted.bin", "rb") as file_in, open("passwords.txt", "r") as out:
    encrypted = file_in.read()
    for line in out:
        try:
            decrypted = simplecrypt.decrypt(line.strip(), encrypted).decode('utf8')
            print(decrypted)
        except simplecrypt.DecryptionException as ex:
            pass
        else:
            print(decrypted)






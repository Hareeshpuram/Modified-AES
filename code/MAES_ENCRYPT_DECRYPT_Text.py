from StdMAES import MAES
plaintext=b'thisisplaintexts'
key=b'mysecretpassword'
c=MAES(key)
cipher=c.encrypt(plaintext)
decrypted=c.decrypt(cipher)
print(f'plaintext:{plaintext}\nkey:{key}\nciphertext:{cipher}\nDecrypted text:{decrypted}')
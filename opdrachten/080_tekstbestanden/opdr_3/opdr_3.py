# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:


def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_code = ord(char) + 5
            if char.islower():
                if shifted_code > ord('z'):
                    shifted_code -= 26
            elif char.isupper():
                if shifted_code > ord('Z'):
                    shifted_code -= 26
            encrypted_text += chr(shifted_code)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_code = ord(char) - 5
            if char.islower():
                if shifted_code < ord('a'):
                    shifted_code += 26
            elif char.isupper():
                if shifted_code < ord('A'):
                    shifted_code += 26
            decrypted_text += chr(shifted_code)
        else:
            decrypted_text += char
    return decrypted_text

text = input("Geef je tekst aan die je wilt encrypten: ")
encrypt_text = encrypt(text)
print("Versleute;lde tekst:", encrypt_text)

decrypted_text = decrypt(encrypt_text)
print("Originele tekst:", decrypted_text)
    

def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_stream = [ord(key[i % len(key)]) for i in range(len(plaintext))]
    
    for i in range(len(plaintext)):
        encrypted_text += chr(ord(plaintext[i]) ^ key_stream[i])
    
    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_stream = [ord(key[i % len(key)]) for i in range(len(ciphertext))]
    
    for i in range(len(ciphertext)):
        decrypted_text += chr(ord(ciphertext[i]) ^ key_stream[i])
    
    return decrypted_text

def main():
    plaintext = input("Masukkan plaintext: ")
    key = input("Masukkan kunci (lebih dari 5 karakter): ")

    if len(key) <= 5:
        print("Panjang kunci harus lebih dari 5 karakter.")
        return

    encrypted_text = vigenere_encrypt(plaintext, key)
    decrypted_text = vigenere_decrypt(encrypted_text, key)

    print("\nHasil Enkripsi:")
    print("Ciphertext:", encrypted_text)

    print("\nHasil Dekripsi:")
    print("Plaintext:", decrypted_text)

if __name__ == "__main__":
    main()

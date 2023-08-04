# test_encryption_service.py

import requests

def test_encryption_service():
    # Replace the URL with the actual URL of the encryption service running
    encrypt_url = 'http://127.0.0.1:9001/encrypt'
    decrypt_url = 'http://127.0.0.1:9001/decrypt'
    key = "SecretKey"

    # Test data
    password = "SecretPassword123!"

    # Make an HTTP POST request to encrypt the password
    encrypt_data = {'password': password, 'key': key}
    encrypt_response = requests.post(encrypt_url, json=encrypt_data)

    if encrypt_response.status_code == 200:
        encrypted_password = encrypt_response.json()['encrypted_password']
        print("Encrypted Password:", encrypted_password)

        # Make an HTTP POST request to decrypt the password
        decrypt_data = {'encrypted_password': encrypted_password, 'key': key}
        decrypt_response = requests.post(decrypt_url, json=decrypt_data)

        if decrypt_response.status_code == 200:
            decrypted_password = decrypt_response.json()['decrypted_password']
            print("Decrypted Password:", decrypted_password)

            # Check if decryption is successful
            assert decrypted_password == password, "Decryption failed."
            print("Encryption and Decryption test passed!")
            
            # Check if the decrypted password matches the original password
            if password == decrypted_password:
                print("Password and Decrypted Password are the same.")
            else:
                print("Password and Decrypted Password are different.")

        else:
            print("Error in decryption response:", decrypt_response.text)

    else:
        print("Error in encryption response:", encrypt_response.text)


if __name__ == "__main__":
    test_encryption_service()






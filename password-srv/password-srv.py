# Microservice that takes commands/inputs from password-srv.txt
import requests
import time
import json
import string
import random
import re

from flask import Flask, request, jsonify
app = Flask(__name__)

PASSWORD_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/password-srv.txt"
RESULT_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/result.txt"

SORTED_COMPROMISED_PWORDS = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/password-srv/sorted_compromised_passwords.json"
SORTED_COMMON_PWORDS = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/password-srv/sorted_common_passwords.json"

ENCRYPTION_SERVICE_URL = 'http://127.0.0.1:9001/encrypt'
DECRYPTION_SERVICE_URL = 'http://127.0.0.1:9001/decrypt'
SECRET_KEY = "SecretKey"

# def runSRV():
#     while True:
#         # Sleep for 1 second
#         time.sleep(1)

#         # open password file and get contents
#         pword_file = open(PASSWORD_PATH, "r")
#         line = pword_file.read()

#         # If file is blank
#         if line == '' or line == ' ':
#             continue

#         # Compromised Password Check
#         if line.startswith("compromised-password-check"):
#             line = line.replace("compromised-password-check ", "")

#             # Decrypt the password before performing checks
#             decrypted_password = decrypt_password(line, SECRET_KEY)
#             if decrypted_password is None:
#                 continue
            
#             # Pass password to compromised check
#             compromised_check = password_check(SORTED_COMPROMISED_PWORDS, decrypted_password)
            
#             if compromised_check == True:
#                 result = "The entered password is compromised! Change your password immediately!"
#             else:
#                 result = "Password is safe."

#             clearAndSend(result)

#         # Common Password Check
#         elif line.startswith("common-password-check"):
#             line = line.replace("common-password-check ", "")
            
#             # Decrypt the password before performing checks
#             decrypted_password = decrypt_password(line, SECRET_KEY)
#             if decrypted_password is None:
#                 continue
            
#             # Pass password to common check
#             common_check = password_check(SORTED_COMMON_PWORDS, decrypted_password)
            
#             if common_check:
#                 result = "The entered password is commonly used! Please choose a stronger password."
#             else:
#                 result = "Password is safe."

#             clearAndSend(result)

#         # Combined Check (Compromised and Common)
#         elif line.startswith("combined-check"):
#             line = line.replace("combined-check ", "")

#             # Decrypt the password before performing checks
#             decrypted_password = decrypt_password(line, SECRET_KEY)
#             if decrypted_password is None:
#                 continue

#             # Pass password to both password checks
#             compromised_check = password_check(SORTED_COMPROMISED_PWORDS, decrypted_password)
#             common_check = password_check(SORTED_COMMON_PWORDS, decrypted_password)

#             if compromised_check and common_check:
#                 result = "The entered password is compromised and commonly used! Change your password immediately!"
#             elif compromised_check:
#                 result = "The entered password is compromised! Change your password immediately!"
#             elif common_check:
#                 result = "The entered password is commonly used! Please choose a stronger password."
#             else:
#                 result = "Password is safe."
            
#             clearAndSend(result)
            
#         # Complexity Check 
#         elif line.startswith("complexity-check"):
#             line = line.replace("complexity-check ", "")
            
#             # Decrypt the password before performing checks
#             decrypted_password = decrypt_password(line, SECRET_KEY)
#             if decrypted_password is None:
#                 continue
            
#             # Pass password to both checks (length and complexity)
#             min_length = 12
#             length_check = lengthCheck(decrypted_password, min_length)
#             complexity_check = complexityCheck(decrypted_password)
            
#             if not length_check:
#                 result = "The entered password did not meet length requirements! Good passwords are at least 12 characters."
#             elif not complexity_check:
#                 result = "The entered password is not complex enough."
#             else:
#                 result = "Password meets all complexity requirements."
            
#             clearAndSend(result)
        
#         # Password Recommendation
#         elif line.startswith("password-recommendation"):
#             password_len_str = line.replace("password-recommendation ", "")
#             # Casting the string from input to be an integer
#             password_len = int(password_len_str)
#             result = ""
            
#             unsafe = True
#             while unsafe:
#                 # Create password
#                 result = password_recommendation(password_len)
                
#                 # Pass to both password checks
#                 compromised_check = password_check(SORTED_COMPROMISED_PWORDS, result)
#                 common_check = password_check(SORTED_COMMON_PWORDS, result)
#                 # notComplex = complexityCheck(result)
                
#                 if compromised_check or common_check:
#                     continue
#                 else:
#                     unsafe = False
            
#             # Encrypt password before sending
#             encrypted_password = encrypt_password(result, SECRET_KEY)
#             if encrypted_password is None:
#                 continue
                
#             clearAndSend(encrypted_password)

#         else:
#             print("Unknown command in password-srv.txt file")
        
#         # Close File
#         pword_file.close()


@app.route('/password-check', methods=['POST'])
def handle_password_check():
    data = request.get_json()
    encrypted_password = data.get('encrypted_password')
    selected_service = data.get('selected_service')

    if not encrypted_password or not selected_service:
        return jsonify({'error': 'Missing data'}), 400

    decrypted_password = decrypt_password(encrypted_password, SECRET_KEY)
    if decrypted_password is None:
        return jsonify({'error': 'Error in decryption'}), 500

    result = None
    
    # -------- Compromised Password Check -------- 
    if selected_service == "compromised-password-check":
        # Pass password to compromised check
        compromised_check = password_check(SORTED_COMPROMISED_PWORDS, decrypted_password)
        if compromised_check == True:
            result = "The entered password is compromised! Change your password immediately!"
        else:
            result = "Password is safe."
    
    # -------- Common Password Check -------- 
    elif selected_service == "common-password-check":
        # Pass password to common check
        common_check = password_check(SORTED_COMMON_PWORDS, decrypted_password)
        if common_check:
            result = "The entered password is commonly used! Please choose a stronger password."
        else:
            result = "Password is safe."
            
    # -------- Combined Password Check -------- 
    elif selected_service == "combined-check":
        # Pass password to both password checks
        compromised_check = password_check(SORTED_COMPROMISED_PWORDS, decrypted_password)
        common_check = password_check(SORTED_COMMON_PWORDS, decrypted_password)

        if compromised_check and common_check:
            result = "The entered password is compromised and commonly used! Change your password immediately!"
        elif compromised_check:
            result = "The entered password is compromised! Change your password immediately!"
        elif common_check:
            result = "The entered password is commonly used! Please choose a stronger password."
        else:
            result = "Password is safe."
    
    # -------- Password Complexity Check -------- 
    elif selected_service == "complexity-check":
        # result = complexity_check(decrypted_password)
        # Pass password to both checks (length and complexity)
        min_length = 10
        length_check = lengthCheck(decrypted_password, min_length)
        complexity_check = complexityCheck(decrypted_password)
        
        if not length_check:
            result = "The entered password did not meet length requirements! Good passwords are at least 10 characters."
        elif not complexity_check:
            result = "The entered password is not complex enough."
        else:
            result = "Password meets all complexity requirements."
        
    # -------- Password Recommendation -------- 
    elif selected_service == "password-recommendation":
        password_len = int(decrypted_password)
        result = password_recommendation(password_len)
    
    # -------- Unknown Command -------- 
    else:
        return jsonify({'error': 'Unknown command'}), 400
    
    return jsonify({'result': result})
        
        
## Code for clearing .txt files and writing results to result_file
def clearAndSend(results):
    # Clear contents of both pword_file and result_file, write to result_file
        pword_file = open(PASSWORD_PATH, "w")                                   #FIXME: DONT THINK I NEED
        result_file = open(RESULT_PATH, "w")
        result_file.write(results)
        result_file.close()

## ------- Encrypting and Decrypting Password Using Service my Partner Created -------
def encrypt_password(password, key):
    encrypt_data = {'password': password, 'key': key}
    encrypt_response = requests.post(ENCRYPTION_SERVICE_URL, json=encrypt_data)
    
    if encrypt_response.status_code == 200:
        encrypted_password = encrypt_response.json()['encrypted_password']
        return encrypted_password
    else:
        print("Error in encryption response:", encrypt_response.text)
        return None

def decrypt_password(encrypted_password, key):
    decrypt_data = {'encrypted_password': encrypted_password, 'key': key}
    decrypt_response = requests.post(DECRYPTION_SERVICE_URL, json=decrypt_data)

    if decrypt_response.status_code == 200:
        decrypted_password = decrypt_response.json()['decrypted_password']
        return decrypted_password
    else:
        print("Error in decryption response:", decrypt_response.text)
        return None

## ---------- Code for Compromised and Common Password Checks ------------
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

def load_passwords(password_list):
    with open(password_list, "r") as pword_file:
        passwords = json.load(pword_file)
    return passwords

def password_check(password_file, password):
    # Checks inputted password_file for inputted password with binary search
    password_list = load_passwords(password_file)
    if binary_search(password_list, password):
        return True
    else:
        return False
    
## ---------- Code for Complexity Check ------------
def lengthCheck(password, min_length):
    if len(password) < min_length:
        return False
    return True
    
def complexityCheck(password):
    # Uppercase
    if not re.search(r'[A-Z]', password):
        return False

    # Lowercase
    if not re.search(r'[a-z]', password):
        return False
    
    # Integers
    if not re.search(r'\d', password):
        return False
    
    # Special Characters
    if not re.search(r'[^a-zA-Z0-9]', password):
        return False
    
    return True
    
## ---------- Code for password recommendation ------------
def password_recommendation(password_length):
    result = ""
    unsafe = True
    # notComplex = True                       #TODO: Delete Later
    # while unsafe and notComplex:
    while unsafe:
        # Create password
        result = get_password_recommendation(password_length)
        
        # Pass to both password checks
        compromised_check = password_check(SORTED_COMPROMISED_PWORDS, result)
        common_check = password_check(SORTED_COMMON_PWORDS, result)
        # notComplex = complexityCheck(result)                      #TODO: Delete Later
        
        if compromised_check or common_check:
            continue
        else:
            unsafe = False
        
        # Encrypt password before sending
        encrypted_password = encrypt_password(result, SECRET_KEY)
        if encrypted_password is None:
            continue
        result = encrypted_password
    return result
            
def get_password_recommendation(password_length):
    char_options = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(password_length):
        password += random.choice(char_options)
    return password
    

if __name__ == "__main__":
    # runSRV()                              #FIXME: Updating to HTTP Requests. This is .txt file version
    app.run(host='127.0.0.1', port=9002)

# Password service that uses HTTP requests for communication to UI.py and encryption_microservice.py

import requests, json, string, re, random, secrets
import config
from flask import Flask, request, jsonify
app = Flask(__name__)

## ------- Using HTTP Requests for Communication -------
@app.route(config.PASSWORD_SRV_ROUTE, methods=['POST'])
def handle_password_check():
    data = request.get_json()
    encrypted_password = data.get('encrypted_password')
    selected_service = data.get('selected_service')

    if not encrypted_password or not selected_service:
        return jsonify({'error': 'Missing data'}), 400

    decrypted_password = decrypt_password(encrypted_password, config.SECRET_KEY)
    if decrypted_password is None:
        return jsonify({'error': 'Error in decryption'}), 500

    result = None
    
    # -------- Compromised Password Check --------
    if selected_service == "compromised-password-check":
        # Pass password to compromised check
        compromised_check = password_check(config.SORTED_COMPROMISED_PWORDS, decrypted_password)
        if compromised_check:
            result = "The entered password is compromised! Change your password immediately!"
        else:
            result = "Password is safe."
    
    # -------- Common Password Check --------
    elif selected_service == "common-password-check":
        # Pass password to common check
        common_check = password_check(config.SORTED_COMMON_PWORDS, decrypted_password)
        if common_check:
            result = "The entered password is commonly used! Please choose a stronger password."
        else:
            result = "Password is safe."
            
    # -------- Combined Password Check --------
    elif selected_service == "combined-check":
        # Pass password to both password checks
        compromised_check = password_check(config.SORTED_COMPROMISED_PWORDS, decrypted_password)
        common_check = password_check(config.SORTED_COMMON_PWORDS, decrypted_password)

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


## --------- Encrypting and Decrypting Password Using Service my Partner Created ---------
def encrypt_password(password, key):
    encrypt_data = {'password': password, 'key': key}
    encrypt_response = requests.post(config.ENCRYPTION_SERVICE_URL, json=encrypt_data)
    
    if encrypt_response.status_code == 200:
        encrypted_password = encrypt_response.json()['encrypted_password']
        return encrypted_password
    else:
        print("Error in encryption response:", encrypt_response.text)
        return None

def decrypt_password(encrypted_password, key):
    decrypt_data = {'encrypted_password': encrypted_password, 'key': key}
    decrypt_response = requests.post(config.DECRYPTION_SERVICE_URL, json=decrypt_data)

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
    if not re.search(r'[A-Z]', password):          # Uppercase
        return False
    if not re.search(r'[a-z]', password):          # Lowercase
        return False
    if not re.search(r'\d', password):             # Integers
        return False
    if not re.search(r'[^a-zA-Z0-9]', password):   # Special Characters
        return False
    return True
    
    
## ---------- Code for password recommendation ------------
def password_recommendation(password_length):
    result = ""
    unsafe = True
    while unsafe:
        # Create password
        result = get_password_recommendation(password_length)
        
        # Pass to both password checks
        compromised_check = password_check(config.SORTED_COMPROMISED_PWORDS, result)
        common_check = password_check(config.SORTED_COMMON_PWORDS, result)
        if compromised_check or common_check:
            continue
        else:
            unsafe = False
        
        # Encrypt password before sending
        encrypted_password = encrypt_password(result, config.SECRET_KEY)
        if encrypted_password is None:
            continue
        result = encrypted_password
    return result
            
def get_password_recommendation(password_length):
    letters_and_nums = string.ascii_letters + string.digits
    special_characters = string.punctuation
    new_password = ""
    
    for _ in range(password_length):
        char_class = random.choices([letters_and_nums, special_characters], 
                                    weights = config.CHARACTER_PROBAILITIES)[0]
        new_password += random.choice(char_class)
        
    # Create a list of chosen characters, shuffle it, and then return it back in a string again.
    password_list = list(new_password)
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password
    
    
if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PASSWORD_SRV_PORT)
    
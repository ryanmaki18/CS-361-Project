# Microservice that takes commands/inputs from password-srv.txt
import time
import json

PASSWORD_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/password-srv.txt"
RESULT_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/result.txt"

SORTED_COMPROMISED_PWORDS = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/sorted_compromised_passwords.json"
SORTED_COMMON_PWORDS = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/sorted_common_passwords.json"

def runSRV():
    while True:

        # Sleep for 1 second
        time.sleep(1)

        # open password file and get contents
        pword_file = open(PASSWORD_PATH, "r")
        line = pword_file.read()

        # If file is blank
        if line == '' or line == ' ':
            continue

        # Compromised Password Check
        if line.startswith("compromised-password-check"):

            line = line.replace("compromised-password-check ", "")

            if password_check(SORTED_COMPROMISED_PWORDS, line) == True:
                result = "The entered password is compromised! Change your password immediately!"
            else:
                result = "Password is safe."

            # Clear contents of both pword_file and write to result_file
            pword_file = open(PASSWORD_PATH, "w")
            result_file = open(RESULT_PATH, "w")
            result_file.write(result)


        # Common Password Check
        elif line.startswith("common-password-check"):
            line = line.replace("common-password-check ", "")
            
            if password_check(SORTED_COMMON_PWORDS, line) == True:
                result = "The entered password is commonly used! Please choose a stronger password."
            else:
                result = "Password is safe."

            # Clear contents of both pword_file and write to result_file
            pword_file = open(PASSWORD_PATH, "w")
            result_file = open(RESULT_PATH, "w")
            result_file.write(result)


        # Combined Check (Compromised and Common)
        elif line.startswith("combined-check"):
            line = line.replace("combined-check ", "")

            compromised_check = password_check(SORTED_COMPROMISED_PWORDS, line)
            common_check = password_check(SORTED_COMMON_PWORDS, line)

            if compromised_check and common_check:
                result = "The entered password is compromised and commonly used! Change your password immediately!"
            elif compromised_check:
                result = "The entered password is compromised! Change your password immediately!"
            elif common_check:
                result = "The entered password is commonly used! Please choose a stronger password."
            else:
                result = "Password is safe."
            
            # Clear contents of both pword_file and write to result_file
            pword_file = open(PASSWORD_PATH, "w")
            result_file = open(RESULT_PATH, "w")
            result_file.write(result)
        
        # Password Recommendation
        elif line.startswith("password-recommendation"):
            password_len = line.replace("password-recommendation ", "")

            result = password_recommendation(password_len)

            # Clear contents of both pword_file and write to result_file
            pword_file = open(PASSWORD_PATH, "w")
            result_file = open(RESULT_PATH, "w")
            result_file.write(result)

        else:
            print("Unknown command in password-srv.txt file")
        
        # Close File
        pword_file.close()
        result_file.close()


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

def password_recommendation(password_len):
    # Returns a random, strong passworth of length password_len
    return "HI"
    

if __name__ == "__main__":
    runSRV()

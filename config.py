######## ----------- Config File Password Service Project ----------- ########
## Made for CS 361 by Ryan Maki


# ----------- HTTP Communication Information -----------
ENCRYPTION_SERVICE_URL = 'http://127.0.0.1:9001/encrypt'
ENCRYPT_ROUTE='/encrypt'
DECRYPTION_SERVICE_URL = 'http://127.0.0.1:9001/decrypt'
DECRYPT_ROUTE='/decrypt'
ENCRYPT_DECRYPT_PORT = 9001
SECRET_KEY = 'SecretKey'
PASSWORD_SRV_URL = 'http://127.0.0.1:9002/passwords'
PASSWORD_SRV_ROUTE = '/passwords'
HOST = '127.0.0.1'
PASSWORD_SRV_PORT = 9002

# ----------- Used for Compromised and Common Password Checks -----------
SORTED_COMPROMISED_PWORDS = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/password-srv-files/sorted_compromised_passwords.json"
SORTED_COMMON_PWORDS = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/password-srv-files/sorted_common_passwords.json"

# ----------- Used for Password Recomendation -----------
PROBABILITY_LETTERS_AND_NUMS = 0.85
PROBABILITY_SPECIAL_CHARACTERS = 0.15
CHARACTER_PROBAILITIES = [PROBABILITY_LETTERS_AND_NUMS, PROBABILITY_SPECIAL_CHARACTERS]

# ----------- For Help Video -----------
CHECKER_VIDEO_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/VideoAndAudio/checker.mp4"
CHECKER_AUDIO_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/VideoAndAudio/checkerAudio.m4a"
RECOMMENDATION_VIDEO_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/VideoAndAudio/recommendation.mp4"
RECOMMENDATION_AUDIO_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/VideoAndAudio/recommendationAudio.m4a"
VIDEO_HEIGHT = 480
VIDEO_WIDTH = 720

# ----------- Messages for UI.py -----------
starting_message = """
Please enter the number or name of the service you'd like to use: 
    (Passwords Fully Encrypted!)
1 - compromised-password-check
2 - common-password-check
3 - combined-check
    (Checks if compromised or common)
4 - complexity-check
    (Checks if password meets complexity requirements)
5 - password-recommendation
    (Recommends a safe and strong password of any length)
6 - help 
    (Pulls up explanation videos; Will force you to exit when done)
Leave Blank to Exit. 

"""

help_video_input = """Please select which video you would like to watch:
1 - password checker explaination video
2 - password recommendation explaination video
Leave Blank to Exit.

"""

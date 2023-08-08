# A user interface (UI) that prompts user for their choice of service to run
# Uses HTTP requests for communication to password-srv.py and encryption_microservice.py

import requests, cv2
from ffpyplayer.player import MediaPlayer
import config

def runUI():
    while True:
        # prompt user for service selection 
        user_input = input(config.starting_message)

        # If left blank, then exit
        if user_input == '':
            break
        
        # Now that we have a user selection, figure out which it is and complete the task
        if user_input.startswith("compromised-password-check") or user_input.startswith("1"):
            print("compromised-password-check selected.")
            
            while True:
                # Loops until input is left blank
                password = input("Please enter a password or leave blank to exit\n")
                if password == '':
                    break
                
                # Encrypt password before sending/using
                encrypted_password = encrypt_password(password, config.SECRET_KEY)
                if encrypted_password is None:
                    continue

                # Sends encrypted password to password-srv.py and executes the code associated with the selected service
                selected_service = "compromised-password-check"
                response = send_request(selected_service, encrypted_password)
                print(response.get('result'))
                
        elif user_input.startswith("common-password-check") or user_input.startswith("2"):
            print("common-password-check selected.")

            while True:
                # Loops until input is left blank
                password = input("Please enter a password or leave blank to exit\n")
                if password == '':
                    break
                
                # Encrypt password before sending/using
                encrypted_password = encrypt_password(password, config.SECRET_KEY)
                if encrypted_password is None:
                    continue 
                
                # Sends encrypted password to password-srv.py and executes the code associated with the selected service
                selected_service = "common-password-check"
                response = send_request(selected_service, encrypted_password)
                print(response.get('result'))
                
        elif user_input.startswith("combined-check") or user_input.startswith("3"):
            print("combined-check selected.")
            
            while True:
                # Loops until input is left blank
                password = input("Please enter a password or leave blank to exit\n")
                if password == '':
                        break
                    
                # Encrypt password before sending/using
                encrypted_password = encrypt_password(password, config.SECRET_KEY)
                if encrypted_password is None:
                    continue
                
                # Sends encrypted password to password-srv.py and executes the code associated with the selected service
                selected_service = "combined-check"
                response = send_request(selected_service, encrypted_password)
                print(response.get('result'))

        elif user_input.startswith("complexity-check") or user_input.startswith("4"):
            print("complexity-check selected.")
            print("Good passwords have lower/uppercase letters, numbers, and special charatcers.")
            
            while True:
                # Loops until input is left blank
                password = input("Please enter a password or leave blank to exit\n")
                if password == '':
                        break
                    
                # Encrypt password before sending/using
                encrypted_password = encrypt_password(password, config.SECRET_KEY)
                if encrypted_password is None:
                    continue
                
                # Sends encrypted password to password-srv.py and executes the code associated with the selected service
                selected_service = "complexity-check"
                response = send_request(selected_service, encrypted_password)
                print(response.get('result'))
                    
        elif user_input.startswith("password-recommendation") or user_input.startswith("5"):
            print("password-recommendation selected.")
            
            while True:
                # Loops until input is left blank
                password_len_str = input("Please enter the password length you'd like, or leave blank to exit.\n")
                if password_len_str.strip() == '':
                    break
                password_len_str = password_len_str.replace(" ", "")
                
                encrypted_len = encrypt_password(password_len_str, config.SECRET_KEY)
                if encrypted_len is None:
                    continue
                
                # Sends encrypted password to password-srv.py and executes the code associated with the selected service
                selected_service = "password-recommendation"
                response = send_request(selected_service, encrypted_len)
                
                # Decrypt the password before displaying
                decrypted_password = decrypt_password(response.get('result'), config.SECRET_KEY)
                if decrypted_password is None:
                    continue
                
                print("Your recommended password is:")
                print(decrypted_password)
                print("Password was checked and is safe.")                
                
        elif user_input.startswith("help") or user_input.startswith("6"):
            # Pulls up video walkthroughs
            print("Help is on the way!")
            
            while True:
                video_selection_str = input(config.help_video_input)
                if video_selection_str.strip() == '':
                    break
                video_selection = int(video_selection_str)
                if video_selection == 1:
                    open_video(config.CHECKER_VIDEO_PATH, config.CHECKER_AUDIO_PATH)
                elif video_selection == 2:
                    open_video(config.RECOMMENDATION_VIDEO_PATH, config.RECOMMENDATION_AUDIO_PATH)
                else:
                    print("Unknown video selection, please try again.")
            
        else:
            print("Unknown Option")

## ---------- Code for HTTP Requests ----------
def send_request(selected_service, encrypted_password=None):
    data = {'selected_service': selected_service, 'encrypted_password': encrypted_password}
    response = requests.post(config.PASSWORD_SRV_URL, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

## ------- Encrypting and Decrypting Password Using Service my Partner Created -------
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

## ------- Code for help video -------
def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def open_video(video, audio):
    print("Pulling up Video...... Press '⌃C' to Exit.")
    video_capture = getVideoSource(video, config.VIDEO_WIDTH, config.VIDEO_HEIGHT)
    audio_player = MediaPlayer(audio)
    
    if video_capture.isOpened() == False:
        print("Error opening video... Please try again.")
        return
    
    while(video_capture.isOpened()):
        ret, frame = video_capture.read()
        audio_frame, val = audio_player.get_frame()
        
        if ret == 0:
            print("End of Video")
            break
        
        cv2.imshow("Video", frame)

        # Press ^C on the keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            cv2.destroyWindow("Video")
            break
        
    video_capture.release()
    cv2.destroyWindow("Video")

if __name__ == "__main__":
    runUI()
    
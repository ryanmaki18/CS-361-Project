# A user interface (UI) that prompts user for their choice of service to run
import time
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer

PASSWORD_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/password-srv.txt"
RESULT_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/result.txt"

CHECKER_VIDEO_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/VideoAndAudio/checker.mp4"
CHECKER_AUDIO_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/VideoAndAudio/checkerAudio.m4a"
RECOMMENDATION_VIDEO_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/VideoAndAudio/recommendation.mp4"
RECOMMENDATION_AUDIO_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/VideoAndAudio/recommendationAudio.m4a"

starting_message = """
Please enter the number or name of the service you'd like to use: 
1 - compromised-password-check
2 - common-password-check
3 - combined-check
    (Checks if compromised or common; Never stores your information)
4 - complexity-check
    (Checks if password meets complexity requirements)
5 - password-recommendation
    (Recommends a safe and strong password of any length)
6 - help 
    (Pulls up explaination videos)
Leave Blank to Exit. 

"""

help_video_input = """Please select which video you would like to watch:
1 - password checker explaination video
2 - password recommendation explaination video
Leave Blank to Exit.

"""

def runUI():
    while True:

        # prompt user for service selection 
        user_input = input(starting_message)

        # If left blank, then exit
        if user_input == '':
            break
        
        if user_input.startswith("compromised-password-check") or user_input.startswith("1"):
            print("compromised-password-check selected.")
            
            while True:
                # Loops until input is left blank
                password = input("Please enter a password or leave blank to exit\n")
                if password == '':
                    break

                # open password-srv.txt file and write the requested service, along with password
                pword_file = open(PASSWORD_PATH, "w")
                pword_file.write("compromised-password-check " + password)
                pword_file.close()

                # Sleep for 2 seconds
                time.sleep(2)

                # Open result.txt, print contents, and then delete contents
                result_file = open(RESULT_PATH, "r")
                result = result_file.read()
                print(result)
                result_file = open(RESULT_PATH, "w")
                result_file.close()

                # Sleep for 2 seconds
                time.sleep(2)

        elif user_input.startswith("common-password-check") or user_input.startswith("2"):
            print("common-password-check selected.")

            while True:
                # Loops until input is left blank
                password = input("Please enter a password or leave blank to exit\n")
                if password == '':
                    break
                
                # open password-srv.txt file and write the requested service, along with password
                pword_file = open(PASSWORD_PATH, "w")
                pword_file.write("common-password-check " + password)
                pword_file.close()

                # Sleep for 2 seconds
                time.sleep(2)
                
                # Open result.txt, print contents, and then delete contents
                result_file = open(RESULT_PATH, "r")
                result = result_file.read()
                print(result)
                result_file = open(RESULT_PATH, "w")
                result_file.close()

                # Sleep for 2 seconds
                time.sleep(2)

        elif user_input.startswith("combined-check") or user_input.startswith("3"):
            print("combined-check selected.")
            
            while True:
                # Loops until input is left blank
                password = input("Please enter a password or leave blank to exit\n")
                if password == '':
                        break
                # open password-srv.txt file and write the requested service, along with password
                pword_file = open(PASSWORD_PATH, "w")
                pword_file.write("combined-check " + password)
                pword_file.close()
                
                # Sleep for 2 seconds
                time.sleep(2)

                # Open result.txt, print contents, and then delete contents
                result_file = open(RESULT_PATH, "r")
                result = result_file.read()
                print(result)
                result_file = open(RESULT_PATH, "w")
                result_file.close()

                # Sleep for 2 seconds
                time.sleep(2)
                
        elif user_input.startswith("complexity-check") or user_input.startswith("4"):
            print("complexity-check.")
            
            while True:
                # Loops until input is left blank
                password = input("Please enter a password or leave blank to exit\n")
                if password == '':
                        break
                # open password-srv.txt file and write the requested service, along with password
                pword_file = open(PASSWORD_PATH, "w")
                pword_file.write("complexity-check " + password)
                pword_file.close()
                
                # Sleep for 2 seconds
                time.sleep(2)

                # Open result.txt, print contents, and then delete contents
                result_file = open(RESULT_PATH, "r")
                result = result_file.read()
                print(result)
                result_file = open(RESULT_PATH, "w")
                result_file.close()

                # Sleep for 2 seconds
                time.sleep(2)
            
        elif user_input.startswith("password-recommendation") or user_input.startswith("5"):
            print("password-recommendation selected.")
            
            while True:
                # Loops until input is left blank
                password_len_str = input("Please enter the password length you'd like, or leave blank to exit.\n")
                if password_len_str.strip() == '':
                    break
                password_len_str = password_len_str.replace(" ", "")
                
                # # Converting from string to integer
                # password_len = int(password_len_str)
                
                # min_len = 5
                # if password_len < min_len:
                #     print("Recommended passwords must be atleast 5 characters.")
                #     continue
                
                # open password-srv.txt file and write the requested service
                pword_file = open(PASSWORD_PATH, "w")
                pword_file.write("password-recommendation " + password_len_str)
                pword_file.close()

                # Sleep for 2 seconds
                time.sleep(3)

                # Open result.txt, print contents, and then delete contents
                result_file = open(RESULT_PATH, "r")
                result = result_file.read()
                print("Your recommended password is:")
                print(result)
                print("Password was checked and is safe.")
                result_file = open(RESULT_PATH, "w")
                result_file.close()

                # Sleep for 2 seconds
                time.sleep(3)
                
        elif user_input.startswith("help") or user_input.startswith("6"):  ## FIXME: Still will not close until process is done running
            # Pulls up video walkthroughs
            print("Help is on the way!")
            
            while True:
                video_selection_str = input(help_video_input)
                if video_selection_str.strip() == '':
                    break
                video_selection = int(video_selection_str)
                if video_selection == 1:
                    open_video(CHECKER_VIDEO_PATH, CHECKER_AUDIO_PATH)
                elif video_selection == 2:
                    open_video(RECOMMENDATION_VIDEO_PATH, RECOMMENDATION_AUDIO_PATH)
                else:
                    print("Unknown video selection, please try again.")
            
        else:
            print("Unknown Option")


## ------- Code for help video -------
def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def open_video(video, audio):
    print("Pulling up Video......")
    height = 480
    width = 720
    video_capture = getVideoSource(video, width, height)
    audio_player = MediaPlayer(audio)
    
    if video_capture.isOpened() == False:
        print("Error opening video... Please try again.")
        
    exit_time = False
    
    while(video_capture.isOpened() and (exit_time == False)):
        ret, frame = video_capture.read()
        audio_frame, val = audio_player.get_frame()
        
        if ret == 0:
            print("End of Video")
            video_capture.release()
            cv2.destroyWindow("Video")
            break
        
        cv2.imshow("Video", frame)
        
        # Press q on the keyboard to exit
        if cv2.waitKey(28) & 0xFF == ord('q'):
            exit_time = True
            video_capture.release()
            cv2.destroyWindow("Video")
            break

if __name__ == "__main__":
    runUI()
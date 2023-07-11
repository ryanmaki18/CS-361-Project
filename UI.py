# A user interface (UI) that prompts user for their choice of service to run
import time
import cv2

PASSWORD_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/password-srv.txt"
RESULT_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/result.txt"

CHECKER_VIDEO_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/Videos/checker.mp4"
RECOMMENDATION_VIDEO_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/Videos/recommendation.mp4"

starting_message = """
Please enter the number or name of the service you'd like to use: 
1 - compromised-password-check
2 - common-password-check
3 - combined-check
    (Checks if compromised or common; Never stores your information)
4 - password-recommendation
    (Recommends a safe and strong password of any length)
5 - help 
    (Pulls up explaination video)
Leave Blank to Exit. 

"""

help_video_input = """
Please select which video you would like to see:
1 - password checker explaination video
2 - password recommendation explaination video
            
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

        elif user_input.startswith("password-recommendation") or user_input.startswith("4"):
            print("password-recommendation selected.")
            
            while True:
                # Loops until input is left blank
                password_len = input("Please enter the password length you'd like, or leave blank to exit.\n")
                if password_len.strip() == '':
                    break
                password_len = password_len.replace(" ", "")
                

                # open password-srv.txt file and write the requested service
                pword_file = open(PASSWORD_PATH, "w")
                pword_file.write("password-recommendation " + password_len)
                pword_file.close()

                # Sleep for 2 seconds
                time.sleep(2)

                # Open result.txt, print contents, and then delete contents
                result_file = open(RESULT_PATH, "r")
                result = result_file.read()
                print("Your recommended password is:")
                print(result)
                print("Password was checked and is safe.")
                result_file = open(RESULT_PATH, "w")
                result_file.close()

                # Sleep for 2 seconds
                time.sleep(2)

        elif user_input.startswith("help") or user_input.startswith("5"):
            # Pulls up video explaination 
            print("Help is on the way!")
            
            # FIXME: Implement this!
            # help_video()
            
            video_selection_str = input(help_video_input)
            video_selection = int(video_selection_str)
            if video_selection == 1

            elif
            
            else:
                print("Unknown video selection, please try again.")
            
            
        else:
            print("Unknown Option")


## ------- Code for help video -------
def open_video(video):
    print("Pulling up Video......")
    video_capture = cv2.VideoCapture(video)
    
    if video_capture.isOpened() == False:
        print("Error opening video... Please try again.")
        
    while(video_capture.isOpened()):
        ret, frame = video_capture.read
        if ret == True:
            # Then Display the frame
            cv2.imshow("Frame", frame)
            
            # Press q on the keyboard to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Then break out
        else:
            break
    
    # When video is done, release the video capture opject and close all windows
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    runUI()
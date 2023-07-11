# A user interface (UI) that prompts user for their choice of service to run
import time

PASSWORD_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/password-srv.txt"
RESULT_PATH = "/Users/ryanmaki/Documents/UO/CS361/CS-361-Project/result.txt"

starting_message = """
Please enter the number or name of the service you'd like to use: 
1 - compromised-password-check
2 - common-password-check
3 - combined-check
    (All Fully Encrypted)
4 - password-recommendation
    (Recommends 15 character, strong password)
5 - help 
    (Pulls up explaination video)
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

        elif user_input.startswith("password-recommendation") or user_input.startswith("4"):
            print("password-recommendation selected.")
            
            while True:
                # Loops until input is left blank
                password_len = input("Please the password length you'd like\n")
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
                result_file = open(RESULT_PATH, "w")
                result_file.close()

                # Sleep for 2 seconds
                time.sleep(2)

        elif user_input.startswith("help") or user_input.startswith("5"):
            # Pulls up video explaination
            print("Pulling up Video")

            # TODO: Figure out where to implement this?
            # Think i want to just do it right here instead of with .txt file

            # help_video()
        else:
            print("Unknown Option")


if __name__ == "__main__":
    runUI()
# CS-361-Project
CS 361 Assignment #1

Hey there, this is my CS 361 project. The main file is UI.py which calls upon password-srv.py and encryption_microservice.py (which my partner made) using HTTP requests. 

**There are multiple features including:**
  - compromised-password-check
  - common-password-check
  - combined-check  
    (Checks if compromised or common)
  - complexity-check  
    (Checks if password meets complexity requirements)  
  - password-recommendation  
    (Recommends a safe and strong password of any length)  
  - help   
    (Pulls up explanation videos; Will force you to exit when done)  

The compromised password check checks against 100,000 pwned passworded (like from data leaks)
The common passwords are, as they sound, super common and shouldn't be used.
The combined check obviously checks for them both.
The complexity check simply checks of it has upper/lower case letters, a number, and special character.
Lastly, the password recommendation takes in a password length you would like, and returns a random password of that length. 

Enjoy!

import json

INPUT = "/Users/ryanmaki/Documents/UO/CS361/Project/100000-common-passwords.json"
OUTPUT = "/Users/ryanmaki/Documents/UO/CS361/Project/sorted_common_passwords.json"

def sort_passwords_from_json(file_path, output_file_path):
    with open(file_path, 'r') as file:
        passwords = json.load(file)
    
    sorted_passwords = sorted(passwords)
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(json.dumps(sorted_passwords, indent=4))


if __name__ == "__main__":
    sort_passwords_from_json(INPUT, OUTPUT)
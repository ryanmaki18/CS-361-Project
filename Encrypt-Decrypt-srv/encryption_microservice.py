from flask import Flask, request
app = Flask(__name__)


class Cipher:
    def encrypt(self, password, key):
        password_length = len(password)
        key_length = len(key)
        res = ""

        for i in range(password_length):
            shift = ord(password[i]) + ord(key[i % key_length])
            res += chr((shift - 33) % 94 + 33)

        return res

    def decrypt(self, password, key):
        password_length = len(password)
        key_length = len(key)
        res = ""

        for i in range(password_length):
            shift = ord(password[i]) - ord(key[i % key_length])
            res += chr((shift - 33) % 94 + 33)

        return res


cipher = Cipher()


@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    data = request.get_json()
    password = data['password']
    key = data['key']
    encrypted_password = cipher.encrypt(password, key)
    return {'encrypted_password': encrypted_password}


@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    data = request.get_json()
    encrypted_password = data['encrypted_password']
    key = data['key']
    decrypted_password = cipher.decrypt(encrypted_password, key)
    return {'decrypted_password': decrypted_password}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9001)

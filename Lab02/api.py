from flask import Flask, request, jsonify, render_template
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/caesar")
def caesar_page():
    return render_template("caesar.html")

@app.route("/railfence")
def railfence_page():
    return render_template("railfence.html")

@app.route("/vigenere")
def vigenere_page():
    return render_template("vigenere.html")

@app.route("/playfair")
def playfair_page():
    return render_template("playfair.html")

@app.route("/transposition")
def transposition_page():
    return render_template("transposition.html")



caesar_cipher = CaesarCipher()
#CAESAR
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#VIGENERE
vigenere_cipher = VigenereCipher()
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def cvigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#RAIL FENCE
railfence_cipher = RailFenceCipher()
@app.route("/api/railfence/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#Playfair
playfair_cipher = PlayFairCipher()
@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})
    
@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt_route():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
    return jsonify({'encrypted_message': encrypted_text, 'matrix': matrix}) # Thêm 'matrix' vào response

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt_route():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return jsonify({'decrypted_message': decrypted_text, 'matrix': matrix}) # Thêm 'matrix' vào response


#TRANSPOSTION CIPHER ALGORITHM
transposition_cipher = TranspositionCipher()
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
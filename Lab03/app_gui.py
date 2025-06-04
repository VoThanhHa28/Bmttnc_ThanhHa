import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import os
current_file_dir = os.path.dirname(os.path.abspath(__file__))
if current_file_dir not in sys.path:
    sys.path.append(current_file_dir)

from ui.ui_rsa import Ui_MainWindow
from cipher.rsa.rsa_cipher import RSACipher


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rsa_handler = RSACipher()

        self.generateKeysButton.clicked.connect(self.handle_generate_keys)
        self.encryptButton.clicked.connect(self.handle_encrypt)
        self.decryptButton.clicked.connect(self.handle_decrypt)
        self.signButton.clicked.connect(self.handle_sign)
        self.verifyButton.clicked.connect(self.handle_verify)

        self.private_key, self.public_key = self.rsa_handler.load_keys()
        if not self.private_key or not self.public_key:
            QMessageBox.warning(self, "Cảnh báo", "Không tìm thấy khóa RSA. Vui lòng tạo khóa trước.")

    def handle_generate_keys(self):
        self.rsa_handler.generate_keys()
        self.private_key, self.public_key = self.rsa_handler.load_keys()

        if self.private_key and self.public_key:
            QMessageBox.information(self, "Thành công", "Đã tạo và lưu cặp khóa RSA thành công.")
        else:
            QMessageBox.critical(self, "Lỗi", "Không thể tạo khóa RSA. Kiểm tra console để biết chi tiết.")

    def handle_encrypt(self):
        if not self.public_key:
            QMessageBox.warning(self, "Lỗi", "Chưa có khóa công khai. Vui lòng tạo khóa trước.")
            return

        message = self.plainTextEdit.toPlainText() # Lấy thông điệp từ Plain text
        if not message:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập thông điệp cần mã hóa.")
            return

        try:
            encrypted_bytes = self.rsa_handler.encrypt(message, self.public_key)
        except UnicodeEncodeError:
            QMessageBox.critical(self, "Lỗi mã hóa", "Thông điệp chứa ký tự không phải ASCII. Vui lòng sử dụng tiếng Anh hoặc thay đổi encoding trong rsa_cipher.py thành 'utf-8'.")
            return
        except Exception as e:
            QMessageBox.critical(self, "Lỗi mã hóa", f"Có lỗi xảy ra khi mã hóa: {e}")
            return

        if encrypted_bytes:
            encrypted_hex = encrypted_bytes.hex()
            self.encryptedTextOutput.setText(encrypted_hex) # HIỂN THỊ KẾT QUẢ MÃ HÓA VÀO Ô ENCRYPTED
            QMessageBox.information(self, "Thành công", "Thông điệp đã được mã hóa.")
        else:
            QMessageBox.critical(self, "Lỗi", "Không thể mã hóa thông điệp. Kiểm tra console để biết chi tiết.")

    def handle_decrypt(self):
        if not self.private_key:
            QMessageBox.warning(self, "Lỗi", "Chưa có khóa riêng tư. Vui lòng tạo khóa trước.")
            return

        ciphertext_hex = self.encryptedTextOutput.toPlainText()
        if not ciphertext_hex:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng thực hiện mã hóa trước hoặc nhập dữ liệu vào ô Encrypted.")
            return

        try:
            ciphertext_bytes = bytes.fromhex(ciphertext_hex)
        except ValueError:
            QMessageBox.critical(self, "Lỗi", "Định dạng hex của thông điệp mã hóa không hợp lệ.")
            return

        decrypted_message = self.rsa_handler.decrypt(ciphertext_bytes, self.private_key)

        if decrypted_message is not None and decrypted_message is not False:
            self.plainTextEdit.setText(decrypted_message) # Hiển thị kết quả giải mã vào ô Plain text
            # KHÔNG XÓA Ô NÀO CẢ SAU KHI GIẢI MÃ
            QMessageBox.information(self, "Thành công", "Thông điệp đã được giải mã.")
        else:
            QMessageBox.critical(self, "Lỗi", "Không thể giải mã thông điệp. Có thể khóa không đúng, dữ liệu hỏng, hoặc lỗi encoding. Kiểm tra console.")

    def handle_sign(self):
        if not self.private_key:
            QMessageBox.warning(self, "Lỗi", "Chưa có khóa riêng tư. Vui lòng tạo khóa trước.")
            return

        # Lấy thông điệp để ký từ ô cipherTextInput
        message_to_sign = self.cipherTextInput.toPlainText() # <--- VẪN LẤY TỪ CIPHERTEXTINPUT
        if not message_to_sign:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập thông điệp vào ô 'Input for Signing' để tạo chữ ký.")
            return

        try:
            signature_bytes = self.rsa_handler.sign(message_to_sign, self.private_key)
        except UnicodeEncodeError:
            QMessageBox.critical(self, "Lỗi ký", "Thông điệp chứa ký tự không phải ASCII. Vui lòng sử dụng tiếng Anh hoặc thay đổi encoding trong rsa_cipher.py thành 'utf-8'.")
            return
        except Exception as e:
            QMessageBox.critical(self, "Lỗi ký", f"Có lỗi xảy ra khi ký: {e}")
            return

        if signature_bytes:
            signature_hex = signature_bytes.hex()
            self.signatureTextOutput.setText(signature_hex) # Xuất chữ ký hex vào signatureTextOutput
            QMessageBox.information(self, "Thành công", "Thông điệp đã được ký. Chữ ký hiển thị ở ô Signature Output.")
        else:
            QMessageBox.critical(self, "Lỗi", "Không thể ký thông điệp. Kiểm tra console để biết chi tiết.")

    def handle_verify(self):
        if not self.public_key:
            QMessageBox.warning(self, "Lỗi", "Chưa có khóa công khai. Vui lòng tạo khóa trước.")
            return

        # Lấy thông điệp gốc từ ô mà bạn đã dùng để ký (cipherTextInput)
        message_original_for_verify = self.cipherTextInput.toPlainText() # <--- THAY ĐỔI LẤY TỪ CIPHERTEXTINPUT
        signature_hex_to_verify = self.signatureTextOutput.toPlainText()

        if not message_original_for_verify or not signature_hex_to_verify:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập thông điệp gốc (từ ô 'Input for Signing') và đảm bảo có chữ ký (Signature Output) để xác minh.")
            return

        try:
            signature_bytes_to_verify = bytes.fromhex(signature_hex_to_verify)
        except ValueError:
            QMessageBox.critical(self, "Lỗi", "Định dạng hex của chữ ký không hợp lệ.")
            return

        try:
            is_verified = self.rsa_handler.verify(message_original_for_verify, signature_bytes_to_verify, self.public_key)
        except UnicodeEncodeError:
            QMessageBox.critical(self, "Lỗi xác minh", "Thông điệp gốc chứa ký tự không phải ASCII. Vui lòng sử dụng tiếng Anh hoặc thay đổi encoding trong rsa_cipher.py thành 'utf-8'.")
            return
        except Exception as e:
            QMessageBox.critical(self, "Lỗi xác minh", f"Có lỗi xảy ra khi xác minh: {e}")
            return

        if is_verified:
            QMessageBox.information(self, "Xác minh", "Xác minh thành công: Chữ ký hợp lệ.")
        else:
            QMessageBox.warning(self, "Xác minh", "Xác minh thất bại: Chữ ký không hợp lệ hoặc thông điệp đã thay đổi.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
import hashlib

def calculate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

data_to_hash = input("Nhập dữ liệu để hash bằng MD5: ")
hash_value = calculate_md5(data_to_hash)
print("Giá trị hash MD5:", hash_value)
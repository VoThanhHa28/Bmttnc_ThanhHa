def dao_nguoc_chuoi(lst):
    print(lst[:: -1])
input_lst = input("Nhập vào 1 danh sách các số cách nhau bởi dấu phẩy: ")
lst = list(map(int, input_lst.split(',')))
dao_nguoc_chuoi(lst)
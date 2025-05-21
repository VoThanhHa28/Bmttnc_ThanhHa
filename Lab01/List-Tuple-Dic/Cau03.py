def tao_tuple_tu_lst(lst):
    return tuple(lst)
input_lst = input("Nhập danh sách các số,  cách nhau bằng dấu phẩy: ")
lst = list(map(int, input_lst.split(',')))
print(tao_tuple_tu_lst(lst))

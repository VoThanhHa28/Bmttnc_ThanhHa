def truy_cap_phan_tu(tuple):
    first_ele = tuple[0]
    last_ele = tuple[-1]
    return first_ele, last_ele
input_tuple = eval(input("NhậP tuple, ví dụ (1,2,3): "))
first, last = truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên: ",first)
print("Phần tử cuối cùng: ",last)
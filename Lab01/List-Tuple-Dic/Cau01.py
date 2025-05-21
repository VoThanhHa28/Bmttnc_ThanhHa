def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        tong += num
    return tong
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

answer = tinh_tong_so_chan(numbers)
print("Tổng là: " ,answer)
def dem_so_lan_xuat_hien(lst):
    count_dic = {}
    for item in lst:
        if item in count_dic:
            count_dic[item] += 1
        else: 
            count_dic[item] = 1
    return count_dic
input_lst = input("Nhập danh sách các từ, cách nhau bằng khoảng trắng: ")
lst = input_lst.split()
print(dem_so_lan_xuat_hien(lst))
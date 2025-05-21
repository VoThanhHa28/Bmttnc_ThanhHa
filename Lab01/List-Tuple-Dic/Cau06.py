def xoa_1_phan_tu(dic, key):
    if key in dic:
        del dic[key]
    return dic
input_dic = {'a': 1, 'b': 2}
key = 'b'
print(xoa_1_phan_tu(input_dic, key))
            
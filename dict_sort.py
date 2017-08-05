'''给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','连接，如‘1,2,3'。要求key按照字典序升序排列(注意key可能是字符串）。

例如：a={1:1,2:2,3:3}, 则输出：1,2,3'''

#coding:utf-8

a={1:1,2:2,3:3}
dict_key_list =list()

for key in a.keys():
    dict_key_list.append(str(key))
dict_key_list.sort()

print(','.join(dict_key_list))
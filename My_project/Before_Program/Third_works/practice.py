my_string =""

my_list = [['on e', 1],['t wo', 2],['thr ee',3],['fo ur', 4],['fi ve', 5],['o ne', 6]]
new_list = []
for i in my_list:
    non_blank = str(i[0]).replace(" ", "")
    new_list.append(non_blank)
new_list = set(new_list)
print(new_list)
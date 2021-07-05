dict_a = {"eu":"eur", "usd":"dollar"}
for k in list(dict_a):
    key1 = f"{k}{len(k)}"
    dict_a[key1] = dict_a.pop(k)
print(dict_a)


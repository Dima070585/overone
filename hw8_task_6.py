
def tas_6(lst):
    max_el = max(lst)
    min_el = min(lst)
    max_i = lst.indedx(max_el)
    min_i = lst.indedx(min_el)
    lst[min_i],lst[max_i] = lst[max_i],lst[min_i]






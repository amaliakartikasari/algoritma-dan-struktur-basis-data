import os
os.system('cls')

def flatten(l):
    flat_list = []
    for a in l:
        if isinstance(a, list):
            flat_list.extend(flatten(a))
        else:
            flat_list.append(a)
    return flat_list

def quick_sort(l):
    if len(l) <= 1:
        return l
    
    l = flatten(l)
    pivot = l[0]
    left = [x for x in l[1:] if x < pivot]
    right = [x for x in l[1:] if x >= pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

angka = [12,1,[22,3,[8,14]],2,6,[11],90]
angka = quick_sort(angka)

print(angka)
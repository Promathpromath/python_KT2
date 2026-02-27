def create_phone_number(lst: list) -> str:
    phone_list = []
    for num in lst:
        phone_list.append(str(num)) 
    phone_string = ''.join(phone_list)
    part1 = phone_string[0:3]
    part2 = phone_string[3:6] 
    part3 = phone_string[6:10]
    
    return f"({part1}) {part2}-{part3}"

def duplicate_encode(text: str) -> str:
    """Решение для Задачи 2"""
    freq_map = {}
    for symbol in text.lower():
        freq_map[symbol] = freq_map.get(symbol, 0) + 1
    
    encoded = []
    for original_char in text:
        if freq_map[original_char.lower()] == 1:
            encoded.append("(")
        else:
            encoded.append(")")
    return "".join(encoded)

def is_valid_walk(walk: list) -> bool:
    """Решение для Задачи 3"""
 
    if len(walk) != 10:
        return False
    n = []
    s = []
    w = []
    e = []
    
    for step in walk:
        if step == 'n':
            n.append(step)
        elif step == 's':
            s.append(step)
        elif step == 'w':
            w.append(step)
        elif step == 'e':
            e.append(step)
    
    return len(n) == len(s) and len(w) == len(e)


def move_zeros(lst: list) -> list:
    """Решение для Задачи 4"""
    nz = []
    z = []
    
    for e in lst:
        if e != 0:
            nz.append(e)
        else:
            z.append(e)
    
    return nz + z


        
def find_uniq(lst: list):
    """Решение для Задачи 5"""
    f = lst[0]
    s = lst[1]
    t = lst[2]
    
    c = []
    v = []
    
    if f == s:
        v.append(f)
        c.append(t)
    elif f == t:
        v.append(f)
        c.append(s)
    else:
        v.append(s)
        c.append(f)
    
    for i in lst:
        if i not in v:
            c.append(i)
    
    for x in c:
        if lst.count(x) == 1:
            return x

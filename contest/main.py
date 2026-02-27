def create_phone_number(lst: list) -> str:
    """Решение для Задачи 1"""
    nums = ''.join(str(d) for d in lst)
    return f"({nums[:3]}) {nums[3:6]}-{nums[6:]}"

def duplicate_encode(text: str) -> str:
    """Решение для Задачи 2"""
    text_lower = text.lower()
    char_count = {}
    for ch in text_lower:
        char_count[ch] = char_count.get(ch, 0) + 1
    return ''.join('(' if char_count[ch] == 1 else ')' for ch in text_lower)

def is_valid_walk(walk: list) -> bool:
    """Решение для Задачи 3"""
    if len(walk) != 10:
        return False
    return walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')

def move_zeros(lst: list) -> list:
    """Решение для Задачи 4"""
    non_zeros = [x for x in lst if x != 0]
    return non_zeros + [0] * (len(lst) - len(non_zeros))

def find_uniq(lst: list):
    """Решение для Задачи 5"""
    a, b, c = lst[0], lst[1], lst[2]
    if a == b or a == c:
        common = a
    else:
        common = b
    for x in lst:
        if x != common:
            return x
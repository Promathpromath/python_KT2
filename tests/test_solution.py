from contest.main import create_phone_number, duplicate_encode, is_valid_walk, move_zeros, find_uniq

def test_create_phone_number():
    """Тесты к Задаче №1"""
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"
    assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"
    
def test_duplicate_encode():
    """Тесты к Задаче №2"""
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())", "Внимание! функция должна игнорировать регистр!"
    assert duplicate_encode("(( @") == "))(("
    
def test_is_valid_walk():
    """Тесты к Задаче №3"""
    assert is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) == True
    assert is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) == False, 'Слишком длинная прогулка'   
    assert is_valid_walk(['w']) == False, 'Слишком короткая прогулка'           
    assert is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) == False
    
def test_move_zeros():
    """Тесты к Задаче №4"""
    assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0] 
    assert move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert move_zeros([0, 0]) == [0, 0]
    assert move_zeros([0]) == [0]
    assert move_zeros([]) == []
    
def test_find_uniq():
    """Задача №5"""
    assert find_uniq([1, 1, 1, 2, 1, 1]) == 2
    assert find_uniq([0, 0, 0.55, 0, 0]) == 0.55
    assert find_uniq([3, 10, 3, 3, 3]) == 10

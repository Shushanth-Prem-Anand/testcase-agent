# rag/simple_rag.py

def get_related_example(function_name):
    examples = {
        "add_numbers": '''
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, -1) == -2
    assert add_numbers(0, 0) == 0
''',

        "is_prime": '''
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
''',

        "reverse_string": '''
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
''',

        "calculate_discount": '''
def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(200, 0) == 200
    assert calculate_discount(150, 100) == 0
    try:
        calculate_discount(100, 150)
    except ValueError:
        assert True
'''
    }

    return examples.get(function_name, "# No similar test cases found.")

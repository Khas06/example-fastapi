from app.calculations import add

def test_add():
    print("hello")
    assert add(5, 3) == 8

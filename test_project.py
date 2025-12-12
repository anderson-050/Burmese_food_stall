import pytest
from project import get_menu, item_match, get_item_data, process_order

@pytest.fixture
def menu():
    return get_menu()

def test_menu_is_a_list(menu):
    assert isinstance(menu, list)
    assert len(menu) == 5

def test_item_match(menu):
    assert item_match("mohinga", menu) == ("Mohinga (Fish Noodle Soup)", "$1.50")
    assert item_match("tea leaf salad", menu) == ("Laphet Thoke (Tea Leaf Salad)", "$1.20")
    assert item_match("pizza", menu) == None

def test_get_item_data(menu):
    assert get_item_data("mohinga", menu) == ("Mohinga (Fish Noodle Soup)", 1.50)
    assert get_item_data("shan noodles", menu) == ("Shan Khao Swe (Shan Noodles)", 1.80)
    assert get_item_data("coffee", menu) == None

def test_process_order(monkeypatch, menu):
    inputs = [
        "Mohinga, 2",
        "laphet thoke",
        "Mohinga (Fish Noodle Soup)",
        "fried dough stick, 4",
        "e"
    ]

    input_generator = (i for i in inputs)

    monkeypatch.setattr('builtins.input', lambda prompt: next(input_generator))

    expected_result = [
        {"Item": "Mohinga (Fish Noodle Soup)",
        "Quantity": 3,
        "Price": 1.50,
        "Total Price": 4.50},
        {"Item": "Laphet Thoke (Tea Leaf Salad)",
        "Quantity": 1,
        "Price": 1.20,
        "Total Price": 1.20},
        {"Item": "E Kya Kway (Fried Dough Stick)",
        "Quantity": 4,
        "Price": 0.80,
        "Total Price": 3.20}]

    result = process_order(menu)
    assert result == expected_result

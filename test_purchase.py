import pytest

@pytest.fixture
def SetUp():
    print("setup started")
    yield
    print("exited")

def test_AddItemtoCart(SetUp):
    print("Added successfully")

def test_RemoveItemfromCart(SetUp):
    print("Removed successfully")
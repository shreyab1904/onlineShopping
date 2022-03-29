import pytest

@pytest.fixture
def SetUp():
    print("Open Amazon")
    print("USER LOGGED IN")
    yield
    print("USER LOGGED OUT")
    print("Close Amazon")

def test_AddItemtoCart(SetUp):
    print("Added successfully")

def test_RemoveItemfromCart(SetUp):
    print("Removed successfully")
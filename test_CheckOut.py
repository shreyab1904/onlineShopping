import pytest

@pytest.fixture()
def SetUp():
    print("Open Amazon")
    print("USER LOGGED IN")
    yield
    print("USER LOGGED OUT")
    print("Close Amazon")

def test_placeOrder(SetUp):
    print("Placing order")

def test_makePayment(SetUp):
    print("Do payment")

def test_OrderConfirmation(SetUp):
    print("Order confirmed")


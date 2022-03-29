import pytest

@pytest.fixture(scope="session" , autouse=True)
def SetUp():
    print("Open Amazon")
    print("USER LOGGED IN")
    yield
    print("USER LOGGED OUT")
    print("Close Amazon")
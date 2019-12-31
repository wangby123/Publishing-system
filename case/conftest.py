import pytest
from page.login_page import login_cbxt

@pytest.fixture(scope="session")
def login(driver, host):

    login_cbxt(driver, host)

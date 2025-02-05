import pytest
import allure
from pages.orange_hrm.login_page import LoginPage
from pages.orange_hrm.dashboard_page import DashboardPage
from playwright.sync_api import Page
from data.test_credentials import bad_credentials


@pytest.mark.skip
@pytest.mark.orange
def test_validate_login_page_elements(setup_driver: Page):
    """
    Test Case: Verify a login page is loaded with expected page elements.

    Steps:
    1. Navigate to the login page.
    2. Assert expected login page components are visible and functional
        1. login header
        2. correct URL
        3. social icons
        4. main branding header/logo
        5. password reset link
    3. Assert a credential submission form is available and interactive
        1. user/pass input fields
        2. submission button
    2. Assert that login header, credentials form, password reset link are available
    """
    username = 'Admin'
    password = 'admin123'

    login_page = LoginPage(setup_driver)
    # login_page.navigate()

    # # Assert page elements are visible
    # assert login_page.get_page_header_login_text() == 'login', \
    #     'Credential form header login text not found'
    #
    # assert 'login' in login_page.page.url, 'The login page URL does not contain the text login'
    #
    # assert 'Forgot your password' in login_page.forgot_password_link.text_content(), \
    #     "The forgot password link was not visible"
    #
    # assert login_page.social_icons.count() == 4, \
    #     f'Expected 4 social icons but found {login_page.social_icons.count()} instead'

    # Input data into the credential fields
    login_page.fill_username(username)
    login_page.fill_password(password)

    # Assert input elements are visible and interactive
    assert login_page.username_input_field.input_value() == username, \
        'No username entry was found in the username field.'

    assert login_page.password_input_field.input_value() == password, \
        'No password entry was found in the username field.'

    assert login_page.submit_button is not None, 'No submit form button was found on the login page'


@pytest.mark.orange
@pytest.mark.parametrize("username, password", bad_credentials)
@allure.description("Verify incorrect credentials result in login page error message")
def test_login_incorrect_credentials(setup_driver: Page, username: str, password: str):
    """
    Test to check bad credentials result in an error page being shown.

    Parameterized to take a bad_credentials list of tuples from the data folder.

    """
    login_page = LoginPage(setup_driver)
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.submit_login()

    assert login_page.get_error_message() == "Invalid credentials", "No error message is displayed"


@pytest.mark.skip
@pytest.mark.orange
@allure.description("Verify dashboard page loads after login")
def test_dashboard_loads_after_login(setup_driver: Page):
    """
    Test to check bad credentials result in an error page being shown.

    Parameterized to take a bad_credentials list of tuples from the data folder.

    """
    username = "Admin"
    password = "admin123"

    login_page = LoginPage(setup_driver)
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.submit_login()

    dashboard_page = DashboardPage(setup_driver)

    assert dashboard_page.is_breadcrumb_visible(), "The dashboard page is not visible"

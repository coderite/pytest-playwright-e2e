from playwright.sync_api import Page, expect
from config import playwright_config
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    """
    Page Object Model for the Login Page of the Orange HRM demo site.

    This class encapsulates the interactions and elements of the login page,
    providing methods to perform actions such as filling in credentials and
    perform a login.
    """
    def __init__(self, page: Page):
        """
        Initializes the LoginPage with the given Playwright Page instance.

        Args:
            page (Page): The Playwright Page object representing the browser page.
        """
        self.page_login_header = "h5.orangehrm-login-title"
        self.username_input_field = "[name='username']"
        self.password_input_field = "[name='password']"
        self.submit_button = "[type='submit']"
        self.forgot_password_link = ".orangehrm-login-forgot > p"
        self.header_branding_image = ".orangehrm-login-branding > img"
        self.social_icons = "svg.orangehrm-sm-icon"
        self.alert_content_text = ".oxd-alert-content-text"
        self.error_container = "p.oxd-alert-content-text"

        self.page = page

    @allure.step("Enter username in login page")
    def fill_username(self, username: str) -> None:
        """
        Fills the username input field with the provided username.

        Args:
            username (str): The username to be entered into the username input field.
        """
        self.enter_text(page=self.page, selector=self.username_input_field, text_to_enter=username)

    @allure.step("Enter password in login page")
    def fill_password(self, password: str) -> None:
        """
        Fills the password input field with the provided password.

        Args:
            password (str): The password to be entered into the password input field.
        """
        self.enter_text(page=self.page, selector=self.password_input_field, text_to_enter=password)

    @allure.step("Click the submit button")
    def submit_login(self) -> None:
        """
        Clicks the submit button to attempt logging in with the provided credentials.
        """
        self.click(self.page, selector=self.submit_button)

    @allure.step("Retrieving error message from the login page")
    def get_error_message(self) -> str:
        """
        Retrieve the error message from the login page
        :return: A string containing the error text
        """
        return self.get_text_from_element(self.page, self.error_container)



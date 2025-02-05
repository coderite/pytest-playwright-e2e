from playwright.sync_api import Page
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        self.breadcrumb = '.oxd-topbar-header-breadcrumb-module'

        self.page = page

    def is_breadcrumb_visible(self) -> bool:
        return self.wait_for_visibility_of_element(page=self.page, selector=self.breadcrumb)

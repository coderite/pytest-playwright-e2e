from playwright.sync_api import Page, TimeoutError, Locator, expect


class BasePage:
    def wait_for_visibility_of_element(self, page: Page, selector: str, timeout: int = 20000, raise_error=True):
        try:
            element = page.locator(selector)
            element.wait_for(timeout=timeout, state='visible')
        except TimeoutError:
            if raise_error:
                raise ValueError(f'{selector} element not found after {timeout} of waiting.')

    def enter_text(self, page: Page, selector: str, text_to_enter: any, timeout: int = 20000):
        self.wait_for_visibility_of_element(page=page, selector=selector, timeout=timeout)
        locator = page.locator(selector)
        locator.fill(str(text_to_enter))

    def click(self, page: Page, selector: str, timeout: int = 20000):
        self.wait_for_visibility_of_element(page=page, selector=selector, timeout=timeout)
        locator = page.locator(selector)
        locator.click()

    def get_text_from_element(self, page: Page, selector: str, timeout: int = 20000):
        self.wait_for_visibility_of_element(page=page, selector=selector, timeout=timeout)
        return page.locator(selector).text_content().strip()


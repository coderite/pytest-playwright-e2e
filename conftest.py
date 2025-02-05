import allure
import pytest
from playwright.sync_api import Playwright, sync_playwright

from config import playwright_config


@pytest.fixture(scope='function')
def setup_driver():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set headless=True for CI
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()
        page.goto(playwright_config.orange_hrm_base_url)

        yield page

        # Attach video to Allure report
        video_path = context.pages[0].video.path()

        allure.attach.file(
            video_path,
            name="Video",
            attachment_type=allure.attachment_type.WEBM
        )

        context.close()
        browser.close()






import os


class PlaywrightConfig:
    def __init__(self):
        self.orange_hrm_base_url = os.getenv('ORANGE_HRM_LOGIN_URL')

        if not self.orange_hrm_base_url:
            raise ValueError('The Orange HRM base login URL not found in env variables')

    def __repr__(self):
        return f"PlaywrightConfig(orange_hrm_base_url={self.orange_hrm_base_url})"


# Instantiate a global PlaywrightConfig object for easy access
playwright_config = PlaywrightConfig()

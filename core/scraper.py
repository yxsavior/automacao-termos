from playwright.sync_api import sync_playwright
from config import BASE_URL
from core.logger import logger

class Scraper:

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(accept_downloads=True)
        self.page = self.context.new_page()

    def login(self, usuario, senha):
        try:
            self.page.goto(BASE_URL)
            self.page.fill('input[name="username"]', usuario)
            self.page.fill('input[name="password"]', senha)
            self.page.get_by_role("button", name="Login").click()
            self.page.wait_for_selector('h1:has-text("Termo")', timeout=15000)
            logger.info("Login realizado com sucesso")
        except Exception as e:
            logger.error(f"Erro no login: {e}")
            raise

    def close(self):
        self.browser.close()
        self.playwright.stop()
from tests.test_page import TestPage


def test_caption(driver, url):
    page = TestPage.with_driver(driver=driver, base_url=url)
    page.open_page()
    page.check_caption()


def test_paragraphs(driver, url):
    page = TestPage.with_driver(driver=driver, base_url=url)
    page.open_page()
    page.check_paragraphs()


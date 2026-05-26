import sys
from playwright.sync_api import sync_playwright

url = sys.argv[1]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url, wait_until="networkidle", timeout=30000)
    page.wait_for_selector('[data-track-load="description_content"]', timeout=15000)
    title = page.query_selector('div[class*="text-title-large"]')
    desc = page.query_selector('[data-track-load="description_content"]')
    print("=== TITLE ===")
    print(title.inner_text() if title else "(title not found)")
    print("\n=== DESCRIPTION ===")
    print(desc.inner_text() if desc else "(description not found)")
    browser.close()

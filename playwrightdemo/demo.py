import asyncio
from playwright.async_api import async_playwright, TimeoutError

async def scrape_himalayas():

    async with async_playwright() as p:

        # Launch Microsoft Edge
        browser = await p.chromium.launch(
            channel="msedge",
            headless=False
        )

        context = await browser.new_context()
        page = await context.new_page()

        # Open Bing
        await page.goto("https://www.bing.com")

        # Handle Cookie Popup (if appears)
        try:
            await page.wait_for_selector("xpath=//button[@id='bnp_btn_accept']", timeout=5000)
            await page.click("xpath=//button[@id='bnp_btn_accept']")
            print("Cookie accepted")
        except TimeoutError:
            print("No cookie popup")
        

        # Use YOUR XPath for search box
        await page.wait_for_selector("xpath=//*[@id='sb_form_q']", state="visible")

        # Search Himalayas
        await page.fill("xpath=//*[@id='sb_form_q']", "Himalayas")
        await page.keyboard.press("Enter")

        # Wait for search results (stable XPath)
        await page.wait_for_selector("xpath=(//h2/a)[1]", timeout=15000)

        # Click first search result
        await page.click("xpath=(//h2/a)[1]")

        # Wait for page to load completely
        await page.wait_for_load_state("networkidle")

        # Scrape paragraph text
        paragraphs = await page.locator("xpath=//p").all_inner_texts()
        page_text = "\n".join(paragraphs)

        # Save to text.txt
        with open("text.txt", "w", encoding="utf-8") as f:
            f.write(page_text)

        print("✅ Scraped text saved into text.txt")

        await browser.close()

# Run async function
asyncio.run(scrape_himalayas())

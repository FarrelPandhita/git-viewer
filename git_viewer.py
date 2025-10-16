# WARNING: Run this ONLY against servers you own or have permission to test.
# Save as play_visitors_async_safe.py and run in a Jupyter/Colab or async-capable env.
from playwright.async_api import async_playwright
import asyncio, random, datetime

# CHANGE THIS to your local/staging URL that you own
URL = "https://github.com/FarrelPandhita"
VISIT_COUNT = 10000

# faster timings for testing (be conservative in real tests!)
MIN_VIEW_SECONDS = 0.5   # simulate shorter "read" time
MAX_VIEW_SECONDS = 2.0
MIN_INTER_DELAY = 0.05   # short pause between visits
MAX_INTER_DELAY = 0.25

# A short list of user agents for basic rotation (keep it realistic)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
]

async def visit_once(page, idx):
    """
    Visit the URL once and log info.
    Returns a tuple (success:bool, status:int or None).
    """
    try:
        # navigate and wait for network idle (adjust if page loads indefinitely)
        response = await page.goto(URL, wait_until="networkidle", timeout=30000)
        status = response.status if response else None
        now = datetime.datetime.utcnow().isoformat() + "Z"
        print(f"[{idx}] visited at {now} status={status}")
        return True, status
    except Exception as e:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        print(f"[{idx}] error at {now}: {e}")
        return False, None

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for i in range(VISIT_COUNT):
            ua = random.choice(USER_AGENTS)
            context = await browser.new_context(user_agent=ua)
            page = await context.new_page()
            succes, status = await visit_once(page, i+1)
            # simulate some on-page time (shortened for faster test)
            await asyncio.sleep(random.uniform(MIN_VIEW_SECONDS, MAX_VIEW_SECONDS))
            # small scroll to simulate activity
            try:
                await page.mouse.wheel(0, 300)
            except Exception:
                pass
            await context.close()
            # short randomized pause before next visit
            await asyncio.sleep(random.uniform(MIN_INTER_DELAY, MAX_INTER_DELAY))
        await browser.close()

# If running in a notebook/Colab: use "await main()"
# If running as a standalone script, wrap with asyncio.run(main())
# Running inside Jupyter/Colab
await main()

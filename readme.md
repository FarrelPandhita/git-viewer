<p align="center"><img src="https://socialify.git.ci/FarrelPandhita/git-viewer/image?custom_description=A+high-performance+asynchronous+web+visitor+tool+built+with+Playwright+for+testing%2C+monitoring%2C+and+analyzing+web+page+performance+under+load.&amp;description=1&amp;font=JetBrains+Mono&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Floating+Cogs&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

# git-viewer

A high-performance asynchronous web visitor tool built with Playwright for testing, monitoring, and analyzing web page performance under load.

## 📋 Features

- **Asynchronous Execution**: Efficiently handles thousands of concurrent page visits using async/await patterns
- **Realistic User Simulation**: Rotates user agents and simulates natural browsing behavior (scrolling, read time)
- **Configurable Parameters**: Easy customization of visit counts, timeouts, delays, and viewing durations
- **Error Handling**: Robust exception handling with detailed logging for troubleshooting
- **Network Monitoring**: Tracks HTTP response statuses and network idle states
- **Headless Browser**: Runs without GUI overhead for faster, resource-efficient testing

## ⚙️ Requirements

- Python 3.7+
- Playwright
- Asyncio (built-in with Python)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/FarrelPandhita/git-viewer.git
cd git-viewer
```

2. Install dependencies:
```bash
pip install playwright
```

3. Install browser binaries:
```bash
playwright install chromium
```

## 📖 Usage

### Configuration

Before running, edit the configuration variables in `play_visitors_async_safe.py`:

```python
URL = "https://example.com"              # Target URL to visit
VISIT_COUNT = 10000                      # Number of page visits
MIN_VIEW_SECONDS = 0.5                   # Minimum time spent on page
MAX_VIEW_SECONDS = 2.0                   # Maximum time spent on page
MIN_INTER_DELAY = 0.05                   # Min delay between visits
MAX_INTER_DELAY = 0.25                   # Max delay between visits
```

### Running in Jupyter/Colab

```python
await main()
```

### Running as Standalone Script

```bash
python play_visitors_async_safe.py
```

Alternatively, wrap the execution with asyncio:

```python
if __name__ == "__main__":
    asyncio.run(main())
```

## 🔍 How It Works

1. **Initialization**: Launches a headless Chromium browser with async Playwright
2. **User Agent Rotation**: Randomly selects from a pool of realistic user agents for each visit
3. **Page Visit**: Navigates to the target URL and waits for network idle state
4. **Interaction**: Simulates user activity (scrolling, viewing time)
5. **Logging**: Records visit status, timing, and any errors
6. **Cleanup**: Closes browser contexts and pages between visits

### Key Functions

- `visit_once(page, idx)`: Executes a single page visit and captures response status
- `main()`: Orchestrates the browser session and manages the visit loop

## ⚠️ Important Notes

**Use Responsibly**: This tool should only be used against servers you own or have explicit permission to test. Unauthorized load testing may violate terms of service and applicable laws.

### Testing Best Practices

- Start with smaller `VISIT_COUNT` values (e.g., 100) to test your setup
- Adjust timing parameters based on target page complexity
- Monitor server resources during testing
- Space out large test runs to avoid overwhelming infrastructure

## 🛠️ Customization

### Adding More User Agents

Expand the `USER_AGENTS` list to include additional browser signatures:

```python
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0)...",
    # Add more agents
]
```

### Adjusting Timeouts

Modify the `goto()` timeout parameter:

```python
response = await page.goto(URL, wait_until="networkidle", timeout=60000)  # 60 seconds
```

### Custom Request Headers

Add custom headers to simulate specific client types:

```python
context = await browser.new_context(
    user_agent=ua,
    extra_http_headers={"Accept-Language": "en-US,en;q=0.9"}
)
```

## 📊 Output

The tool logs each visit with:
- Visit index number
- ISO 8601 timestamp
- HTTP response status code
- Any errors encountered

Example output:
```
[1] visited at 2024-01-15T10:30:45.123Z status=200
[2] visited at 2024-01-15T10:30:46.456Z status=200
[3] error at 2024-01-15T10:30:47.789Z: Timeout waiting for network idle
```

## 🐛 Troubleshooting

**Browser crashes**: Increase `MIN_VIEW_SECONDS` or reduce `VISIT_COUNT`

**Timeout errors**: Increase the `timeout` parameter in `page.goto()`

**High memory usage**: Reduce `VISIT_COUNT` or add garbage collection between iterations

**Rate limiting**: Increase `MAX_INTER_DELAY` to reduce request frequency

## 📝 License

This project is provided as-is. Ensure compliance with your target website's terms of service and local regulations.

## 👤 Author

**Farrel Pandhita**
- GitHub: [@FarrelPandhita](https://github.com/FarrelPandhita)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

**Disclaimer**: This tool is intended for authorized testing only. The author assumes no responsibility for misuse or unauthorized testing against third-party servers.

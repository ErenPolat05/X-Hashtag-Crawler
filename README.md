# 🐦 Tweet Fetcher

A Python bot that automates Twitter (X) login using Selenium, searches for any hashtag, scrolls through the timeline, and saves fetched tweets into a `.txt` file.

---

## 🚀 Features

- ✅ Logs into Twitter (X) automatically
- 🔍 Searches for a given hashtag
- 🧭 Scrolls dynamically to load more tweets
- 📝 Saves tweet contents locally into `tweetdepo.txt`
- 🌐 Multi-language ready (sets browser to English for stability)

---

## 📦 Requirements

- Python 3.8+
- Google Chrome installed
- ChromeDriver (automatically managed by `webdriver_manager`)

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/tweet-fetcher.git
cd tweet-fetcher
pip install -r requirements.txt

!!!!!
You can import the email, password and username information yourself from another .py file.
!!!!!

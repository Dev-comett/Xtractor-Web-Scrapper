# Xtractor Web Scraper

> **Web Scraping Made Easy**  
> A lightweight Streamlit app to perform Google SERP scraping and live-URL extraction, with built-in weather & news widgets.

---

## 🚀 Features

- **Advanced Google Scraper**  
  Fetches top organic results for any query via SerpAPI, displaying title, snippet and clickable links.  
- **Live Website Scraper**  
  Extracts the first paragraphs from any URL.  
- **Weather & News Sidebar**  
  Real-time weather (Tomorrow.io) and top news (NewsAPI) in a persistent right sidebar.  
- **Dark-mode UI**  
  Sleek, mobile-friendly design with customizable banner.  

---

## 🔧 Prerequisites

- Python 3.8+  
- A free SerpAPI key (for Google scraping)  
- A Tomorrow.io API key (weather)  
- A NewsAPI key (news)  

Store your keys in `.streamlit/secrets.toml`:

```toml
SERP_API_KEY = "your_serpapi_key"
TOMORROW_API_KEY = "your_tomorrowio_key"
NEWS_API_KEY = "your_newsapi_key"

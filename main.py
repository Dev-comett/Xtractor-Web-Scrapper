import streamlit as st
import requests
from streamlit_option_menu import option_menu
from bs4 import BeautifulSoup
import re

# --- Config ---
st.set_page_config(page_title="Xtractor", layout="wide", page_icon="😎")

SERP_API_KEY     = st.secrets["SERP_API_KEY"]
TOMORROW_API_KEY = st.secrets["TOMORROW_API_KEY"]
NEWS_API_KEY     = st.secrets["NEWS_API_KEY"]

# --- Global Styles ---
st.markdown("""
    <style>
      body, .stApp { background: #111; color: #f5f5f5; }
      h1, h2, h3 { color: #ff9900; }
      a { color: #ff9900 !important; text-decoration: underline; }
      .block-container { padding-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar (persistent) ---
with st.sidebar:
    st.title("Xtractor")
    st.markdown("<p style='color:#ccc;'>Web Scraping Made Easy</p>", unsafe_allow_html=True)
    page = option_menu(None,
        ["Home😴", "Web Scraper🔎"],
        icons=["house-fill","search"],
        default_index=0,
        orientation="vertical"
    )

# --- Home Page ---
if page == "Home😴":
    # Two columns: left for banner & placeholder, right for weather/news
    main, sidebar = st.columns([3, 1])

    with main:
        # show banner1.png at top of main area
        st.image('banner1.png', use_column_width=True)
        # placeholder message below
        st.markdown(
            "<div style='height:50vh; display:flex; align-items:center; justify-content:center;'>"
            "<h2 style='color:#888;'>More features coming soon…</h2>"
            "</div>",
            unsafe_allow_html=True
        )

    with sidebar:
        st.subheader("🌡️ Weather")
        city = st.text_input("Enter city", "New York")
        if city:
            try:
                w = requests.get(
                    f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={TOMORROW_API_KEY}"
                ).json()['data']['values']
                st.success(f"{city.title()}: {w['temperature']}°C, Humidity {w['humidity']}%, Wind {w['windSpeed']} kph")
            except:
                st.warning("⚠️ Weather data unavailable.")

        st.subheader("📰 Top News")
        kw = st.text_input("News keyword", "technology")
        if kw:
            try:
                articles = requests.get(
                    f"https://newsapi.org/v2/everything?q={kw}&apiKey={NEWS_API_KEY}"
                    "&language=en&sortBy=publishedAt&pageSize=5"
                ).json().get("articles", [])
                for art in articles:
                    st.markdown(f"**[{art['title']}]({art['url']})**")
                    st.caption(art.get("description", ""))
            except:
                st.warning("News API error.")

# --- Web Scraper Page ---
else:
    st.header("🔍 Web Scraper")
    query = st.text_input("Enter search query")
    if st.button("Scrape it 🔨") and query:
        try:
            data = requests.get(
                f"https://serpapi.com/search.json?q={query}&engine=google&api_key={SERP_API_KEY}"
            ).json().get("organic_results", [])
            if not data:
                st.info("No results found.")
            for res in data:
                title   = res.get("title","No Title")
                link    = res.get("link","#")
                snippet = res.get("snippet","")
                st.markdown(f"**[{title}]({link})**")
                if snippet:
                    st.write(snippet)
                st.markdown("---")
        except Exception as e:
            st.error(f"Search error: {e}")
# --- Footer ---
st.markdown("""
    <hr style='border-color: #333;'>
    <div style='text-align:center; padding:10px; color:#888'>
        Made with ❤️ by Im_Dev | 
        <a href='https://github.com/Dev-comett' target='_blank'>GitHub</a> • 
        <a href='https://www.linkedin.com/in/dev-ice' target='_blank'>LinkedIn</a>
    </div>
""", unsafe_allow_html=True)

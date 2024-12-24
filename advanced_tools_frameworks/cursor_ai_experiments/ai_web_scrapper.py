import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get Google API key from environment
api_key = os.getenv("GOOGLE_API_KEY")

# Streamlit app title
st.title("AI Web Scraper")

# Input fields for user prompt and source URL
prompt = st.text_input("Enter the information you want to extract:")
source_url = st.text_input("Enter the source URL:")

# Configuration for the scraping pipeline
graph_config = {
    "llm": {
        "api_key": api_key,
        "model": "gemini-1.5-flash",
    },
    "verbose": True,
    "headless": False,
}

# Button to start the scraping process
if st.button("Scrape"):
    if prompt and source_url:
        if api_key:
            # Create the SmartScraperGraph instance
            smart_scraper_graph = SmartScraperGraph(
                prompt=prompt,
                source=source_url,
                config=graph_config
            )

            # Run the pipeline
            result = smart_scraper_graph.run()

            # Display the result
            st.write(result)
        else:
            st.error("API key is missing. Please check your .env file.")
    else:
        st.error("Please provide the required inputs (prompt and source URL).")

# Instructions for the user
st.markdown("""
### Instructions
1. Enter the information you want to extract in the first input box.
2. Enter the source URL from which you want to extract the information.
3. Click on the "Scrape" button to start the scraping process.
4. Ensure that the Google API key is set in the .env file as `GOOGLE_API_KEY`.
""")

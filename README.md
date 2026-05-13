# 👑 Clash Royale Collection Level Calculator

A lightweight web application built with Python and Streamlit to help Clash Royale players calculate their exact Collection Level ahead of the massive update.

You can try the live web app here: collvl.streamlit.app


# What it Does:

With the removal of the old King Level system, progression is now tied directly to your entire inventory. This tool uses the official Clash Royale API to calculate exactly which transition reward bin you will fall into when the update drops.

It automatically handles the math for:

Standard card absolute levels

Tower Troop absolute levels

The flat +5 bonus for unlocked Evolutions

The flat +5 bonus for unlocked Hero variants

Note: Champions are calculated at their standard unlock level (11) and do not receive the +5 form bonus.


# How it Works:

This project uses Streamlit for the frontend UI and the Python requests library to fetch JSON data.

Because official Supercell API keys are strictly IP-locked, this tool relies on a static API key routed through the RoyaleAPI Community Proxy (proxy.royaleapi.dev). This allows the cloud-hosted Streamlit app to reliably fetch player data without triggering IP mismatch errors (403 Forbidden).


# Running it Locally:

If you want to clone this repository and run it yourself, you will need your own API key:

Clone the repository: git clone https://github.com/RedditProj/ColLvl.git

Install the requirements: pip install streamlit requests

Set up a .streamlit/secrets.toml file in the root directory and add your key: CR_API_KEY = "your_key_here"

Run the app: streamlit run app.py


# License:

This project is licensed under the MIT License - see the LICENSE file for details.

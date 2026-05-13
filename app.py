import requests
import streamlit as st

st.set_page_config(page_title="CR Collection Level Calc", page_icon="👑")

st.title("👑 Clash Royale Collection Level Calculator")
st.markdown("Find out exactly which **2026 Celebration Reward Bin** you fall into before the update drops!")

# Secret key in Streamlit's dashboard
API_KEY = st.secrets["CR_API_KEY"] 

player_tag = st.text_input("Enter your Player Tag (with or without #):", placeholder="e.g. 2PP")
col1, col2 = st.columns(2)
with col1:
    evo_count = st.number_input("How many Evolutions do you have unlocked?", min_value=0, max_value=50, value=0)
with col2:
    hero_count = st.number_input("How many Hero Variants (NOT Champions) do you have unlocked?", min_value=0, max_value=50, value=0)

def get_reward_bin(level):
    if level < 20: return "None (Level too low)"
    elif level <= 200: return "Level 20 - 200: 500 Gems, 1x 5-Star Chest"
    elif level <= 400: return "Level 201 - 400: 750 Gems, 1x 5-Star Chest"
    elif level <= 600: return "Level 401 - 600: 1,000 Gems, 1x 5-Star Chest"
    elif level <= 800: return "Level 601 - 800: 1,500 Gems, 1x 5-Star Chest"
    elif level <= 1000: return "Level 801 - 1000: 2,000 Gems, 1x 5-Star Chest, 1x Banner"
    elif level <= 1200: return "Level 1001 - 1200: 2,500 Gems, 1x 5-Star Chest, 2x Banners"
    elif level <= 1400: return "Level 1201 - 1400: 3,000 Gems, 1x 5-Star Chest, 3x Banners"
    elif level <= 1600: return "Level 1401 - 1600: 3,500 Gems, 2x 5-Star Chests, 4x Banners"
    elif level <= 1800: return "Level 1601 - 1800: 4,000 Gems, 2x 5-Star Chests, 5x Banners"
    elif level <= 2000: return "Level 1801 - 2000: 4,500 Gems, 3x 5-Star Chests, 6x Banners"
    else: return "Level 2001+: 5,000 Gems, 3x 5-Star Chests, 6x Banners, 1x Exclusive Tower Skin"

if st.button("Calculate My Level!", type="primary"):
    if not player_tag:
        st.warning("Please enter a player tag!")
    else:
        with st.spinner("Fetching data from Supercell..."):
            clean_tag = player_tag.replace('#', '').upper()
            
            # RoyaleAPI proxy to bypass the strict IP whitelisting
            url = f"https://proxy.royaleapi.dev/v1/players/%23{clean_tag}"
            headers = {"Authorization": f"Bearer {API_KEY}"}
            
            try:
                response = requests.get(url, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    total_level = 0
                    
                    for card in data.get('cards', []):
                        rarity = card.get('rarity', '').lower()
                        relative_level = card.get('level', 0)
                        
                        if rarity == 'common': absolute_level = relative_level
                        elif rarity == 'rare': absolute_level = relative_level + 2
                        elif rarity == 'epic': absolute_level = relative_level + 5
                        elif rarity == 'legendary': absolute_level = relative_level + 8
                        elif rarity == 'champion': absolute_level = relative_level + 10
                        else: absolute_level = relative_level 
                            
                        total_level += absolute_level

                    total_level += (hero_count * 5)
                    total_level += (evo_count * 5)
                    
                    st.success(f"### Your Exact Collection Level is: **{total_level}**")
                    st.info(f"🎁 **Your Reward Bracket:** {get_reward_bin(total_level)}")
                    
                elif response.status_code == 404:
                    st.error("Player tag not found. Check for typos (Remember: no letter 'O's, only the number '0').")
                elif response.status_code == 403:
                    st.error("API Key error. The proxy might be blocking the request or the key is invalid.")
                else:
                    st.error(f"Error fetching data: {response.status_code}")
                    
            except Exception as e:
                st.error(f"Failed to connect to the API: {e}")

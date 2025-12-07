import streamlit as st
import pandas as pd

# ==========================================
# 1. DATABASE (The "Brain" of the App)
# ==========================================

# MAPS DATABASE (Expanded to all maps through v52 - FINAL LIST)
maps_db = [
    # BEGINNER MAPS (21)
    {"name": "Monkey Meadow", "difficulty": "Beginner", "features": ["Standard", "Long"]},
    {"name": "Logs", "difficulty": "Beginner", "features": ["Standard", "Long"]},
    {"name": "Tree Stump", "difficulty": "Beginner", "features": ["Standard"]},
    {"name": "Town Center", "difficulty": "Beginner", "features": ["Standard"]},
    {"name": "Resort", "difficulty": "Beginner", "features": ["Standard", "Loop"]},
    {"name": "Skates", "difficulty": "Beginner", "features": ["Standard", "Loop"]},
    {"name": "Scoop", "difficulty": "Beginner", "features": ["Standard"]},
    {"name": "Alpine Run", "difficulty": "Beginner", "features": ["Standard"]},
    {"name": "Frozen Over", "difficulty": "Beginner", "features": ["Ice/Obstacle"]},
    {"name": "Cubism", "difficulty": "Beginner", "features": ["Water", "Standard"]},
    {"name": "Four Circles", "difficulty": "Beginner", "features": ["Standard"]},
    {"name": "Hedge", "difficulty": "Beginner", "features": ["Obstacle", "Short"]},
    {"name": "End of the Road", "difficulty": "Beginner", "features": ["Standard"]},
    {"name": "Water Park", "difficulty": "Beginner", "features": ["Water", "Moving"]},
    {"name": "Polyphemus", "difficulty": "Beginner", "features": ["LOS"]},
    {"name": "Covered Gardens", "difficulty": "Beginner", "features": ["Obstacle"]},
    {"name": "Quarry", "difficulty": "Beginner", "features": ["LOS", "Button"]},
    {"name": "Quiet Street", "difficulty": "Beginner", "features": ["Standard"]},
    {"name": "Bloonarius Prime", "difficulty": "Beginner", "features": ["Standard"]},
    {"name": "Lotus Island", "difficulty": "Beginner", "features": ["Water", "Stun"]},
    {"name": "KingoftheSea", "difficulty": "Beginner", "features": ["Water"]},

    # INTERMEDIATE MAPS (19) - ADDED: LOST CREVASSE, LUMINOUS COVE
    {"name": "In The Loop", "difficulty": "Intermediate", "features": ["Loop"]},
    {"name": "Middle of the Road", "difficulty": "Intermediate", "features": ["Standard"]},
    {"name": "One Two Tree", "difficulty": "Intermediate", "features": ["Standard"]},
    {"name": "Scrapyard", "difficulty": "Intermediate", "features": ["Obstacle"]},
    {"name": "The Cabin", "difficulty": "Intermediate", "features": ["Obstacle"]},
    {"name": "Encrypted", "difficulty": "Intermediate", "features": ["Obstacle", "Graveyard"]},
    {"name": "Bazaar", "difficulty": "Intermediate", "features": ["Standard"]},
    {"name": "Adora's Temple", "difficulty": "Intermediate", "features": ["Standard"]},
    {"name": "Spring Spring", "difficulty": "Intermediate", "features": ["Water", "Standard"]},
    {"name": "KartsNDarts", "difficulty": "Intermediate", "features": ["Obstacles", "Moving"]},
    {"name": "Moon Landing", "difficulty": "Intermediate", "features": ["Standard", "Gimmick"]},
    {"name": "Haunted", "difficulty": "Intermediate", "features": ["LOS", "Gimmick"]},
    {"name": "Downstream", "difficulty": "Intermediate", "features": ["Water", "Standard"]},
    {"name": "Firing Range", "difficulty": "Intermediate", "features": ["LOS", "Standard"]},
    {"name": "Cracked", "difficulty": "Intermediate", "features": ["Multi", "Standard"]},
    {"name": "Streambed", "difficulty": "Intermediate", "features": ["Water", "Split Path"]},
    {"name": "Spice Islands", "difficulty": "Intermediate", "features": ["Water", "Limited Land"]},
    {"name": "Lost Crevasse", "difficulty": "Intermediate", "features": ["Gimmick", "Split Path", "LOS"]},
    {"name": "Luminous Cove", "difficulty": "Intermediate", "features": ["Water", "Gimmick"]},
    
    # ADVANCED MAPS (14) - ADDED: TINKERTON
    {"name": "Chutes", "difficulty": "Advanced", "features": ["LOS", "Standard"]},
    {"name": "Rake", "difficulty": "Advanced", "features": ["Standard"]},
    {"name": "Dark Path", "difficulty": "Advanced", "features": ["LOS", "Short"]},
    {"name": "Erosion", "difficulty": "Advanced", "features": ["Water", "Gimmick"]},
    {"name": "Midnight Mansion", "difficulty": "Advanced", "features": ["LOS", "Gimmick"]},
    {"name": "Sunken Columns", "difficulty": "Advanced", "features": ["Water", "LOS"]},
    {"name": "X Factor", "difficulty": "Advanced", "features": ["Multi", "LOS"]},
    {"name": "Mesa", "difficulty": "Advanced", "features": ["Multi", "Short"]},
    {"name": "Geared", "difficulty": "Advanced", "features": ["Gimmick", "Rotating"]},
    {"name": "Spillway", "difficulty": "Advanced", "features": ["Water", "Gimmick"]},
    {"name": "Cargo", "difficulty": "Advanced", "features": ["Water", "Gimmick"]},
    {"name": "Pat's Pond", "difficulty": "Advanced", "features": ["Water", "LOS"]},
    {"name": "Peninsula", "difficulty": "Advanced", "features": ["Water", "Limited Land"]},
    {"name": "Tinkerton", "difficulty": "Advanced", "features": ["Gimmick", "Obstacle"]},

    # EXPERT MAPS (10) - ADDED: TRICKY TRACKS
    {"name": "High Finance", "difficulty": "Expert", "features": ["Short", "Gimmick"]},
    {"name": "Another Brick", "difficulty": "Expert", "features": ["Split Path", "Standard"]},
    {"name": "Off The Coast", "difficulty": "Expert", "features": ["Water", "Standard"]},
    {"name": "Cornfield", "difficulty": "Expert", "features": ["Obstacles", "No Water"]},
    {"name": "Underground", "difficulty": "Expert", "features": ["Multi", "Gimmick"]},
    {"name": "Glacial Trail", "difficulty": "Expert", "features": ["Standard"]},
    {"name": "Dark Dungeons", "difficulty": "Expert", "features": ["LOS", "Short"]},
    {"name": "Sanctuary", "difficulty": "Expert", "features": ["Multi", "Moving"]},
    {"name": "Ravine", "difficulty": "Expert", "features": ["Standard", "Gimmick"]},
    {"name": "Tricky Tracks", "difficulty": "Expert", "features": ["New", "Short", "No LOS"]},

    # EXTREME MAPS (The true hardest ones - 9)
    {"name": "Flooded Valley", "difficulty": "Expert", "features": ["Water", "Flood", "Gimmick"]},
    {"name": "Infernal", "difficulty": "Expert", "features": ["LOS", "Multi"]},
    {"name": "Bloody Puddles", "difficulty": "Expert", "features": ["Multi", "Short", "Water", "Limited Land"]},
    {"name": "Workshop", "difficulty": "Expert", "features": ["Multi", "Gimmick"]},
    {"name": "Quad", "difficulty": "Expert", "features": ["Multi", "LOS", "Short"]},
    {"name": "Dark Castle", "difficulty": "Expert", "features": ["Multi", "Water", "Short"]},
    {"name": "Muddy Puddles", "difficulty": "Expert", "features": ["Multi", "Water", "LOS"]},
    {"name": "Ouch", "difficulty": "Expert", "features": ["Multi", "LOS", "Short"]},
    {"name": "Blons", "difficulty": "Expert", "features": ["Short", "Gimmick"]},
]

# STRATEGY DATABASE (No change to strats, keeping low-micro focus)
strategies_db = [
    # --- ORIGINAL LOW-MICRO SET ---
    {
        "name": "Druid of Wrath Poplustball",
        "heroes": ["Obyn Greenfoot"],
        "tier": "A",
        "tags": ["Standard", "Centralized", "Magic", "Low-Micro"],
        "desc": "Surround Obyn with 5 Poplust Druids and 1 Avatar of Wrath.",
        "path": "Start: Ninja (4-0-1) + Alch (4-2-0) -> Mid: 6x Druids (0-1-4) -> Late: Avatar of Wrath (0-2-5).",
        "support": "Village (2-3-0) for MIB is mandatory for DDTs."
    },
    {
        "name": "Sub Commander Flotilla",
        "heroes": ["Admiral Brickell", "Pat Fusty"],
        "tier": "S",
        "tags": ["Water", "Flood", "Low-Micro"],
        "desc": "Massive damage for water maps using Brickell's level 3 ability.",
        "path": "Start: Sub (2-0-2) -> Mid: Sub Commander (2-0-5) -> Late: Pre-Emptive Strike (2-5-0).",
        "support": "Alchemist (4-2-0) on the Commander. Engineer (0-4-0) to Overclock Commander."
    },
    {
        "name": "Tack Zone Icicle Impale",
        "heroes": ["Sauda", "Gwendolin"],
        "tier": "A",
        "tags": ["Loop", "Centralized", "Standard", "Low-Micro"],
        "desc": "High DPS in a small area. Requires a good corner.",
        "path": "Start: Tack (2-0-3) -> Mid: Tack Zone (2-0-5) -> Late: Super Brittle (5-2-0) Ice.",
        "support": "Village (4-2-0) Primary Training. Alchemist (4-2-0)."
    },
    {
        "name": "Mauler/Assassin Spam",
        "heroes": ["Striker Jones"],
        "tier": "B",
        "tags": ["Split Path", "Standard", "Low-Micro"],
        "desc": "Anti-MOAB specialized strat. Weak vs Ceramics without support.",
        "path": "Start: Bomb (0-0-0) -> Mid: 6x MOAB Maulers (1-3-0) -> Late: MOAB Eliminator (0-5-0).",
        "support": "Village (4-2-0) is mandatory. Ice (0-2-4) to catch Ceramics."
    },
    {
        "name": "Geraldo Turret Save-Up",
        "heroes": ["Geraldo"],
        "tier": "S",
        "tags": ["Expert", "Multi", "No Water", "Low-Micro"],
        "desc": "Use Geraldo's shop items to save money for expensive T5s.",
        "path": "Start: Geraldo Shooty Turrets -> Mid: Sniper (0-5-2) -> Late: Any expensive T5 (e.g. Pouakai).",
        "support": "Pickles on low attack speed towers. Sharpening Stone on Sharp towers."
    },
    {
        "name": "Grandmaster Ninja Shinobi Spam",
        "heroes": ["Pat Fusty"],
        "tier": "A",
        "tags": ["Centralized", "Standard", "Short", "Low-Micro"],
        "desc": "Classic strat. Surround Grandmaster with 20 Shinobis to max attack speed.",
        "path": "Start: Ninja (4-0-1) -> Mid: Grandmaster (5-0-2) -> Late: 20x Shinobis (0-3-0).",
        "support": "Pat Fusty's Roar (Lvl 3) multiplies the Ninja's damage massively. Total Transformation Alch is a fun variant."
    },
    # --- NEW PASSIVE SET ---
    {
        "name": "Permaspike Defense (BAD Killer)",
        "heroes": ["Ezili"],
        "tier": "A",
        "tags": ["Standard", "Late Game", "Low-Micro"],
        "desc": "Highly passive strategy focused on piling up spikes at the track exit. Ezili handles Round 100 with Hex.",
        "path": "Start: Dart/Hero -> Mid: Alch (4-2-0) + Permaspike (0-2-5) -> Late: Overclock (0-4-0) and Homeland Defense (5-2-0) on Spactory.",
        "support": "Ezili's Hex ability is critical for the final BAD on Round 100. Must have Monkey Intelligence Bureau (3-x-x Village)."
    },
    {
        "name": "Pat Fusty Glue Lord",
        "heroes": ["Pat Fusty"],
        "tier": "B",
        "tags": ["Standard", "Centralized", "Crowd Control", "Low-Micro"],
        "desc": "Pat's stun and roar heavily buff the Boomerang's fast attack speed. Excellent for mass ceramics and MOABs.",
        "path": "Start: Boomer (3-2-0) -> Mid: Glue Gunner (0-2-5) + Pat -> Late: Glaive Lord (5-2-0) and Super Maelstrom (0-5-2).",
        "support": "Village (2-3-0) for MIB and attack speed. Glue slows the cleanup."
    },
    {
        "name": "MAD Global Damage",
        "heroes": ["Etienne"],
        "tier": "S",
        "tags": ["Multi", "Expert", "No LOS", "Low-Micro"],
        "desc": "Etienne provides global camo, allowing the MAD to automatically aim and destroy MOAB-class bloons anywhere on the map.",
        "path": "Start: Dartling (2-0-3) -> Mid: MAD (0-5-2) -> Late: Sky Shredder (5-0-1) for ceramic cleanup.",
        "support": "Alchemist (4-2-0) on the MAD is non-negotiable. Place Etienne centrally."
    },
    {
        "name": "Ezili MOAB Hex Stall",
        "heroes": ["Ezili"],
        "tier": "A",
        "tags": ["Advanced", "Late Game", "Alternate Bloon Rounds", "Low-Micro"],
        "desc": "The 'Anti-BAD' strat. Ezili kills Round 100 easily. You just need to survive until then.",
        "path": "Start: Prince of Darkness (0-2-5) -> Mid: Carpet of Spikes (2-5-0) -> Late: Ezili Level 20.",
        "support": "Use Energizer Sub (5-0-0) to reduce Ezili's cooldowns so she can Hex every MOAB wave."
    },
    {
        "name": "Psi & Sniper Stun",
        "heroes": ["Psi"],
        "tier": "B",
        "tags": ["Expert", "Multi", "No LOS", "Low-Micro"],
        "desc": "Infinite stalling. Snipers stun MOABs in place while Psi kills them globally. Very hands-off after setup.",
        "path": "Start: Sniper (1-0-0) -> Mid: Elite Sniper (0-5-2) -> Late: Maim MOAB (4-2-0) on Strong.",
        "support": "Downdraft Heli (0-3-0) to blow ceramics back. This is a very slow, patient strategy."
    },
]

# ==========================================
# 2. APP LOGIC (No Change from previous version)
# ==========================================

st.set_page_config(page_title="BTD6 Strat Picker (v52)", layout="wide")

st.title("🎈 BTD6 Strategy Companion (v52)")
st.markdown("Select your mission parameters to get the best updated strategies.")

# --- SIDEBAR FILTERS ---
st.sidebar.header("Mission Briefing")

# 1. Select Map
map_names = sorted([m["name"] for m in maps_db])
selected_map_name = st.sidebar.selectbox("Select Map", ["Any"] + map_names)

# 2. Select Hero (Optional)
hero_options = set()
for s in strategies_db:
    for h in s["heroes"]:
        hero_options.add(h)
selected_hero = st.sidebar.selectbox("Preferred Hero (Optional)", ["Any"] + sorted(list(hero_options)))

# 3. Difficulty
difficulty = st.sidebar.radio("Difficulty Mode", ["Hard", "Impoppable", "CHIMPS"])

# --- FILTERING LOGIC ---

# Get features of selected map
selected_map_features = []
if selected_map_name != "Any":
    map_data = next((item for item in maps_db if item["name"] == selected_map_name), None)
    if map_data:
        selected_map_features = map_data["features"]
        st.sidebar.info(f"Map Type: {map_data['difficulty']}")
        st.sidebar.write(f"Features: {', '.join(selected_map_features)}")

# Filter Strategies
valid_strategies = []

for strat in strategies_db:
    # Filter by Hero
    if selected_hero != "Any" and selected_hero not in strat["heroes"]:
        continue
    
    # Filter by Map Logic (Basic compatibility check)
    # If Strategy requires Water, but Map has "No Water", exclude it
    if "Water" in strat["tags"] and "No Water" in selected_map_features:
        continue
    
    valid_strategies.append(strat)

# --- DISPLAY RESULTS ---

tab1, tab2 = st.tabs(["Strategy Picker", "Full Database"])

with tab1:
    if not valid_strategies:
        st.warning("No specific strategies match this combination. Try setting Hero to 'Any'.")
    else:
        st.success(f"Found {len(valid_strategies)} Recommended Strategies")
        
        for strat in valid_strategies:
            with st.expander(f"**{strat['name']}** (Tier {strat['tier']}) - Best with {', '.join(strat['heroes'])}", expanded=True):
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.markdown("#### 🛠️ Build Order")
                    st.caption(strat["path"])
                    st.markdown(f"**Best For:** {', '.join(strat['tags'])}")
                
                with col2:
                    st.markdown("#### 📝 Execution Notes")
                    st.write(strat["desc"])
                    st.info(f"**Support Needed:** {strat['support']}")

with tab2:
    st.header("All Version 52 Strategies")
    df = pd.DataFrame(strategies_db)
    # Reorder columns for readability
    cols = ["name", "heroes", "tier", "desc", "path", "support", "tags"]
    st.dataframe(df[cols])

    st.header("Map Reference")
    df_maps = pd.DataFrame(maps_db)
    st.dataframe(df_maps)

st.markdown("---")
st.caption("Updated for Version 52 (Frontier Legends).")

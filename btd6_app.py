import streamlit as st
import pandas as pd

# ==========================================
# 1. DATABASE (The "Brain" of the App)
# ==========================================

# MAPS DATABASE (Expanded to 60 Maps - FINAL LIST)
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

    # INTERMEDIATE MAPS (17)
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

    # ADVANCED MAPS (13)
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

    # EXPERT MAPS (9)
    {"name": "High Finance", "difficulty": "Expert", "features": ["Short", "Gimmick"]},
    {"name": "Another Brick", "difficulty": "Expert", "features": ["Split Path", "Standard"]},
    {"name": "Off The Coast", "difficulty": "Expert", "features": ["Water", "Standard"]},
    {"name": "Cornfield", "difficulty": "Expert", "features": ["Obstacles", "No Water"]},
    {"name": "Underground", "difficulty": "Expert", "features": ["Multi", "Gimmick"]},
    {"name": "Glacial Trail", "difficulty": "Expert", "features": ["Standard"]},
    {"name": "Dark Dungeons", "difficulty": "Expert", "features": ["LOS", "Short"]},
    {"name": "Sanctuary", "difficulty": "Expert", "features": ["Multi", "Moving"]},
    {"name": "Ravine", "difficulty": "Expert", "features": ["Standard", "Gimmick"]},

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
    {"name": "Tricky Tracks", "difficulty": "Expert", "features": ["New", "Short", "No LOS"]},
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
        "path": "Start: Dart/Hero -> Mid: Alch (4-2-0) + Permaspike (0-2-5) -> Late: Overclock (0-4-0) and Homeland Defense (

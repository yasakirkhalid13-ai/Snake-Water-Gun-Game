# Snake Water Gun Game Project
# Build the complete Snake, Water, Gun Game frontend using Streamlit.
import streamlit as st
import random

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Snake Water Gun",
    page_icon="🎮",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #172554);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    color: #38bdf8;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 35px;
}

.choice-card {
    background: #1e293b;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid #334155;
}

.choice-emoji {
    font-size: 65px;
}

div.stButton > button {
    width: 100%;
    height: 65px;
    border-radius: 12px;
    background: #2563eb;
    color: white;
    font-size: 20px;
    font-weight: bold;
    border: none;
}

div.stButton > button:hover {
    background: #0ea5e9;
    color: white;
    border: none;
}

[data-testid="stMetric"] {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
}
</style>
""", unsafe_allow_html=True)

# GAME DATA
choices = {
    "Snake": 1,
    "Water": -1,
    "Gun": 0
}

emoji = {
    1: "🐍 Snake",
    -1: "💧 Water",
    0: "🔫 Gun"
}

# SESSION STATE
if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "draws" not in st.session_state:
    st.session_state.draws = 0

if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = None

# GAME LOGIC
def play_game(player_choice):

    computer_choice = random.choice([1, -1, 0])

    if player_choice == computer_choice:
        result = "Draw"
        st.session_state.draws += 1

    elif (
        (player_choice == 1 and computer_choice == -1)
        or (player_choice == -1 and computer_choice == 0)
        or (player_choice == 0 and computer_choice == 1)
    ):
        result = "You Win!"
        st.session_state.player_score += 1

    else:
        result = "Computer Wins!"
        st.session_state.computer_score += 1

    st.session_state.result = {
        "player": player_choice,
        "computer": computer_choice,
        "outcome": result
    }

    st.session_state.history.insert(0, {
        "Player": emoji[player_choice],
        "Computer": emoji[computer_choice],
        "Result": result
    })

# HEADER
st.markdown(
    '<div class="main-title">🎮 SNAKE • WATER • GUN</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Challenge the Computer | Test Your Luck!</div>',
    unsafe_allow_html=True
)

st.divider()

# SCOREBOARD
st.subheader("🏆 GAME SCOREBOARD")

col1, col2, col3 = st.columns(3)

col1.metric("👤 YOUR SCORE", st.session_state.player_score)
col2.metric("🤖 COMPUTER SCORE", st.session_state.computer_score)
col3.metric("🤝 DRAWS", st.session_state.draws)

st.divider()

# GAME CHOICES
st.subheader("⚔️ SELECT YOUR WEAPON")
st.write("Choose one of the three options below.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="choice-card">
        <div class="choice-emoji">🐍</div>
        <h2>Snake</h2>
        <p>Snake drinks Water</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🐍 Choose Snake", use_container_width=True):
        play_game(1)

with col2:
    st.markdown("""
    <div class="choice-card">
        <div class="choice-emoji">💧</div>
        <h2>Water</h2>
        <p>Water defeats Gun</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💧 Choose Water", use_container_width=True):
        play_game(-1)

with col3:
    st.markdown("""
    <div class="choice-card">
        <div class="choice-emoji">🔫</div>
        <h2>Gun</h2>
        <p>Gun defeats Snake</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔫 Choose Gun", use_container_width=True):
        play_game(0)

# DISPLAY RESULT
if st.session_state.result:

    st.divider()
    st.subheader("🎯 ROUND RESULT")

    result = st.session_state.result

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"👤 You selected: {emoji[result['player']]}")

    with col2:
        st.info(f"🤖 Computer selected: {emoji[result['computer']]}")

    if result["outcome"] == "You Win!":
        st.success("🎉 Congratulations! You won this round!")
        st.balloons()

    elif result["outcome"] == "Computer Wins!":
        st.error("😔 Computer won this round. Try again!")

    else:
        st.warning("🤝 It's a draw! Nobody wins this round.")

# GAME HISTORY
st.divider()
st.subheader("📜 GAME HISTORY")

if st.session_state.history:

    st.dataframe(
        st.session_state.history,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No games played yet. Start your first round!")

# RESET
st.divider()

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🔄 RESET ENTIRE GAME", use_container_width=True):

        st.session_state.player_score = 0
        st.session_state.computer_score = 0
        st.session_state.draws = 0
        st.session_state.history = []
        st.session_state.result = None

        st.rerun()

st.markdown(
    "<center>Developed with ❤️ using Python & Streamlit</center>",
    unsafe_allow_html=True
)

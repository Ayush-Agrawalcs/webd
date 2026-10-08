import streamlit as st
import random
import html
from pathlib import Path

st.set_page_config(
    page_title="For Sneha ❤️",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------- STYLE --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

:root {
    --bg: #090711;
    --card: rgba(255,255,255,.065);
    --line: rgba(255,255,255,.14);
    --text: #f8f3ff;
    --muted: #b9acc8;
    --pink: #ff8fc7;
    --rose: #ff5fa8;
    --purple: #9fb8ff;
    --blue: #6e9cff;
}

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
}
.stApp {
    color: var(--text);
    background:
      radial-gradient(circle at 8% 4%, rgba(255,95,168,.25), transparent 25%),
      radial-gradient(circle at 92% 12%, rgba(88,139,255,.25), transparent 27%),
      radial-gradient(circle at 50% 90%, rgba(221,104,190,.16), transparent 30%),
      linear-gradient(145deg, #080610, #130a1d 50%, #080610);
}
.block-container {
    max-width: 1180px;
    padding-top: 1.3rem;
    padding-bottom: 5rem;
}
.hero {
    text-align:center;
    padding: 30px 15px 25px;
}
.eyebrow {
    text-transform:uppercase;
    letter-spacing:5px;
    color:#d8c9f0;
    font-size:11px;
}
.hero h1, .serif {
    font-family:"Cormorant Garamond", serif;
}
.hero h1 {
    font-size:clamp(58px, 9vw, 105px);
    line-height:.84;
    margin:12px 0;
    background:linear-gradient(90deg,#fff,#f5b5d9,#c7b7ff,#fff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.hero p {
    color:var(--muted);
    font-size:15px;
    line-height:1.8;
}
.glass {
    background:linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.025));
    border:1px solid var(--line);
    border-radius:28px;
    padding:28px;
    box-shadow:0 25px 80px rgba(0,0,0,.25);
    backdrop-filter:blur(18px);
}
.question {
    text-align:center;
    padding:30px 20px;
    border-radius:25px;
    background:linear-gradient(145deg,rgba(139,88,205,.17),rgba(255,255,255,.035));
    border:1px solid rgba(216,190,255,.19);
    margin:12px 0 18px;
}
.question .number {
    font-size:11px;
    letter-spacing:3px;
    text-transform:uppercase;
    color:#cbb9e9;
}
.question h2 {
    font-family:"Cormorant Garamond",serif;
    font-size:clamp(28px,4vw,45px);
    margin:10px auto 0;
    max-width:850px;
}
.prize {
    border:1px solid rgba(255,255,255,.12);
    border-radius:22px;
    padding:18px;
    background:rgba(255,255,255,.035);
}
.prize h3 {font-family:"Cormorant Garamond",serif;font-size:26px;margin-top:0}
.prize-row {padding:5px 8px;color:#81768e;font-size:13px}
.prize-active {
    padding:7px 10px;
    border-radius:10px;
    background:rgba(202,151,255,.14);
    color:#f4e7ff;
    font-weight:700;
}
.section-title {
    text-align:center;
    margin:50px 0 22px;
}
.section-title h2 {
    font-family:"Cormorant Garamond",serif;
    font-size:48px;
    margin:0;
}
.section-title p {color:var(--muted)}
.shayari {
    font-family:"Cormorant Garamond",serif;
    font-size:27px;
    line-height:1.65;
    text-align:center;
    color:#f5e9ff;
    padding:35px 20px;
}
.shayari span {color:#f3a9d0}
.love-card {
    position:relative;
    overflow:hidden;
    text-align:center;
    border-radius:32px;
    padding:55px 28px;
    background:
      radial-gradient(circle at 50% 0%,rgba(246,165,208,.25),transparent 40%),
      linear-gradient(145deg,#24132d,#120d1e);
    border:1px solid rgba(255,215,239,.22);
    box-shadow:0 30px 100px rgba(0,0,0,.35);
}
.love-card:before,.love-card:after {
    content:"✦";
    position:absolute;
    color:rgba(255,255,255,.28);
    font-size:25px;
}
.love-card:before {left:9%;top:13%}
.love-card:after {right:11%;bottom:15%}
.love-card h1 {
    font-family:"Cormorant Garamond",serif;
    font-size:clamp(44px,7vw,76px);
    margin:8px 0;
}
.love-card p {
    max-width:720px;
    margin:15px auto;
    color:#dfd2e8;
    line-height:1.9;
    font-size:16px;
}
.caption {
    text-align:center;
    color:#a89aaf;
    font-size:11px;
    margin-top:9px;
}
.photo {
    border-radius:22px;
    overflow:hidden;
    border:1px solid rgba(255,255,255,.14);
    background:rgba(255,255,255,.04);
    min-height:150px;
}
.stButton > button {
    min-height:48px !important;
    border-radius:14px !important;
    background:rgba(255,255,255,.065) !important;
    color:white !important;
    border:1px solid rgba(255,255,255,.14) !important;
    font-weight:600 !important;
}
.stButton > button:hover {
    border-color:#e5b8ef !important;
    background:rgba(190,120,205,.17) !important;
}
div[data-testid="stFileUploader"] {
    border-radius:16px;
}

.proposal {
    position:relative;
    min-height:500px;
    display:flex;
    align-items:center;
    justify-content:center;
    overflow:hidden;
    border-radius:34px;
    padding:55px 25px;
    background:
      radial-gradient(circle at 50% 42%, rgba(255,110,177,.32), transparent 30%),
      radial-gradient(circle at 15% 20%, rgba(91,145,255,.28), transparent 28%),
      linear-gradient(145deg,#111c3d,#24102d 55%,#100817);
    border:1px solid rgba(255,185,220,.28);
    box-shadow:0 35px 120px rgba(31,17,65,.7);
    perspective:1000px;
}
.proposal-inner {
    text-align:center;
    transform:rotateX(2deg) rotateY(-2deg);
    max-width:780px;
    position:relative;
    z-index:2;
}
.proposal .ring {
    font-size:82px;
    filter:drop-shadow(0 0 28px rgba(255,148,205,.65));
    animation:ringFloat 2.5s ease-in-out infinite;
}
.proposal h1 {
    font-family:"Cormorant Garamond",serif;
    font-size:clamp(50px,8vw,88px);
    line-height:.9;
    margin:15px 0;
    background:linear-gradient(90deg,#fff,#ffc3e1,#9fc0ff,#fff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.proposal .question-text {
    font-family:"Cormorant Garamond",serif;
    font-size:30px;
    color:#ffe9f5;
    margin:20px 0;
}
.proposal .proposal-copy {
    color:#e4d9eb;
    line-height:1.9;
    font-size:16px;
}
.glow-heart {
    position:absolute;
    color:rgba(255,125,188,.5);
    animation:heartFloat 6s ease-in-out infinite;
}
.h1 {left:7%;top:12%;font-size:35px}
.h2 {right:8%;top:18%;font-size:22px;animation-delay:1s}
.h3 {left:15%;bottom:14%;font-size:23px;animation-delay:2s}
.h4 {right:15%;bottom:11%;font-size:38px;animation-delay:3s}
@keyframes ringFloat {
    0%,100% {transform:translateY(0) rotate(-4deg)}
    50% {transform:translateY(-12px) rotate(4deg)}
}
@keyframes heartFloat {
    0%,100% {transform:translateY(0) rotate(0);opacity:.35}
    50% {transform:translateY(-25px) rotate(10deg);opacity:.85}
}
.collage {
    position:relative;
    padding:22px;
    border-radius:34px;
    background:
      linear-gradient(135deg,#f8c6df,#b9cfff 48%,#f6a8ce);
    box-shadow:0 25px 80px rgba(255,93,171,.18);
    overflow:hidden;
}
.collage-inner {
    background:#171020;
    padding:12px;
    border-radius:24px;
    display:grid;
    grid-template-columns:1.2fr .8fr;
    grid-template-rows:1fr 1fr;
    gap:10px;
    min-height:480px;
}
.collage-photo {
    overflow:hidden;
    border-radius:18px;
    border:2px solid rgba(255,255,255,.55);
    background:linear-gradient(145deg,#251735,#101322);
    display:flex;
    align-items:center;
    justify-content:center;
}
.collage-photo:first-child {grid-row:1/3}
.collage-photo img {width:100%;height:100%;object-fit:cover;display:block}
.collage-title {
    text-align:center;
    font-family:"Cormorant Garamond",serif;
    font-size:34px;
    color:#fff;
    margin-top:16px;
}
.collage-subtitle {
    text-align:center;
    color:#ffe1f0;
    font-size:12px;
    letter-spacing:2px;
    text-transform:uppercase;
}

.small {
    text-align:center;
    color:#786d80;
    font-size:11px;
    margin-top:32px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- QUESTIONS --------------------
HISTORY = [
("Who was the first President of independent India?", ["Dr. Rajendra Prasad","Jawaharlal Nehru","Sardar Patel","Dr. B. R. Ambedkar"], 0),
("The Battle of Plassey was fought in which year?", ["1757","1764","1857","1776"], 0),
("Who founded the Maurya Empire?", ["Ashoka","Chandragupta Maurya","Bindusara","Harshavardhana"], 1),
("The Quit India Movement was launched in which year?", ["1930","1942","1947","1919"], 1),
("Who gave the slogan “Swaraj is my birthright and I shall have it”?", ["Bal Gangadhar Tilak","Mahatma Gandhi","Subhas Chandra Bose","Lala Lajpat Rai"], 0),
("The Dandi March was associated with which movement?", ["Non-Cooperation Movement","Civil Disobedience Movement","Quit India Movement","Swadeshi Movement"], 1),
("Who was the last Mughal emperor?", ["Akbar II","Bahadur Shah Zafar","Shah Alam II","Aurangzeb"], 1),
("The French Revolution began in which year?", ["1776","1789","1815","1848"], 1),
("Who was known as the ‘Iron Man of India’?", ["Sardar Vallabhbhai Patel","Bhagat Singh","Rajendra Prasad","B. R. Ambedkar"], 0),
("The Jallianwala Bagh massacre took place in which city?", ["Delhi","Amritsar","Lahore","Lucknow"], 1),
("Who wrote the Indian national anthem ‘Jana Gana Mana’?", ["Bankim Chandra Chattopadhyay","Rabindranath Tagore","Sarojini Naidu","Sri Aurobindo"], 1),
("The ancient city of Pompeii was buried after the eruption of which volcano?", ["Mount Etna","Mount Vesuvius","Krakatoa","Mount Fuji"], 1),
("Who was the first woman to become Prime Minister of India?", ["Sarojini Naidu","Indira Gandhi","Vijaya Lakshmi Pandit","Sushma Swaraj"], 1),
("The Berlin Wall fell in which year?", ["1961","1975","1989","1991"], 2),
("Who was the first person to step on the Moon?", ["Yuri Gagarin","Buzz Aldrin","Neil Armstrong","Michael Collins"], 2),
("The Renaissance began primarily in which country?", ["France","Italy","Spain","Germany"], 1),
]

MATH = [
("What is 15% of 200?", ["20","25","30","35"], 2),
("If 3x + 7 = 22, what is x?", ["3","5","7","9"], 1),
("What is the average of 10, 20 and 30?", ["15","20","25","30"], 1),
("A ₹500 item gets a 20% discount. What is the sale price?", ["₹380","₹400","₹420","₹450"], 1),
]

QUESTIONS = []
for q, opts, ans in HISTORY:
    QUESTIONS.append({"q":q,"options":opts,"answer":ans,"type":"Historical GK"})
for q, opts, ans in MATH:
    QUESTIONS.append({"q":q,"options":opts,"answer":ans,"type":"Basic Mathematics"})

PRIZES = [
"₹1,000","₹2,000","₹5,000","₹10,000","₹20,000",
"₹40,000","₹80,000","₹1,60,000","₹3,20,000","₹6,40,000",
"₹12,50,000","₹25,00,000","₹50,00,000","₹75,00,000","₹1 Crore",
"₹2 Crore","₹3 Crore","₹5 Crore","₹7 Crore","₹10 Crore"
]

SHAYARI = [
"""Sneha, lafzon mein kaise bataun tum mere liye kya ho,
Tum saamne na ho phir bhi mere har khayal mein tum ho.
Faasle chahe jitne bhi ho, dil ko yeh manzoor nahi,
Meri har khushi ke peeche, kahin na kahin tum hi tum ho. ❤️""",
"""Kabhi kabhi ek insaan poori duniya sa lagta hai,
Uski ek smile se har gham chhota sa lagta hai.
Sneha, tum meri kahani ka woh khoobsurat hissa ho,
Jise padhte-padhte dil ko har baar sukoon sa milta hai. 💜""",
"""Na koi perfect story chahiye, na koi perfect pal,
Bas tumhara saath ho, toh khoobsurat hai har kal.
Aaj yeh chhoti si website sirf ek bahaana hai,
Tumhe batane ka ki Sneha, tum mere liye bahut khaas ho. ✨""",
]

COUPLE_PROMPTS = [
"Who would fall asleep first during a late-night call?",
"Who is more likely to say “I'm fine” when they are actually annoyed?",
"Who would plan a surprise date?",
"Who would start laughing at the worst possible moment?",
"Who is more likely to say “bas 5 minutes” and take 30 minutes?",
"Who would choose food over almost any plan?",
"Who remembers tiny details better?",
"Who would survive longer without checking their phone?",
"Who would win a silly argument just because they refuse to give up?",
"Who would suggest a spontaneous trip?",
"Who would send the first message after a tiny fight?",
"Who is secretly more romantic?",
]

# -------------------- STATE --------------------
defaults = {
    "page":"home",
    "q":0,
    "score":0,
    "answered":False,
    "lifeline_5050":False,
    "lifeline_audience":False,
    "lifeline_skip":False,
    "couple_index":0,
    "couple_answers":[],
    "uploaded_photos":[],
    "photo_data":[],
    "wrong_message":False,
    "game_over":False,
    "proposal_accepted":False,
}
for k,v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

def reset_quiz():
    st.session_state.q=0
    st.session_state.score=0
    st.session_state.answered=False
    st.session_state.lifeline_5050=False
    st.session_state.lifeline_audience=False
    st.session_state.lifeline_skip=False
    st.session_state.wrong_message=False
    st.session_state.game_over=False
    st.session_state.page="quiz"

def escape(s):
    return html.escape(str(s))

# -------------------- HEADER --------------------
st.markdown("""
<div class="hero">
  <div class="eyebrow">A little universe made for one person</div>
  <h1>Sneha ❤️</h1>
  <p>
    This isn't just a quiz.<br>
    It's a tiny collection of questions, memories, smiles and feelings — made especially for you.
  </p>
</div>
""", unsafe_allow_html=True)

# -------------------- HOME --------------------
if st.session_state.page == "home":
    st.markdown("""
    <style>
    .rose-garden{position:relative;height:88px;margin:-10px auto 5px;max-width:900px;pointer-events:none;overflow:hidden}
    .floating-rose{position:absolute;font-size:34px;filter:drop-shadow(0 5px 10px rgba(255,60,120,.35));animation:roseDrift 4s ease-in-out infinite}
    .floating-rose.r1{left:4%;top:28px;animation-delay:0s}
    .floating-rose.r2{left:17%;top:5px;font-size:28px;animation-delay:1s}
    .floating-rose.r3{left:31%;top:34px;font-size:25px;animation-delay:.5s}
    .floating-rose.r4{right:31%;top:12px;font-size:28px;animation-delay:1.4s}
    .floating-rose.r5{right:17%;top:35px;animation-delay:.8s}
    .floating-rose.r6{right:4%;top:8px;font-size:32px;animation-delay:1.8s}
    @keyframes roseDrift{0%,100%{transform:translateY(0) rotate(-5deg);opacity:.78}50%{transform:translateY(-10px) rotate(7deg);opacity:1}}
    .home-love-line{text-align:center;font-family:"Cormorant Garamond",serif;font-size:25px;color:rgba(255,220,238,.9);margin:-4px 0 18px}
    </style>
    <div class="rose-garden">
      <span class="floating-rose r1">🌹</span><span class="floating-rose r2">🌹</span>
      <span class="floating-rose r3">🌹</span><span class="floating-rose r4">🌹</span>
      <span class="floating-rose r5">🌹</span><span class="floating-rose r6">🌹</span>
    </div>
    <div class="home-love-line">A little world of love, made just for Sneha ❤️</div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    with a:
        st.markdown('<div style="text-align:center;font-size:42px">🎯</div><h3 style="text-align:center">20 Questions</h3><p style="text-align:center;color:#aaa">16 historical GK + 4 easy maths questions.</p>', unsafe_allow_html=True)
    with b:
        st.markdown('<div style="text-align:center;font-size:42px">💞</div><h3 style="text-align:center">Couple Game</h3><p style="text-align:center;color:#aaa">Play a fun “Who would…” game together virtually.</p>', unsafe_allow_html=True)
    with c:
        st.markdown('<div style="text-align:center;font-size:42px">💌</div><h3 style="text-align:center">A Final Surprise</h3><p style="text-align:center;color:#aaa">Shayari, your photos and a final love card.</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    x,y,z = st.columns([1,1.4,1])
    with y:
        if st.button("💜 Start Sneha's KBC", use_container_width=True):
            reset_quiz()
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="love-card" style="margin-top:25px"><h1>For the girl who makes ordinary moments feel special.</h1><p>Take your time. There is no pressure to win. The real prize is waiting at the end.</p></div>', unsafe_allow_html=True)

# -------------------- QUIZ --------------------
elif st.session_state.page == "quiz":
    i=st.session_state.q
    item=QUESTIONS[i]

    left,right=st.columns([3.1,1])
    with left:
        st.markdown(f"""
        <div class="question">
          <div class="number">Question {i+1} of 20 · {item["type"]}</div>
          <h2>{escape(item["q"])}</h2>
        </div>
        """, unsafe_allow_html=True)

        c1,c2,c3=st.columns(3)
        with c1:
            if st.button("🌓 50 : 50", disabled=st.session_state.lifeline_5050, use_container_width=True):
                st.session_state.lifeline_5050=True
                st.rerun()
        with c2:
            if st.button("👥 Audience", disabled=st.session_state.lifeline_audience, use_container_width=True):
                st.session_state.lifeline_audience=True
                st.rerun()
        with c3:
            if st.button("🔄 Skip", disabled=st.session_state.lifeline_skip, use_container_width=True):
                st.session_state.lifeline_skip=True
                if i < 19:
                    st.session_state.q += 1
                    st.session_state.answered=False
                st.rerun()

        opts=list(enumerate(item["options"]))
        if st.session_state.lifeline_5050:
            wrong=[n for n in range(4) if n != item["answer"]]
            remove=random.sample(wrong,2)
            opts=[x for x in opts if x[0] not in remove]

        if st.session_state.lifeline_audience:
            percentages=[8,8,8,8]
            percentages[item["answer"]]=76
            remain=[n for n in range(4) if n != item["answer"]]
            for n in remain:
                percentages[n]=8
            st.info("👥 Audience Poll — " + " · ".join(f"{chr(65+n)} {percentages[n]}%" for n in range(4)))

        for n,text in opts:
            if st.button(f"{chr(65+n)}. {text}", key=f"ans_{i}_{n}", use_container_width=True, disabled=st.session_state.answered):
                if n == item["answer"]:
                    st.session_state.score += 1
                    st.session_state.answered=True
                    st.success("✨ Correct! Beautifully done.")
                else:
                    # Wrong answer = game ends immediately.
                    st.session_state.answered=True
                    st.session_state.game_over=True
                    st.session_state.page="game_over"
                    st.rerun()

        if st.session_state.answered and not st.session_state.game_over:
            st.markdown("<br>", unsafe_allow_html=True)
            if i < 19:
                if st.button("➡️ Next Question", key=f"next_question_{i}", use_container_width=True):
                    st.session_state.q += 1
                    st.session_state.answered=False
                    st.rerun()
            else:
                if st.button("💜 Finish Quiz", key="finish_quiz", use_container_width=True):
                    st.session_state.answered=False
                    st.session_state.page="shayari"
                    st.rerun()

    with right:
        st.markdown('<div class="prize"><h3>🏆 Prize Ladder</h3>', unsafe_allow_html=True)
        for n in range(19,-1,-1):
            if n == i:
                st.markdown(f'<div class="prize-active">{PRIZES[n]}</div>', unsafe_allow_html=True)
            elif n < i:
                st.markdown(f'<div class="prize-row">✓ {PRIZES[n]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="prize-row">{PRIZES[n]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="small">Score so far: {st.session_state.score}/{i} · Made especially for Sneha</div>', unsafe_allow_html=True)

# -------------------- SHAYARI --------------------
elif st.session_state.page == "game_over":
    st.markdown("""
    <div class="love-card" style="margin-top:20px">
      <div style="font-size:68px">🥺💗</div>
      <div class="eyebrow">KBC · Sneha's Game</div>
      <h1>Sorry cutie,<br>it's wrong.</h1>
      <p>
        Try next time ❤️
        <br><br>
        Game over for this round…
        but don't worry, something special is still waiting for you.
      </p>
      <div style="font-family:'Cormorant Garamond';font-size:25px;color:#f7b7d9;margin-top:22px">
        Don't be sad, cutie. The next surprise is waiting. 💕
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("💜 Next Surprise", use_container_width=True):
        # Do NOT restart the quiz. Move directly to the next experience.
        st.session_state.page="shayari"
        st.rerun()

elif st.session_state.page == "shayari":
    st.markdown(f"""
    <div class="love-card">
      <div style="font-size:55px">🌙</div>
      <h1>20 questions later…</h1>
      <p>You got <strong>{st.session_state.score}/20</strong> correct.</p>
      <p>But honestly, the score was never the important part.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title"><h2>Ab thoda dil ki baat…</h2><p>Some words that were waiting for you.</p></div>', unsafe_allow_html=True)

    for s in SHAYARI:
        st.markdown(f'<div class="glass shayari">{s.replace(chr(10),"<br>")}</div><br>', unsafe_allow_html=True)

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    if st.button("💞 Play Our Couple Game", use_container_width=True):
        st.session_state.page="couple"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- COUPLE GAME --------------------
elif st.session_state.page == "couple":
    j=st.session_state.couple_index
    prompt=COUPLE_PROMPTS[j]

    st.markdown('<div class="section-title"><h2>Us, But Make It A Game 💞</h2><p>Take turns choosing who fits the statement better.</p></div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="question">
      <div class="number">Round {j+1} of {len(COUPLE_PROMPTS)}</div>
      <h2>“{escape(prompt)}”</h2>
    </div>
    """, unsafe_allow_html=True)

    a,b=st.columns(2)
    with a:
        if st.button("❤️ Ayush", use_container_width=True):
            st.session_state.couple_answers.append(("Ayush",prompt))
            if j < len(COUPLE_PROMPTS)-1:
                st.session_state.couple_index += 1
            else:
                st.session_state.page="photos"
            st.rerun()
    with b:
        if st.button("💜 Sneha", use_container_width=True):
            st.session_state.couple_answers.append(("Sneha",prompt))
            if j < len(COUPLE_PROMPTS)-1:
                st.session_state.couple_index += 1
            else:
                st.session_state.page="photos"
            st.rerun()

    st.markdown('<br><div class="glass"><p style="text-align:center;color:#b9acc8">Tip: Say your answers out loud at the same time, then laugh about it. 😄</p></div>', unsafe_allow_html=True)

# -------------------- PHOTOS --------------------
elif st.session_state.page == "photos":
    st.markdown('<div class="section-title"><h2>Our Little Gallery 📸</h2><p>Upload up to four favourite photos — they will become one romantic frame at the end.</p></div>', unsafe_allow_html=True)

    cols=st.columns(4)
    current_photo_data=[]
    for idx in range(4):
        with cols[idx]:
            f=st.file_uploader(
                f"Photo {idx+1}",
                type=["jpg","jpeg","png","webp"],
                key=f"photo_{idx}"
            )
            if f:
                raw=f.getvalue()
                current_photo_data.append({
                    "bytes": raw,
                    "mime": getattr(f, "type", None) or "image/jpeg"
                })
                st.image(f, use_container_width=True)
            else:
                st.markdown(
                    '<div class="photo" style="display:flex;align-items:center;justify-content:center">'
                    '<span style="font-size:38px">♡</span></div>',
                    unsafe_allow_html=True
                )
                st.markdown('<div class="caption">Your photo here</div>', unsafe_allow_html=True)

    # Copy the actual bytes into a non-widget session-state key so the photos
    # survive when Streamlit changes from the upload page to the final page.
    if current_photo_data:
        st.session_state.photo_data=current_photo_data

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✨ Create Our Final Card", use_container_width=True):
        st.session_state.page="final"
        st.rerun()

# -------------------- FINAL CARD --------------------
elif st.session_state.page == "final":
    st.markdown('<div class="section-title"><h2>The Moment I Wanted You To Reach</h2><p>Forget the score. This is the real question.</p></div>', unsafe_allow_html=True)

    if st.session_state.get("proposal_accepted", False):
        st.markdown("""
        <style>
        .yes-card {
            max-width:760px;
            margin:30px auto;
            padding:55px 30px;
            text-align:center;
            border-radius:32px;
            background:linear-gradient(145deg,rgba(255,255,255,.12),rgba(255,75,125,.12));
            border:1px solid rgba(255,255,255,.20);
            box-shadow:0 25px 70px rgba(255,45,95,.25);
        }
        .rose {font-size:105px;animation:roseFloat 2.2s ease-in-out infinite}
        .love-title {font-family:"Cormorant Garamond",serif;font-size:58px;font-weight:700}
        .love-line {font-family:"Cormorant Garamond",serif;font-size:34px;margin-top:10px}
        @keyframes roseFloat {0%,100%{transform:translateY(0) rotate(-3deg)}50%{transform:translateY(-12px) rotate(3deg)}}
        </style>
        <div class="yes-card">
          <div class="rose">🌹</div>
          <div class="eyebrow">She said YES ❤️</div>
          <div class="love-title">I Love You, Sneha.</div>
          <div class="love-line">I love you a lot. More than I can put into words. ❤️</div>
          <div style="margin-top:25px;font-size:20px">This little moment is yours forever. 💕</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align:center;margin:25px auto 8px;font-family:'Cormorant Garamond',serif;font-size:25px">
          🎶 <strong>Our song — Tu Chahiye</strong> 🌹
        </div>
        """, unsafe_allow_html=True)
        st.components.v1.html("""
        <div style="display:flex;justify-content:center">
          <iframe
            width="100%" height="90"
            style="max-width:700px;border:0;border-radius:18px;box-shadow:0 12px 35px rgba(0,0,0,.3)"
            src="https://www.youtube.com/embed/zuvla6ABKbs?autoplay=1&playsinline=1&rel=0"
            title="Tu Chahiye - T-Series"
            allow="autoplay; encrypted-media; picture-in-picture"
            allowfullscreen>
          </iframe>
        </div>
        """, height=105)
    else:
        st.markdown("""
        <style>
        .proposal-actions{display:flex;justify-content:center;align-items:center;gap:18px;margin:25px auto 35px;min-height:70px}
        .runaway-no{
            display:flex;align-items:center;justify-content:center;
            width:150px;height:48px;border-radius:999px;
            border:1px solid rgba(255,255,255,.28);
            background:rgba(255,255,255,.10);color:white;
            font-weight:700;cursor:pointer;user-select:none;
            transition:transform .15s ease;
        }
        .runaway-no:hover{animation:runAway .42s linear infinite}
        @keyframes runAway{
            0%{transform:translate(0,0) rotate(0deg)}
            20%{transform:translate(90px,-45px) rotate(-8deg)}
            40%{transform:translate(-75px,55px) rotate(8deg)}
            60%{transform:translate(110px,45px) rotate(-5deg)}
            80%{transform:translate(-105px,-35px) rotate(7deg)}
            100%{transform:translate(0,0) rotate(0deg)}
        }
        .yes-note{text-align:center;color:rgba(255,255,255,.72);font-size:14px;margin-top:-8px}
        </style>
        <div class="proposal">
          <span class="glow-heart h1">♥</span>
          <span class="glow-heart h2">♥</span>
          <span class="glow-heart h3">♥</span>
          <span class="glow-heart h4">♥</span>
          <div class="proposal-inner">
            <div class="ring">💍</div>
            <div class="eyebrow">Sneha, one last question…</div>
            <h1>Will you marry me?</h1>
            <div class="question-text">Not just for today. For all the little tomorrows too. ❤️</div>
            <div class="proposal-copy">
              Shayad main har baar perfect words na bol paun,
              lekin jo feel karta hoon woh bilkul simple hai —
              <strong>tum mere liye bahut special ho.</strong>
              <br><br>
              Main perfect relationship ka promise nahi karta.
              Main bas yeh promise karta hoon ki hum dono milkar
              apni story ko aur beautiful banayenge.
              <br><br>
              <strong>So Sneha… will you be mine, today and always? 💗</strong>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="proposal-actions"><div class="runaway-no">No 😜</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="yes-note">The “No” button is a little shy. 😄</div>', unsafe_allow_html=True)

        if st.button("💍 YES, I WILL ❤️", key="proposal_yes", use_container_width=True):
            st.session_state.proposal_accepted = True
            st.rerun()

    st.markdown('<div class="section-title"><h2>Our Little Frame 📸</h2><p>Your pictures are arranged into one romantic collage.</p></div>', unsafe_allow_html=True)

    # Use copied photo bytes instead of Streamlit uploader objects.
    # Uploader widgets can be removed from session state when this page changes.
    photo_data = st.session_state.get("photo_data", [])

    st.markdown("""
    <style>
    .heart-gallery {
        width: min(760px, 94vw);
        aspect-ratio: 1 / 1;
        margin: 28px auto 10px;
        position: relative;
        filter: drop-shadow(0 22px 40px rgba(255, 80, 165, .30));
    }
    .heart-gallery::before {
        content: "";
        position: absolute;
        inset: -16px;
        background: linear-gradient(135deg, #fff, #ff8fc7 35%, #9fb8ff 72%, #fff);
        clip-path: polygon(
            50% 97%, 8% 56%, 3% 36%, 7% 19%, 18% 8%, 32% 9%,
            50% 25%, 68% 9%, 82% 8%, 93% 19%, 97% 36%, 92% 56%
        );
    }
    .heart-gallery-inner {
        position: absolute;
        inset: 0;
        overflow: hidden;
        background: #171126;
        clip-path: polygon(
            50% 97%, 8% 56%, 3% 36%, 7% 19%, 18% 8%, 32% 9%,
            50% 25%, 68% 9%, 82% 8%, 93% 19%, 97% 36%, 92% 56%
        );
        padding: 9%;
        box-sizing: border-box;
    }
    .heart-grid {
        width: 100%;
        height: 100%;
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 1fr 1fr;
        gap: 10px;
    }
    .heart-photo {
        min-width: 0;
        min-height: 0;
        overflow: hidden;
        border: 5px solid rgba(255,255,255,.95);
        box-shadow: 0 8px 24px rgba(0,0,0,.34);
        background: rgba(255,255,255,.08);
    }
    .heart-photo:nth-child(1) { border-radius: 58% 14px 14px 14px; }
    .heart-photo:nth-child(2) { border-radius: 14px 58% 14px 14px; }
    .heart-photo:nth-child(3) { border-radius: 14px 14px 14px 58%; }
    .heart-photo:nth-child(4) { border-radius: 14px 14px 58% 14px; }
    .heart-photo img {
        width: 100%;
        height: 100%;
        display: block;
        object-fit: cover;
        object-position: center;
    }
    .heart-label {
        text-align: center;
        margin: 0 auto 26px;
        font-family: "Cormorant Garamond", serif;
        font-size: 23px;
        color: rgba(255,255,255,.88);
    }
    @media (max-width: 600px) {
        .heart-gallery-inner { padding: 10%; }
        .heart-grid { gap: 6px; }
        .heart-photo { border-width: 3px; }
    }
    </style>
    """, unsafe_allow_html=True)

    import base64
    photo_html = []
    for item in photo_data[:4]:
        encoded = base64.b64encode(item["bytes"]).decode("utf-8")
        mime = item.get("mime", "image/jpeg")
        photo_html.append(
            f'<div class="heart-photo"><img src="data:{mime};base64,{encoded}" alt="Memory"></div>'
        )

    while len(photo_html) < 4:
        photo_html.append(
            '<div class="heart-photo"><div style="height:100%;display:flex;'
            'align-items:center;justify-content:center;color:#fff;font-size:34px">♡</div></div>'
        )

    st.markdown(
        '<div class="heart-gallery"><div class="heart-gallery-inner">'
        '<div class="heart-grid">' + ''.join(photo_html) +
        '</div></div></div>'
        '<div class="heart-label">four little memories · one big heart ❤️</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="glass shayari" style="margin-top:25px">
      “Tum mile toh laga, kuch kahaniyan likhi nahi jaati…
      <br>bas dheere-dheere dil mein ban jaati hain.” 💗
    </div>
    """, unsafe_allow_html=True)

    a,b=st.columns(2)
    with a:
        if st.button("📸 Change Photos", use_container_width=True):
            st.session_state.page="photos"
            st.rerun()
    with b:
        if st.button("↩ Start Again", use_container_width=True):
            st.session_state.page="home"
            st.session_state.q=0
            st.session_state.score=0
            st.session_state.couple_index=0
            st.session_state.wrong_message=False
            st.session_state.game_over=False
            st.rerun()

st.markdown('<div class="small">Made with Python · For Sneha, with love ❤️</div>', unsafe_allow_html=True)

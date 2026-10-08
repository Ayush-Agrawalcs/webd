# For Saneha ❤️ — Python Romantic Website

A polished Streamlit website containing:

1. KBC-style quiz
   - Exactly 20 questions
   - 16 historical/general-knowledge questions
   - 4 basic mathematics questions
   - Prize ladder
   - 50:50 lifeline
   - Audience Poll
   - Skip lifeline

2. Hinglish shayari reveal after the quiz

3. Virtual couple game
   - "Who would..." prompts
   - Ayush/Saneha choices
   - 12 rounds

4. Photo gallery
   - Four replaceable upload slots
   - JPG/JPEG/PNG/WEBP

5. Final romantic card
   - Personalized message
   - Photo frame layout
   - Easy-to-edit text

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Customize

All questions, shayari, couple prompts and final-card text are near the top/middle of `app.py`.
You can replace them with your own memories and inside jokes.

## Important

The website does not permanently store uploaded photos. They are held by the Streamlit session.
If you want permanent hosting/photo storage, add a database or cloud storage later.


## Latest romantic updates

- Wrong answer now shows: **“Sorry cutie, it's wrong. Try next time ❤️”**
- Added blue + pink romantic glow palette.
- Added a 3D-style proposal finale with a ring and floating hearts.
- Added a final photo-frame/collage presentation.

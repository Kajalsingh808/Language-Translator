# app.py

import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os
from io import BytesIO

# --- App Title ---
st.set_page_config(page_title="Language Translation Tool", page_icon="🌐", layout="centered")
st.title("🌐 Language Translation Tool")
st.write("Translate text easily between multiple languages.")

# --- Initialize Translator ---
translator = Translator()

# --- Input Section ---
text = st.text_area("Enter text to translate:", height=150)
src_lang = st.selectbox("Source Language", ["auto", "en", "hi", "fr", "es", "de", "ta", "bn", "zh-cn"])
dest_lang = st.selectbox("Target Language", ["en", "hi", "fr", "es", "de", "ta", "bn", "zh-cn"])

# --- Translation Logic ---
def translate_text(text, src, dest):
    try:
        result = translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        return f"⚠️ Translation error: {e}"

# --- Translate Button ---
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        translated_text = translate_text(text, src_lang, dest_lang)
        st.subheader("Translated Text:")
        st.success(translated_text)

        # --- Optional: Text-to-Speech ---
        tts_audio = BytesIO()
        tts = gTTS(translated_text, lang=dest_lang)
        tts.save("temp.mp3")

        st.audio("temp.mp3")

        # --- Optional: Copy Button ---
        st.download_button("📋 Copy Translated Text", data=translated_text, file_name="translation.txt")

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ using Streamlit and Googletrans")

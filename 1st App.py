from googletrans import Translator
import streamlit as st
from gtts import gTTS
translator = Translator()

def translate_text(text, src_lang, dest_lang):
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text
st.title("🌐 Language Translation Tool")

text = st.text_area("Enter text to translate:")
src_lang = st.selectbox("Source language", ["en", "hi", "fr", "es", "de"])
dest_lang = st.selectbox("Target language", ["hi", "en", "fr", "es", "de"])

if st.button("Translate"):
    translated_text = translate_text(text, src_lang, dest_lang)
    st.success(translated_text)

    if st.button("🔊 Text to Speech"):
        tts = gTTS(translated_text, lang=dest_lang)
        tts.save("translated.mp3")
        st.audio("translated.mp3")

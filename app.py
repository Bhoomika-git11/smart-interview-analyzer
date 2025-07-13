import streamlit as st
import os

from speech_to_text import transcribe_audio
from sentiment_analysis import analyze_sentiment_and_emotion
from utils.keyword_extractor import extract_keywords
from feedback_generator import generate_feedback

st.set_page_config(page_title="Smart Interview Analyzer")
st.title("🎤 Smart Interview Analyzer")

uploaded_file = st.file_uploader("Upload your interview audio (.wav only)", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    os.makedirs("audio_samples", exist_ok=True)
    file_path = os.path.join("audio_samples", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("Transcribing audio...")
    transcript = transcribe_audio(file_path)

    st.subheader("📝 Transcript")
    st.write(transcript)

    sentiment, compound, emotion, filler_count = analyze_sentiment_and_emotion(transcript)
    keywords = extract_keywords(transcript)
    feedback = generate_feedback(transcript, emotion, filler_count, compound)

    st.subheader("🎯 Analysis Result")
    st.write("*Sentiment:*", sentiment)
    st.write("*Compound Score:*", round(compound, 3))
    st.write("*Emotion Detected:*", emotion)
    st.write("*Filler Words Count:*", filler_count)

    st.subheader("🗝 Detected Keywords")
    st.write(", ".join(keywords) if keywords else "No keywords detected.")

    st.subheader("💡 Feedback & Suggestions")
    if feedback:
        for tip in feedback:
            st.write("- " + tip)
    else:
        st.write("✅ Your response looks great!")
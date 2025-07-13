# 🎙 Smart Interview Analyzer

An AI-powered tool that analyzes spoken interview responses and provides personalized feedback on tone, fluency, and content relevance — helping users improve their communication skills before real interviews.



##  Project Objective

The Smart Interview Analyzer simulates a virtual HR evaluator by listening to recorded voice responses, converting them to text, and analyzing various elements such as:

- Emotional tone and confidence (sentiment analysis)
- Filler words that affect fluency
- Relevance and strength of spoken keywords
- Overall communication clarity



##  Features

✅ Converts .wav audio input into clean text  
✅ Detects emotional tone using VADER Sentiment Analysis  
✅ Highlights common filler words (like “um”, “actually”, “you know”)  
✅ Extracts key phrases and topics using SpaCy NLP  
✅ Generates actionable suggestions to improve interview performance  
✅ Simple, clean web interface using Streamlit

---

##  Technologies Used

- Python 3.8+
- Streamlit - https://streamlit.io/
- SpeechRecognition- https://pypi.org/project/SpeechRecognition/
- NLTK- https://www.nltk.org/
- VADER Sentiment- https://github.com/cjhutto/vaderSentiment
- Matplotlib & WordCloud (optional for visualizations)



##  Sample Input

Place your .wav audio samples inside the audio_samples/ folder.  
Make sure the files:
- Are between 10–60 seconds long
- Use clear English speech
- Have minimal background noise

If your audio is not .wav, convert it using: [https://cloudconvert.com/]



## How to Run Locally


```bash
git clone https://github.com/Bhoomika-git11/smart-interview-analyzer.git
cd smart-interview-analyzer
pip install -r requirements.txt
*If this file is missing, install required packages individually using pip*
python -m streamlit run app.py 
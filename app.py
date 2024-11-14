import streamlit as st
import google.generativeai as genai
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🎧 Audio Analysis with Gemini")
st.write("Upload an audio file and ask a question about its content!")

audio_file = st.file_uploader("Upload your audio file", type=['mp3', 'wav', 'm4a'])

question = st.text_input("What would you like to know about the audio?", "Describe this audio clip")

if audio_file is not None:
    try:
        temp_path = Path("temp_audio.mp3")
        with open(temp_path, "wb") as f:
            f.write(audio_file.getbuffer())
            
        with st.spinner("Analyzing audio..."):
            uploaded_file = genai.upload_file(temp_path)
            
            response = model.generate_content([uploaded_file, question])
            
            st.write("### Analysis:")
            st.write(response.text)
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        
    finally:
        if temp_path.exists():
            os.remove(temp_path)

with st.sidebar:
    st.markdown("""
    ### How to use this app:
    1. Upload an audio file (MP3, WAV, or M4A format)
    2. Type your question or use the default prompt
    3. Wait for Gemini to analyze the audio
    
    ### Note:
    - Ensure your audio file is clear for better results
    - Processing may take a moment depending on file size
    """)
# Audio-Analyzer-Streamlit-App-with-Gemini-for-Audio-Q-A
An Audio Question-Answering App with Google Gemini  This app is an interactive tool that allows users to upload audio files and ask questions about the content.   

  # Audio Insight: An Audio Question-Answering App with Google Gemini

This app is an interactive tool that allows users to upload audio files and ask questions about the content. Using Google’s Gemini 1.5 Flash model, the app generates answers based on the audio content, providing insights in real-time. Built with Streamlit, the app features a user-friendly interface for seamless audio analysis.

---

## Features

- **Upload Audio**: Supports `.mp3`, `.wav`, and `.m4a` files.
- **Ask Questions**: Type questions related to the audio content.
- **Instant Analysis**: Uses Google’s Gemini 1.5 Flash model to answer based on audio data.
- **Streamlit Interface**: Simple, web-based UI for easy interaction.

---

## Requirements

1. **Python** (version 3.7 or later)
2. **Python Libraries** (Install with `pip install -r requirements.txt`)
   - `streamlit`
   - `google-generativeai`
   - `python-dotenv`
3. **Google Gemini API Key**:
   - Sign up for access to Google Gemini 1.5 Flash model via Google Cloud.
   - Store the API key in a `.env` file as follows:
     ```plaintext
     GOOGLE_API_KEY=your_api_key_here
     ```
4. **Audio Files**:
   - Supported formats: `.mp3`, `.wav`, and `.m4a`

---

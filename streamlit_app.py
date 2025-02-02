import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import tempfile

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Error: Unable to recognize speech."
        except sr.RequestError:
            return "Error: Could not request results from speech recognition service."

def summarize_text(text, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"Summarize this speech: {text}")
    return response.text

def main():
    st.title("Speech Summarizer using Google Gemini")
    api_key = st.text_input("Enter your Google API Key", type="password")
    audio_value = st.audio_input("Record a voice message")
    
    if audio_value and api_key:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(audio_value.getvalue())
            temp_audio_path = temp_audio.name
        
        st.audio(audio_value)
        
        st.write("### Transcribing Audio...")
        transcript = transcribe_audio(temp_audio_path)
        st.text_area("Transcript", transcript, height=200)
        
        if "Error" not in transcript:
            st.write("### Generating Summary...")
            summary = summarize_text(transcript, api_key)
            st.text_area("Summary", summary, height=150)
        else:
            st.error("Failed to process audio. Try again with a clearer recording.")

if __name__ == "__main__":
    main()

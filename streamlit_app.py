import streamlit as st
import speech_recognition as sr

# Set the title of the app
st.title('Speech-to-Text with Streamlit')

# Add instructions
st.write("Click the button below and start speaking to convert speech into text:")

# Create a button for recording speech
if st.button('Start Recording'):
    recognizer = sr.Recognizer()

    # Record the speech
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google's Speech Recognition
            st.write("Recognizing...")
            text = recognizer.recognize_google(audio)
            st.write("You said: " + text)
        except sr.UnknownValueError:
            st.write("Sorry, I couldn't understand your speech.")
        except sr.RequestError:
            st.write("Sorry, there was an issue with the API request.")

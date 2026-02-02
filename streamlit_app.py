import streamlit as st
import google.generativeai as genai
from PIL import Image

st.title("My AI Project Manager (Gemini Edition) 🤖")

# קבלת מפתח ה-API מהמשתמש
api_key = st.sidebar.text_input("הכניסי Google API Key", type="password")

uploaded_file = st.file_uploader("תעלי תמונה של משימות/לוח", type=['png', 'jpg', 'jpeg'])

if uploaded_file and api_key:
    # הגדרת המודל
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    image = Image.open(uploaded_file)
    st.image(image, caption="הקובץ נקלט!", width=300)
    
    if st.button("נתחי משימות"):
        with st.spinner("Gemini מנתח את התמונה..."):
            try:
                # שליחת התמונה ל-AI
                response = model.generate_content([
                    "אתה עוזר אישי לניהול פרויקטים. תסתכל על התמונה ותמצת לי: מה המשימות שמופיעות כאן ומה סדר העדיפויות המומלץ?", 
                    image
                ])
                st.subheader("התובנות של ה-AI:")
                st.write(response.text)
            except Exception as e:
                st.error(f"שגיאה: {e}")

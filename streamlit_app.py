import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="AI Project Manager", layout="centered")
st.title("My AI Project Manager 🤖")

with st.sidebar:
    st.header("הגדרות")
    api_key = st.text_input("הכניסי Google API Key", type="password")

uploaded_file = st.file_uploader("בחרי תמונה...", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="התמונה הועלתה", use_column_width=True)
    
    if st.button("🚀 נתחי משימות"):
        if not api_key:
            st.error("אנא הכניסי API Key!")
        else:
            try:
                genai.configure(api_key=api_key)
                
                # בדיקה אילו מודלים זמינים למפתח שלך
                available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                
                # נסיון להשתמש ב-flash, ואם לא - בראשון שזמין
                model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
                
                st.write(f"מתחברת למודל: {model_name}") # זה יעזור לנו להבין מה קורה
                
                model = genai.GenerativeModel(model_name)
                
                with st.spinner("מנתחת..."):
                    response = model.generate_content(["נתח את המשימות בתמונה בעברית", image])
                    st.success("הנה הניתוח:")
                    st.write(response.text)
                    
            except Exception as e:
                st.error(f"אירעה שגיאה: {e}")

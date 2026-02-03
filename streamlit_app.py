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
    
    if st.button("🚀 נתחי משימות עכשיו"):
        if not api_key:
            st.error("חסר מפתח API!")
        else:
            try:
                genai.configure(api_key=api_key)
                # שימוש במודל העדכני ביותר ל-2026
                model = genai.GenerativeModel('gemini-2.0-flash')
                
                with st.spinner("מנתחת..."):
                    response = model.generate_content([
                        "נתח את המשימות בתמונה וסדר אותן בעברית.", 
                        image
                    ])
                    st.success("הנה הניתוח:")
                    st.write(response.text)
            except Exception as e:
                st.error(f"אירעה שגיאה: {e}")

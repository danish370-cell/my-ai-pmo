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
            st.error("אנא הכניסי API Key בתפריט הצד!")
        else:
            try:
                # הגדרה פשוטה וישירה
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                with st.spinner("מנתחת..."):
                    # שליחת התמונה לניתוח
                    response = model.generate_content([
                        "אתה עוזר ניהול פרויקטים. נתח את התמונה וחלץ משימות בעברית.", 
                        image
                    ])
                    st.success("הנה הניתוח:")
                    st.write(response.text)
            except Exception as e:
                # הדפסת השגיאה המלאה כדי שנבין אם משהו אחר השתבש
                st.error(f"אירעה שגיאה: {e}")

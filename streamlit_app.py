import streamlit as st
import google.generativeai as genai
from PIL import Image

# הגדרת דף בסיסית
st.set_page_config(page_title="AI Project Manager", layout="centered")

st.title("My AI Project Manager 🤖")
st.write("העלי תמונה של רשימת משימות, לוח מחיק או פתק, וה-AI ינתח אותם עבורך.")

# תפריט צד לקבלת המפתח
with st.sidebar:
    st.header("הגדרות")
    api_key = st.text_input("הכניסי Google API Key", type="password")
    st.info("ניתן להוציא מפתח ב-Google AI Studio")

# העלאת קובץ
uploaded_file = st.file_uploader("בחרי תמונה...", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="התמונה הועלתה בהצלחה", use_column_width=True)
    
    if st.button("🚀 נתחי משימות עכשיו"):
        if not api_key:
            st.error("אנא הכניסי API Key בתפריט הצד!")
        else:
            try:
                # הגדרת המודל עם השם המלא שגוגל דורשת
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                with st.spinner("מנתחת את התמונה, רק רגע..."):
                    # שליחת הבקשה
                    response = model.generate_content([
                        "אתה עוזר ניהול פרויקטים מקצועי. נתח את התמונה המצורפת, חלץ מתוכה את כל המשימות שאתה רואה, וסדר אותן ברשימה ברורה בעברית לפי סדר עדיפויות מומלץ.", 
                        image
                    ])
                    
                    st.success("הנה הניתוח שלי:")
                    st.markdown(response.text)
                    
            except Exception as e:
                st.error(f"אירעה שגיאה: {e}")
                st.info("טיפ: ודאי שהמפתח תקין ושהקובץ requirements.txt מכיל את google-generativeai")

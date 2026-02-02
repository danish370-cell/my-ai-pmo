import streamlit as st
import base64

st.set_page_config(page_title="AI Project Manager", page_icon="📥")

st.title("ניהול פרויקט אישי - ה-Inbox שלי 📥")
st.write("מנהלת פרויקטים יקרה, האתר שלך באוויר!")

# תיבת העלאה
uploaded_file = st.file_uploader("תעלי תמונה או מסמך", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    # המרה ל-Base64
    file_bytes = uploaded_file.getvalue()
    base64_string = base64.b64encode(file_bytes).decode()
    
    st.image(uploaded_file, caption="נקלט בהצלחה", width=300)
    st.success("הקובץ מוכן לעיבוד AI!")
    st.expander("קוד ה-Base64 של התמונה").text(base64_string[:100] + "...")

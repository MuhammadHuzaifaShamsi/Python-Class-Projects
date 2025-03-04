import streamlit as st
import re
import pyperclip

st.set_page_config(page_title="HUX Password Strength Meter")

st.title("🔐 HUX Password Strength Meter")

def check_password_strength(password):
    criteria = {
        " Length (≥8 chars)": len(password) >= 8,
        " Upper & Lowercase": bool(re.search(r'[A-Z]', password)) and bool(re.search(r'[a-z]', password)),
        " At least 1 digit (0-9)": bool(re.search(r'\d', password)),
        " Special char (!@#$%^&*)": bool(re.search(r'[!@#$%^&*]', password))
    }

    score = sum(criteria.values())

    if score == 4:
        strength = "Strong"
        color = "green"
    elif score == 3:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    return criteria, score, strength, color

password = st.text_input("Enter Password:", type="password")

if password:
    criteria, score, strength, color = check_password_strength(password)

    st.markdown("### ✅ Live Password Checks:")
    for key, value in criteria.items():
        status = "✅" if value else "❌"
        st.write(f"{status} {key}")

    st.markdown(f"### **Strength Level: 🛡️ `{strength}`**", unsafe_allow_html=True)

    if strength in ["Weak", "Moderate"]:
        st.warning("⚠️ Improve your password by meeting all the criteria above.")


    if strength == "Strong":
        st.markdown("### 📋 Copy Password:")
        st.text_area("Copy this password:", password, height=70)

        if st.button("📋 Copy to Clipboard", key="copy_btn"):
            pyperclip.copy(password)
            st.success("✅ Password copied to clipboard!")

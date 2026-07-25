import streamlit as st
import requests

# Title and Input Box
st.title("🔍 ScamScan - Scam Message Detector")
st.markdown("Paste any message or email to check if it's a scam!")

input_text = st.text_area("📩 Enter message here:")

# Scan Button
if st.button("Scan Now"):
    if not input_text.strip():
        st.warning("Please enter a message.")
    else:
        with st.spinner("Analyzing..."):
            try:
                # Send request to Flask backend
               response = requests.post(
                   "https://scamscan-ai.onrender.com/predict",
                   json={"text": input_text}
               )
                result = response.json()

                # Show prediction
                st.subheader("Result:")
                st.success(result["prediction"])
                st.progress(int(result["confidence"]))
                st.caption(f"Confidence: {result['confidence']}%")

            except Exception as e:
                st.error("Backend not reachable. Make sure Flask is running.")
                st.code(str(e))

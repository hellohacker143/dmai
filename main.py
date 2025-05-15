import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure your Google Generative AI API key
api_key = "AIzaSyDVHjHwybedvh_TJ0bZ1W7UIpFsGCGl6_U"
genai.configure(api_key=api_key)

st.title("AI-Powered Digital Marketing Toolkit")

# Sidebar menu
menu = st.sidebar.radio("Select Tool", ["Hashtag Generator", "Story Teller", "Image Teller"])

if menu == "Hashtag Generator":
    st.header("Hashtag Generator")
    topic = st.text_input("Enter a topic or keyword for hashtags:", "")
    number = st.number_input("Number of hashtags (max 30):", min_value=1, max_value=30, value=10)
    
    if st.button("Generate Hashtags"):
        if not topic.strip():
            st.error("Please enter a valid topic.")
        else:
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                prompt = f"Generate {number} relevant and trending hashtags for the topic: {topic}"
                response = model.generate_content(prompt)
                hashtags = response.text.strip().replace("\n", " ")
                st.success("Generated Hashtags:")
                st.write(hashtags)
            except Exception as e:
                st.error(f"API Error: {e}")

elif menu == "Story Teller":
    st.header("AI Story Teller")
    prompt = st.text_area("Write a prompt for your story:", "Write a story about digital marketing success")
    
    with st.expander("How to use Story Teller"):
        st.write("""
        - Enter a short prompt or theme.  
        - Click Generate Story.  
        - AI will create a story based on your input.  
        - Use this to generate marketing narratives or creative content.
        """)
    
    if st.button("Generate Story"):
        if not prompt.strip():
            st.error("Please enter a story prompt.")
        else:
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                st.subheader("Generated Story:")
                st.write(response.text)
            except Exception as e:
                st.error(f"API Error: {e}")

elif menu == "Image Teller":
    st.header("Image Teller - Describe Your Image")
    uploaded_file = st.file_uploader("Upload an image to get AI description", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        try:
            img = Image.open(uploaded_file)
            st.image(img, caption="Uploaded Image", use_column_width=True)
            
            model = genai.GenerativeModel("gemini-1.5-flash")
            # Note: This is a simple placeholder approach; real image understanding requires special API calls.
            prompt = "Describe this image in detail:"
            response = model.generate_content(prompt + " [Image attached]")
            st.subheader("AI Description:")
            st.write(response.text)
        except Exception as e:
            st.error(f"API Error: {e}")

else:
    st.write("Select a tool from the sidebar.")


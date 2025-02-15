import streamlit as st
import os
import warnings
from PIL import Image

# Suppress FutureWarnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Define base paths for datasets
BASE_PATHS = {
    "American Sign Language (ASL)": r"C:\Users\hongx\Downloads\Hand Gesture Detection\Data (American Sign Language)",
    "British Sign Language (BSL)": r"C:\Users\hongx\Downloads\Hand Gesture Detection\Data (British Sign Language)",
    "Bangladesh Sign Language (BDSL)": r"C:\Users\hongx\Downloads\Hand Gesture Detection\Data (Bangladesh Sign Language)",
    "Malaysia Sign Language (BIM)": r"C:\Users\hongx\Downloads\Hand Gesture Detection\Data (Malaysia Sign Language)",
    "Japan Sign Language (JSL)": r"C:\Users\hongx\Downloads\Hand Gesture Detection\Data (Japan Sign Language)"
}

# Define gestures available for each sign language
GESTURES = {
    "American Sign Language (ASL)": {
        "Alphabet": ["Display All"] + [f"{letter} (ASL)" for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
        "Digit": ["Display All"] + [f"{i} (ASL)" for i in range(10)],
        "Common": ["Display All", "Call Me", "Dislike", "Drink", "F-You", "Food", "Forever", "Good Job",
                   "Good Luck", "Hello", "I Love You", "Loser", "Ok", "Pain", "Rock On", "Victory"]
    },
    "British Sign Language (BSL)": {
        "Digit": ["Display All"] + [f"{i} (BSL)" for i in range(10)],
        "Common": ["Display All", "Bad", "Deaf", "Hello", "I", "Middle Finger", "Relax", "Thank You"]
    },
    "Bangladesh Sign Language (BDSL)": {
        "Digit": ["Display All"] + [f"{i} (BDSL)" for i in range(10)],
        "Common": ["Display All", "Aj (Today)", "Ami (I am)", "Ashirbad (Blessing)", "Bati (Bowl)", "Biyog (Separation)",
                   "Darao (Stop)", "Desh (Country)", "Ekhane (Here)", "Kothay (Where)", "Puru (Thick)",
                   "Shundor (Beautiful)", "Tahara (They)"]
    },
    "Malaysia Sign Language (BIM)": {
        "Common": ["Display All", "Air", "Demam", "Dengar", "Makan", "Minum", "Salah", "Saya", "Senyap", "Tidur", "Waktu"]
    },
    "Japan Sign Language (JSL)": {
        "Syllabary": ["Display All", "a", "e", "i", "ka", "ke", "ki", "ko", "ku", "na", "ni", "nu", "o",
                      "sa", "se", "si", "so", "su", "ta", "te", "ti", "to", "tu", "u"]
    }
}

# Function to get the first image in a folder
def get_first_image(language, category, gesture):
    base_path = BASE_PATHS[language]
    folder_path = os.path.join(base_path, category, gesture)

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if image_files:
            return os.path.join(folder_path, image_files[0])  # Return the first image only
    return None

# Function to display images
def display_images(language, category, gesture):
    if gesture == "Display All":
        st.subheader(f"📷 Showing first image of each {category} in {language}")
        col1, col2 = st.columns(2)  # Two-column layout

        for index, gesture_name in enumerate(GESTURES[language][category][1:]):  # Skip "Display All"
            image_path = get_first_image(language, category, gesture_name)
            if image_path:
                img = Image.open(image_path)
                with col1 if index % 2 == 0 else col2:
                    st.image(img, caption=gesture_name, use_container_width=True)
            else:
                st.warning(f"⚠️ No images found for {gesture_name}!")
    else:
        st.subheader(f"📷 Showing {gesture} in {language}")
        image_path = get_first_image(language, category, gesture)
        if image_path:
            st.image(Image.open(image_path), caption=gesture, use_container_width=True)
        else:
            st.warning("⚠️ No images found!")

# Streamlit UI - Sidebar for Selections
st.set_page_config(page_title="Sign Language Recognition", page_icon="🤟", layout="wide")

st.sidebar.title("🌍 Choose Your Sign Language")
language = st.sidebar.selectbox("Select Language:", list(BASE_PATHS.keys()))

st.sidebar.subheader("📁 Choose a Category")
category = st.sidebar.selectbox('Select Category:', list(GESTURES[language].keys()))

st.sidebar.subheader("🤟 Choose a Gesture")
gesture = st.sidebar.selectbox('Select Gesture:', GESTURES[language][category])

# Main content
st.title("📚 Welcome to E-braille Sign Language Education Website")
st.write("Select a category and gesture to learn sign language.")

# Display images based on selection
display_images(language, category, gesture)

# Footer
st.markdown("""
---
🔹 **Developed by E-braille** | 🤟 *Education Hand Gesture for Future !*  
""", unsafe_allow_html=True)

#Loqo
logo_path = r"C:\Users\hongx\Downloads\Hand Gesture Detection\Logo E-braille.png"  # Replace with actual path
st.image(logo_path, width=150)

#Background Setup
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Example usage (Replace with your own image URL)
set_background("https://i.pinimg.com/originals/f6/b1/10/f6b11053f863f0aa918ddebbb04bafa7.gif")
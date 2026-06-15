import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# ---------------- CONFIG ----------------
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- SETTINGS ----------------
POEMS_FOLDER = "poems"

st.set_page_config(page_title="Hindi Poetry Gallery", layout="centered")

st.title("📜 Hindi Handwritten Poetry Collection")
st.write("All poems loaded from local folder and transcribed using AI.")

# ---------------- GET FILES ----------------
image_files = [
    f for f in os.listdir(POEMS_FOLDER)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

image_files.sort()  # keeps order consistent

# ---------------- DISPLAY ----------------
if not image_files:
    st.warning("No images found in poems folder.")
else:

    for idx, filename in enumerate(image_files):

        file_path = os.path.join(POEMS_FOLDER, filename)

        st.markdown("---")
        st.subheader(f"📖 Poem {idx + 1}: {filename}")

        # Show image
        image = Image.open(file_path)
        st.image(image, use_container_width=True)

        # Read bytes
        with open(file_path, "rb") as f:
            img_bytes = f.read()

        # Transcribe
        with st.spinner("Transcribing with AI... ⏳"):

            try:
                response = model.generate_content([
                    """
                    Transcribe this handwritten Hindi poem exactly as written.

                    Rules:
                    - Do NOT translate
                    - Do NOT summarize
                    - Preserve line breaks
                    - Keep original spelling
                    - If unclear word, write [unclear]
                    """,
                    {
                        "mime_type": "image/jpeg",
                        "data": img_bytes
                    }
                ])

                st.success("Done")

                st.text_area(
                    "📝 Hindi Text",
                    response.text,
                    height=300,
                    key=f"text_{idx}"
                )

            except Exception as e:
                st.error(f"Error processing {filename}")
                st.exception(e)

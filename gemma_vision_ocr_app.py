import streamlit as st
import ollama
from PIL import Image
import io
import json

# Page configuration
st.set_page_config(
    page_title="Gemma-4B OCR",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

class GemmaOCRApp:
    @staticmethod
    def extract_text(uploaded_file):
        """
        Extract structured text from the uploaded image using Gemma-4B
        
        Args:
            uploaded_file: Uploaded image file
        
        Returns:
            dict: Extracted text content
        """
        try:
            # Attempt structured extraction 
            response = ollama.chat(
                model='gemma3:4b',  # Updated to gemma:4b
                messages=[{
                    'role': 'user',
                    'content': """Analyze the text in the provided image. Your task is to:
                    1. Extract ALL readable text content
                    2. Provide a detailed, structured analysis including:
                       - Raw extracted text
                       - Line count
                       - Word count
                       - Key entities (if any)
                    3. Format the output as a clear, readable response""",
                    'images': [uploaded_file.getvalue()]
                }]
            )
            
            # Process the response
            raw_text = response.message.content
            return {
                "raw_text": raw_text,
                "line_count": len(raw_text.split('\n')),
                "word_count": len(raw_text.split()),
                "entities": GemmaOCRApp._extract_entities(raw_text)
            }
        
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            return None

    @staticmethod
    def _extract_entities(text):
        """
        Basic entity extraction from the text
        
        Args:
            text (str): Input text
        
        Returns:
            dict: Extracted entities
        """
        import re
        
        return {
            "emails": re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text),
            "phone_numbers": re.findall(r'\b(?:\+\d{1,2}\s?)?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}\b', text),
            "urls": re.findall(r'https?://\S+|www\.\S+', text)
        }

def main():
    # Custom styling
    st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.title("🔎 Gemma-4B OCR Vision")
    st.markdown("Extract and analyze text from images")

    # Sidebar for image upload
    with st.sidebar:
        st.header("📤 Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image...", 
            type=['png', 'jpg', 'jpeg', 'bmp', 'gif']
        )
        
        # Image preview
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

    # Main content area
    if uploaded_file:
        if st.button("Extract Text 🔍", type="primary"):
            with st.spinner("Processing image with Gemma-4B..."):
                # Extract text
                ocr_result = GemmaOCRApp.extract_text(uploaded_file)
                
                # Display results
                if ocr_result:
                    # Raw Text
                    st.subheader("📄 Extracted Text")
                    st.code(ocr_result['raw_text'], language="text")
                    
                    # Text Metrics
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Lines", ocr_result['line_count'])
                    with col2:
                        st.metric("Words", ocr_result['word_count'])
                    
                    # Entities
                    if any(ocr_result['entities'].values()):
                        st.subheader("🔍 Detected Entities")
                        st.json(ocr_result['entities'])
                else:
                    st.error("Failed to extract text from the image.")
    else:
        st.info("Upload an image to begin text extraction.")

    # Footer
    st.markdown("---")
    st.markdown("Powered by Gemma-4B | Local OCR Extraction")

if __name__ == "__main__":
    main()

# Installation Requirements:
# 1. Install Ollama (https://ollama.com/)
# 2. Pull Gemma model: ollama pull gemma:4b
# 3. Install Python dependencies:
#    pip install streamlit ollama pillow
# 4. Run the app:
#    streamlit run gemma_ocr_app.py
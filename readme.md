# Gemma-4B OCR Vision App

## 🚀 Project Overview
A local, AI-powered Optical Character Recognition (OCR) application using Gemma-4B and Streamlit. Extract and analyze text from images directly on your machine.

## 📋 Prerequisites
- Python 3.8+
- Ollama
- pip (Python package manager)

## 🛠️ Installation Steps

### 1. Install Ollama
- Visit [Ollama's official website](https://ollama.com/)
- Download and install the application for your operating system

### 2. Pull Gemma-4B Model
Open Terminal/Command Prompt and run:
```bash
ollama pull gemma:4b
```

### 3. Set Up Python Environment
```bash
# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install required dependencies
pip install streamlit ollama pillow
```

## 🖥️ Running the Application
```bash
streamlit run gemma_ocr_app.py
```

## 🔧 Troubleshooting

### Common Issues
1. **Model Not Found**
   - Ensure Ollama is running
   - Verify model is pulled: `ollama list`
   - Restart Ollama application

2. **Python Dependencies**
   ```bash
   # Upgrade pip and dependencies
   pip install --upgrade pip
   pip install --upgrade streamlit ollama pillow
   ```

3. **Ollama Connection**
   - Check if Ollama is running
   - Restart Ollama desktop application
   - Verify model is correctly pulled

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 📄 License
MIT

## 🙌 Acknowledgments
- Ollama for local AI model serving
- Streamlit for the web application framework
- Google's Gemma team
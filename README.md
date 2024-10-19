# 🎙️ STT-APP: Real-Time Speech Recognition App

## ✨ Features

- 🚀 Real-time speech-to-text conversion
- 🌐 Web-based interface for easy access
- 🎛️ Support for both microphone input and audio file upload
- 🧠 Powered by state-of-the-art AI models
- 🔧 Customizable and extensible architecture
- 📊 Detailed logging for performance monitoring

## 🛠️ Technology Stack

- **Frontend**: Gradio for an intuitive and responsive user interface
- **Backend**: FastAPI for a high-performance, easy-to-use API
- **AI Model**: Transformers library for advanced speech recognition
- **Testing**: Pytest for robust unit testing

## 🚀 Quick Start

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/SpeechWave.git
   cd SpeechWave
   ```

2. Install the required dependencies:
   ```
   pip install -e .
   ```

3. Start the Gradio app:
   ```
   python src/app/main.py
   ```

4. In a separate terminal, start the FastAPI server:
   ```
   python src/remote_api/main.py
   ```

5. Open your web browser and navigate to the URL provided by Gradio (typically http://localhost:7860).

## 🧪 Testing

Run the test suite to ensure everything is working correctly:

```
pytest
```

---
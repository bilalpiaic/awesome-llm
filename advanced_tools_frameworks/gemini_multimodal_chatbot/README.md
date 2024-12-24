## 📄 README: Multimodal Chatbot with Gemini Flash ⚡️

### 🚀 Project Overview
This Streamlit app leverages **Google’s Gemini 1.5 Flash** to create a multimodal chatbot that accepts both **text and image inputs**. Users can upload images and enter text queries, and the chatbot responds with lightning-fast results powered by Gemini Flash.

---

### 🎯 Features
- **Multimodal Capabilities**: Chat with both text and images. Upload an image and ask questions about it.
- **Gemini Flash Integration**: Utilizes **Google's Gemini 1.5 Flash** model for fast and accurate responses.
- **Seamless Interface**: Simple and intuitive Streamlit interface.
- **Dynamic Chat History**: Maintains conversation history for a better user experience.

---

### 🛠️ Requirements
- **Python 3.7+**
- **Streamlit**: `pip install streamlit`
- **Google Generative AI SDK**: `pip install google-generativeai`
- **Pillow (PIL)**: `pip install pillow`

---

### 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bilalpiaic/omega-llm/gemini_multimodal_chatbot.git
   cd multimodal-chatbot-gemini-flash
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run gemini_multimodal_chatbot.py
   ```

---

### 🔑 How to Use
1. **Enter your Google API Key** when prompted.
2. **Upload an image** (jpg, jpeg, png) from the sidebar.
3. **Ask a question** in the chat box. The app will process the image and respond.
4. **View responses** in a continuous chat format, with conversation history maintained.

---

### ⚡ Example Use Cases
- **Medical Imaging**: Upload an X-ray and ask for potential insights.  
- **Product Descriptions**: Upload a product photo and generate descriptions.  
- **Landmark Identification**: Upload travel photos and ask about the landmarks.  

---

### 🚧 Notes
- Ensure you have a **valid Google API key**.
- The app requires an **active internet connection** to interact with Gemini Flash.

---

### 🤝 Contributions
Contributions are welcome! Feel free to open a pull request or raise an issue.

---

## 📧 Contact
- **Author**: Muhammad Bilal Siddique 
- **LinkedIn**: [Your LinkedIn](https://www.linkedin.com/in/muhammad-bilal-siddique-b7967233b)  
- **GitHub**: [Your GitHub](https://github.com/bilalpiaic)

2. Get your Google Studio API Key

- Sign up for an [Google AI Studio](https://aistudio.google.com/app/apikey) and obtain your API key.

3. Run the Streamlit App
```bash
streamlit run gemini_multimodal_chatbot.py
```
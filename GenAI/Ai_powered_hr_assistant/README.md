# AI-Powered HR Assistant for Nestlé HR Policy

## 🏢 Project Overview

This project creates an intelligent conversational chatbot that can answer queries about Nestlé's HR policies and procedures. The assistant uses advanced AI technologies including OpenAI's GPT-3.5 Turbo model, LangChain for document processing, and Gradio for the user interface.

## 🎯 Project Objectives

- **Extract and Process**: Load and process Nestlé's HR policy PDF document
- **Vectorize Content**: Create vector representations of text chunks using ChromaDB and OpenAI embeddings
- **Question-Answering**: Build a retrieval-based QA system using GPT-3.5 Turbo
- **User Interface**: Create an intuitive chatbot interface using Gradio
- **Deploy**: Make the assistant accessible for practical use

## 🚀 Features

- **Interactive Chat Interface**: User-friendly Gradio-based chatbot
- **Context-Aware Responses**: Answers based on official Nestlé HR policy documents
- **Source References**: Responses include references to source documents
- **Example Questions**: Pre-loaded examples for easy testing
- **Conversation Logging**: Optional conversation history tracking


## 📋 Requirements

### System Requirements
- Python 3.8 or higher
- Internet connection for OpenAI API calls
- Minimum 4GB RAM recommended

### Dependencies
```
openai>=1.0.0
gradio>=4.0.0
langchain>=0.1.0
pypdf>=3.0.0
chromadb>=0.4.0
tiktoken>=0.5.0
python-dotenv>=1.0.0
```

## 🛠️ Installation

### 1. Clone or Download the Project
```bash
# If using git
git clone <repository-url>

# Or download and extract the project files
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up OpenAI API Key
1. Get your API key from [OpenAI Platform](https://platform.openai.com/)
2. create .env file and replace your API key as -
```
    OPENAI_API_KEY=<your-actual-api-key-here>
```

## 📖 Usage

### Running the Jupyter Notebook

1. **Start Jupyter Notebook**:
```bash
jupyter notebook hr_assistant.ipynb
```

2. **Execute Cells in Order**:
   - Run each cell sequentially from top to bottom
   - Wait for each cell to complete before proceeding
   - The final cell will launch the Gradio interface

3. **Access the Chatbot**:
   - The Gradio interface will provide a local URL (e.g., `http://127.0.0.1:7860`)
   - A public shareable link will also be generated
   - Open the URL in your web browser

### Using the HR Assistant

1. **Ask Questions**: Type your HR policy questions in natural language
2. **Try Examples**: Use the provided example questions to get started
3. **Review Responses**: The assistant will provide detailed answers with source references
4. **Clear Chat**: Use the clear button to start a new conversation

### Example Questions

- "What is Nestlé's approach to employee development?"
- "How does Nestlé handle performance evaluations?"
- "What are the total rewards offered to employees?"
- "What is Nestlé's policy on work-life balance?"
- "How does Nestlé support diversity and inclusion?"
- "What training opportunities are available?"


```

## 📁 Project Structure

```
ADV-GEN-AI/1756299048_cep_1_crafting_an_ai_powered_hr_assistant/
├── hr-assistant-nestle.ipynb          # Main Jupyter notebook
├── README.md                          # This documentation
├── Dataset/
│   └── the_nestle_hr_policy_pdf_2012.pdf  # HR policy document
├── Course_End_Project_Crafting_an_AI_Powered_HR_Assistant.pdf  # Project requirements
├── Gradio_Documentation.pdf   # Gradio reference
└── chroma_db/                 # Vector database (created during execution)
```

## 🔧 Configuration

### Model Parameters
- **Model**: GPT-3.5 Turbo
- **Temperature**: 0.3 (for consistent responses)
- **Max Tokens**: 500
- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters

### Retrieval Settings
- **Search Type**: Similarity search
- **Number of Retrieved Chunks**: 3
- **Embedding Model**: OpenAI text-embedding-ada-002

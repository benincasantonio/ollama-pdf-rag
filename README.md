# OLLAMA PDF RAG SYSTEM

## Overview
This project implements a PDF-based Retrieval-Augmented Generation (RAG) system inspired by [this YouTube video](https://www.youtube.com/watch?v=GWB9ApTPTv4&t=7842s). It uses LangChain, Ollama, and Chroma to process PDF documents, split them into chunks, create a vector database, and retrieve relevant information based on user queries. The system is designed for learning purposes and demonstrates key concepts in building a RAG pipeline.

## Features
- Load and process PDF documents
- Split PDF into manageable text chunks
- Persist and query a vector database for efficient document retrieval.
- Generate vector embeddings for document chunks using Ollama embeddings
- Create a query-answering chain powered by ChatOllama
- Seamlessly use Ollama for answering questions about your documents.
- Accessible through:
  - **Streamlit Web App**: A user-friendly graphical interface.
  - **CLI**: For quick and direct access to the functionality.

## Requirements
To run this project, follow these steps:

1. Install the required Python dependencies using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

2. Install Ollama on your local machine. Refer to [Ollama's installation guide](https://ollama.ai) for details.

3. Download and install the `llama3.2` model (or any other model you want to use) on your local Ollama instance. If you want to use a different model, please make sure you change the `MODEL_NAME` constant in the code.

4. Place your PDF document in the `./data` folder and update the `DOC_PATH` variable in `config.py`.

## File Structure
- **`src/`**: Contains all source code.
  - `pdf_rag.py`: Core logic for the RAG pipeline.
  - `config.py`: Configuration file for constants and paths.
  - `main.py`: Entry point for running the system.
  - `streamlit_app.py`: Streamlit web app for interactive usage.
- **`requirements.txt`**: A list of dependencies required to run the project.
- **`data/LLMs_Safety.pdf`**: The sample PDF document used for testing.

## Usage

### **1. Streamlit Web App**

```bash
streamlit run streamlit_app.py
```
This will start the web application on http://localhost:8501.
1. Open the app in your browser.
2. Enter your question in the provided text box.
3. Click "Process" to retrieve answers based on your PDF.

### **2. Command-Line Interface (CLI)**

To launch the Streamlit app, use the following command:
1. Run the script:

   ```bash
   python src/main.py
   ```
2. View the generated responses in the console.

## Example Query and Response
Here is an example of a query and its response:

**Query:** "Give me a detailed summary of the document."

**Example Response:**
```
Response: 
The document appears to be a technical report or academic paper related to the safety and security of Large Language Models (LLMs). Here is a detailed summary:

### **Introduction**
The document discusses the importance of ensuring the safety and security of LLMs, which have become increasingly prevalent in various applications. The authors highlight the need for a better understanding of LLMs' abilities, limitations, and potential risks.

### **Concept Formation and Storage**
The report focuses on three dimensions of LLM abilities: concept formation and storage, mechanisms underlying in-context learning, and generalization/emergence of LLM abilities. Concept formation and storage refers to how LLMs learn and represent concepts, which is essential for understanding their decision-making processes.

### **Interpretability**
The authors emphasize the importance of interpretability in understanding LLMs' behavior and identifying potential safety risks. They discuss various methods for interpreting LLMs, including concept formation and memorization, mechanisms underlying in-context learning, and generalization/emergence of LLM abilities.

### **Potential Risks**
The report highlights several potential risks associated with LLMs, including:

1. **Dual-Use**: The same technology being applicable for both beneficial and harmful purposes.
2. **Adversarial Attacks**: Weaknesses that can be exploited to manipulate or deceive the model.
3. **Misunderstanding or Over-Trust in Explanations**: Over-reliance on interpretability methods, leading to inaccurate or incomplete understanding of LLMs' behavior.

### **Future Directions**
The authors propose several future research directions to address the limitations of current interpretability methods:

1. **More Complex Models and Real-World Applications**: Researching more complex models and their behavior in real-world applications.
2. **Practical Interpretability Methods**: Developing more practical and reliable interpretability methods for industrial applications.

### **Misuse**
The report discusses various types of misuse, including:

1. **Weaponization**: Using LLMs for malicious purposes, such as invading privacy or exacerbating biases.
2. **Risks of Misuse in Weapons Acquisition**: The risks associated with acquiring and using LLMs for military or other malicious purposes.

### **Mitigation Methods**
The authors propose several mitigation methods to address the potential risks, including:

1. **External Safeguards**: Implementing external controls to prevent misuse, such as auditing and testing.
2. **Internal Protection**: Implementing internal protections, such as regularization and bias correction.
3. **Evaluation**: Evaluating LLMs' performance and behavior to identify potential risks.

### **Deepfakes**
The report briefly discusses the issue of deepfakes, which are generated using LLMs or other deep learning models. The authors highlight the potential risks associated with deepfakes, including spreading misinformation and manipulating public opinion.

Overall, the document provides a comprehensive overview of the safety and security concerns related to LLMs and proposes several research directions and mitigation methods to address these concerns.
```


## Credits
This project was made during watching [this video course from FreeCodeCamp's YouTube channel](https://www.youtube.com/watch?v=GWB9ApTPTv4&t=7842s).

Additionally, the project utilizes the PDF: ["Large Language Model Safety: A Holistic Survey"](https://arxiv.org/pdf/2412.17686) as the example document.

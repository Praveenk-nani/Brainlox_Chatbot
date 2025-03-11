# 🌟 Brainlox Course Chatbot

Welcome to the **Brainlox Course Chatbot**! This is a **Flask-based retriever chatbot** that fetches relevant course details from the Brainlox website based on your queries. The chatbot uses **LangChain, FAISS, and Hugging Face embeddings** for efficient similarity-based retrieval.

---

## 🚀 **How to Run the Project**

### **1 Clone the Repository**
First, clone this repository to your local machine:

### Example
git clone https://github.com/your-repo-url.git
cd brainlox-chatbot

### **2 Activate Virtual Environment**
Before running the project, activate the virtual environment named internTaskEnvironment


### **3 Install Required Dependencies**
If you haven’t installed the dependencies yet, run:
#### pip install -r requirements.txt

### **4 Run the Flask Server**
Once the environment is activated, start the server by running:

#### python mian.py

after running, the Flask server will start at
#### http://127.0.0.1:5000/.


### **Access the Chatbot**
Open a web browser and go to:

#### http://127.0.0.1:5000/
-> An *HTML page* will appear with a *search placeholder*.
-> Type your *question* related to courses (e.g., "Tell me about Java courses").
-> Click *Submit*, and the chatbot will fetch the best course details from the retriever.



### **Troubleshooting & FAQs**

1. Getting **ModuleNotFoundError** for LangChain imports?
->✅Ensure you have installed the correct dependencies:
*pip install langchain langchain_community langchain_huggingface*

 2. API returns a **415** error in Postman?
✅ Make sure you send JSON data with proper headers:

*{*
   *"question": "Tell me about Java courses"*
*}*

✅ Set headers in Postman:
*Key: Content-Type   |  Value: application/json*


 3. Facing a **TypeError** when submitting a query?

 -> ✅ Ensure you are using the correct retriever method in main.py:

 *results = retriever.invoke(user_input)*


 # Developed by **Praveenkumar**
 # Contact : praveenkyalamancha@yahoo.com
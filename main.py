from flask import Flask,request,jsonify,render_template
from langchain_community.vectorstores import FAISS as fa
from langchain_community.embeddings import HuggingFaceEmbeddings


vectordb = fa.load_local(
    "model/faiss_index",
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
    allow_dangerous_deserialization=True
)


retriever = vectordb.as_retriever()


app = Flask(__name__)



@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/query",methods=["POST"])
def queryPage():

    data = request.get_json()

    if not data or "question" not in data:
        return jsonify({"error":"Invalid request. please send json with a question field"}),400
    
    user_input = data["question"]
    # user_input = request.json.get("question")
    results = retriever.invoke(user_input)


    if results:
        response = results[0].page_content
    else:
        response = "No relevant course found"
    
    return jsonify({"response":response})



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
import os
import requests
import chromadb
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter

MODEL_NAME = "hf.co/rippertnt/HyperCLOVAX-SEED-Text-Instruct-1.5B-Q4_K_M-GGUF:Q4_K_M"
EMBED_MODEL = "mxbai-embed-large"
MD_FILE_PATH = "pinky_library.md"
DB_PATH = "./pinky_rag_db"

if not os.path.exists(MD_FILE_PATH):
    raise FileNotFoundError(f"{MD_FILE_PATH}를 현재 폴더에 준비하세요.")

chroma = chromadb.PersistentClient(path=DB_PATH)
embed_fn = embedding_functions.OllamaEmbeddingFunction(
    model_name=EMBED_MODEL, url="http://localhost:11434/api/embeddings"
)
collection = chroma.get_or_create_collection(
    name="pinky_docs", embedding_function=embed_fn
)

if collection.count() == 0:
    with open(MD_FILE_PATH, "r", encoding="utf-8") as f:
        document = f.read()
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50
    ).split_text(document)
    collection.add(
        ids=[f"pinky_{i}" for i in range(len(chunks))], documents=chunks
    )
    print(f"새 DB 생성: {len(chunks)}개 chunk")
else:
    print(f"기존 DB 로드: {collection.count()}개 chunk")


def search(query, top_k=3):
    count = collection.count()
    if count == 0:
        return []
    result = collection.query(query_texts=[query], n_results=min(top_k, count))
    return result.get("documents", [[]])[0]


def ask_ollama(model, prompt):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        },
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]


def chat():
    print(f"Model: {MODEL_NAME}\nexit 입력 시 종료")
    while True:
        question = input("\n질문: ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue
        docs = search(question, top_k=3)
        context = "\n\n".join(docs) or "관련 문서를 찾지 못했습니다."
        prompt = f"""다음 Context만 근거로 질문에 답하세요.
Context에 없는 내용은 추측하지 말고 모른다고 답하세요.

[Context]
{context}

[Question]
{question}
"""
        print("\n[검색 문서]\n", context)
        print("\n[답변]\n", ask_ollama(MODEL_NAME, prompt))


if __name__ == "__main__":
    chat()

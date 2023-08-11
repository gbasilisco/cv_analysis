import os
import docx
import fitz  # PyMuPDF
from transformers import BertTokenizer, BertModel
import torch

# Impostazioni
folder_path = "Download/"  # Inserisci il percorso della cartella con i CV
similarity_threshold = 0.8  # Soglia di similarità

# Funzione per estrarre il testo da un file DOCX o PDF
def extract_text_from_file(file_path):
    if file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])
    elif file_path.endswith(".pdf"):
        pdf_document = fitz.open(file_path)
        pdf_text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            pdf_text += page.get_text("text")
        return pdf_text
    else:
        return ""

# Caricamento del tokenizzatore e del modello BERT preaddestrato
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Ottenere la lista di file nella cartella
cv_files = [file for file in os.listdir(folder_path) if file.endswith((".docx", ".pdf"))]

# Estrai il testo e crea gli embeddings BERT
cv_texts = [extract_text_from_file(os.path.join(folder_path, file)) for file in cv_files]
inputs = tokenizer(cv_texts, padding=True, truncation=True, return_tensors="pt")
with torch.no_grad():
    embeddings = model(**inputs).last_hidden_state.mean(dim=1)

# Calcolo della similarità
similar_cv_pairs = []
for i in range(len(cv_files)):
    for j in range(i + 1, len(cv_files)):
        similarity = torch.cosine_similarity(embeddings[i], embeddings[j], dim=0).item()
        if similarity > similarity_threshold:
            similar_cv_pairs.append((cv_files[i], cv_files[j]))

# Stampa dei CV simili
if similar_cv_pairs:
    print("Coppie di CV simili:")
    for cv1, cv2 in similar_cv_pairs:
        print(f"{cv1} è simile a {cv2}")
else:
    print("Nessuna coppia di CV simili trovata.")

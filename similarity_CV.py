import os
import docx
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Impostazioni
folder_path = "CV/"  # Inserisci il percorso della cartella con i CV
similarity_threshold = 0.8  # Soglia di similarità

# Funzione per estrarre il testo da un file
def extract_text_from_file(file_path):
    if file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return text
    elif file_path.endswith(".pdf"):
        pdf_text = ""
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            pdf_text = "\n".join([page.extract_text() for page in pdf_reader.pages])
        return pdf_text
    else:
        return ""

def similarity():
    similar_CV = []

    # Ottenere la lista di file nella cartella
    cv_files = [file for file in os.listdir(folder_path) if file.endswith((".docx", ".pdf"))]

    # Estrai il testo e crea i vettori TF-IDF
    vectorizer = TfidfVectorizer()
    cv_texts = [extract_text_from_file(os.path.join(folder_path, file)) for file in cv_files]
    tfidf_matrix = vectorizer.fit_transform(cv_texts)

    # Calcolo della similarità
    similar_cv_pairs = []
    for i in range(len(cv_files)):
        for j in range(i + 1, len(cv_files)):
            similarity = cosine_similarity(tfidf_matrix[i], tfidf_matrix[j])[0][0]
            if similarity > similarity_threshold:
                similar_cv_pairs.append((cv_files[i], cv_files[j]))

    # Stampa dei CV simili
    if similar_cv_pairs:
        print("Coppie di CV simili:")
        for cv1, cv2 in similar_cv_pairs:
            print(f"{cv1} è simile a {cv2}")
            similar_CV.append(f"{cv1} è simile a {cv2}")
    else:
        print("Nessuna coppia di CV simili trovata.")

    return similar_CV

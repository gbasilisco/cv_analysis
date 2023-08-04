import os
import docx
import sys
from PyPDF2 import PdfReader

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Inserisci le parole chiave separate da spazi \n Usage: python3 main.py parola_chiave1 parola_chiave2 ...")
    else:
        # Ottieni le parole chiave dalla riga di comando
        keywords = sys.argv[1:]

        # Ottieni il percorso della cartella corrente
        folder_path = "Download/"

        # Inizializza una lista vuota per i nomi dei file che contengono tutte le parole chiave
        matching_files = []

        # Scorri tutti i file nella cartella corrente
        for filename in os.listdir(folder_path):
            # Verifica se il file ha estensione .docx
            if filename.endswith(".docx"):
                # Apri il file DOCX e leggi tutto il contenuto
                doc = docx.Document(os.path.join(folder_path, filename))
                text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            elif filename.endswith(".pdf"):
                # Apri il file PDF e leggi tutto il contenuto
                with open(os.path.join(folder_path, filename), "rb") as pdf_file:
                    pdf_reader = PdfReader(pdf_file)
                    text = "\n".join([page.extract_text() for page in pdf_reader.pages])

            # Verifica se tutte le parole chiave sono presenti nel contenuto del file
            all_keywords_present = all(keyword.lower() in text.lower() for keyword in keywords)

            if all_keywords_present:
                # Se tutte le parole chiave sono presenti, aggiungi il nome del file alla lista
                matching_files.append(filename)

        # Stampa i nomi dei file che contengono tutte le parole chiave
        print("I seguenti file contengono tutte le parole chiave:")
        for filename in matching_files:
            print(filename)



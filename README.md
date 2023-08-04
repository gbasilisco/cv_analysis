### Features

- Download all CV by Google Drive, reference folder_id in download_cv.py
- Search multiple keywords in docx and pdf file
- Check CV similarity present in folder by 

# cv_analysis
 CV Analysis Tool

 The Python-based CV Analysis Tool is a robust utility designed to streamline and enhance the process of analyzing and managing a collection of CVs (Curriculum Vitae). Leveraging the capabilities of the Python programming language, this tool offers a range of advanced features that contribute to a more efficient and organized workflow:

Google Drive Integration: Seamlessly download all CVs stored on Google Drive using the provided download_cv.py script, which is written in Python. By referencing the folder_id, the tool allows easy access to specific folders, ensuring that you can effortlessly fetch the necessary CVs for analysis.

Keyword Search Capability: Harnessing the power of Python, the CV Analysis Tool enables you to conduct comprehensive searches for multiple keywords within both DOCX and PDF files of the CVs. This Python-driven feature empowers you to efficiently extract relevant information, such as skills, qualifications, and experiences, from a vast array of CVs.

CV Similarity Check: Developed using Python, the tool employs advanced algorithms to assess the content of various CVs within a designated folder. By determining potential overlaps in skills, work history, or other key attributes, it aids in recognizing patterns and identifying candidates with comparable qualifications.

In summary, the Python-based CV Analysis Tool significantly streamlines the CV review and comparison process. By enabling easy CV retrieval from Google Drive through its Python script, offering comprehensive keyword search capabilities, and providing a Python-driven CV similarity assessment, it enhances your ability to efficiently evaluate and manage a collection of CVs. This tool, developed with Python's versatility, is an invaluable asset for anyone involved in talent acquisition, recruitment, or HR management.

# How to you use

 1. download **cv_analysis** from github
     `git clone https://github.com/gbasilisco/cv_analysis.git`
 2. open directory `cv_analysis`, or unzip zip file downloaded and install required python package with `pip3`
 3. create from console.cloud.google your OAuth 2.0 Client IDs you can follow this guide https://developers.google.com/drive/api/quickstart/python
 4. copy client_secret json file in the root of `cv_analysis`
 5. modify 
 
    ```python
    flow = InstalledAppFlow.from_client_secrets_file( 
        'SECRET_CLIENT.json', SCOPES) 
    creds = flow.run_local_server(port=0)
    ```
to insert the name of your client_secret json file downloaded from Google Cloud Console

6. create a empty file `token.json`
7. to download use `python3 download_cv.py`
8. to search multiple keywords use `python3 main.py key1 key2 ...`
9. to check CV similarity `python3 similarity_CV.py`

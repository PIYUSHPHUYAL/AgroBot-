import os
import re
import pandas as pd
import PyPDF2
import docx

def read_pdf(file_path):
    """Extract text from PDF files"""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    return text

def read_word(file_path):
    """Extract text from Word documents"""
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def read_txt(file_path):
    """Read plain text files"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def process_documents(directory):
    """Process all documents in a directory"""
    combined_text = ""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Process different file types
        if filename.lower().endswith('.pdf'):
            combined_text += read_pdf(file_path)
        elif filename.lower().endswith('.docx'):
            combined_text += read_word(file_path)
        elif filename.lower().endswith('.txt'):
            combined_text += read_txt(file_path)
    
    # Clean text
    combined_text = re.sub(r'\n+', '\n', combined_text).strip()
    return combined_text

### 3. Convert to Q&A Format
def create_qa_dataset(text_data):
    """
    Convert raw text to Q&A format.
    This is a simplified approach - you may need to customize based on your specific data.
    """
    # Split text into paragraphs or sections
    paragraphs = text_data.split('\n\n')
    
    qa_pairs = []
    for para in paragraphs:
        if len(para.split()) > 10:  # Ensure meaningful content
            # Generate a sample question (very basic approach)
            question = f"[Q] Tell me about {para.split()[0:3]}"
            answer = f"[A] {para}"
            qa_pairs.append(f"{question}\n{answer}\n")
    
    return "\n".join(qa_pairs)

### 4. Main Execution
def main():
    # Set your agriculture documents directory
    agriculture_docs_dir = 'documents'
    
    # Process documents
    raw_text = process_documents(agriculture_docs_dir)
    
    # Convert to Q&A format
    qa_text = create_qa_dataset(raw_text)
    
    # Save processed data
    with open('agriculture_qa_dataset.txt', 'w', encoding='utf-8') as f:
        f.write(qa_text)

if __name__ == '__main__':
    main()
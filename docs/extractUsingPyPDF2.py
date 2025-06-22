import PyPDF2
import os
from datetime import datetime

def extract_pdf_text(pdf_path):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Initialize a variable to store extracted text
            text = ""
            
            # Iterate through all pages
            for page in pdf_reader.pages:
                # Extract text from each page and append it
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            
            return text
    
    except FileNotFoundError:
        return "Error: The specified PDF file was not found."
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    start_time =  datetime.now()
    pdf_file_path = "C:\\test\\IRM.pdf"  # Replace with your PDF file path
    extracted_text = extract_pdf_text(pdf_file_path)
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time}")
    
    # create a text file to save the extracted text
    output_file_path = "C:\\test\\pdf_extracted_text.txt"  # Replace with your desired output path
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(extracted_text)   
    print(f"Text extracted and saved to {output_file_path}")
    
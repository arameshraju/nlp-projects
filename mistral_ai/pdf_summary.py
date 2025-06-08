import fitz  # PyMuPDF
import ollama
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def chunk_text(text, max_chunk_size=2000):
    """Split text into chunks to fit model context window."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_length += len(word) + 1
        if current_length > max_chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word) + 1
        else:
            current_chunk.append(word)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

def summarize_text(text):
    """Summarize text using Mistral model."""
    try:
        # Prepare prompt for summarization
        prompt = f"Summarize the following text in 100-150 words:\n\n{text}"
        response = ollama.chat(
            model="mistral:7b",
            messages=[
                {"role": "system", "content": "You are a helpful assistant skilled at summarizing text concisely."},
                {"role": "user", "content": prompt}
            ],
            options={"temperature": 0.3}  # Lower temperature for focused output
        )
        return response['message']['content']
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return None

def main():
    # Get PDF file path
    pdf_path = input("Enter the path to your PDF file: ")
    if not os.path.exists(pdf_path):
        print("PDF file not found!")
        return

    # Extract text
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)
    if not text:
        return

    # Chunk text if too large
    chunks = chunk_text(text)
    if not chunks:
        print("No text extracted from PDF.")
        return

    # Summarize each chunk and combine
    print("Generating summary...")
    summaries = []
    for i, chunk in enumerate(chunks, 1):
        print(f"Processing chunk {i}/{len(chunks)}...")
        summary = summarize_text(chunk)
        if summary:
            summaries.append(summary)

    # Combine summaries
    if summaries:
        final_summary = " ".join(summaries)
        print("\n=== Summary ===")
        print(final_summary)
    else:
        print("Failed to generate summary.")

if __name__ == "__main__":
    main()
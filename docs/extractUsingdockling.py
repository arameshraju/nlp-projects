from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from datetime import datetime
pipeline_options = PdfPipelineOptions()
pipeline_options.do_code_enrichment = True

converter = DocumentConverter(format_options={
    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
})



start_time =  datetime.now()
pdf_file_path = "C:\\test\\IRM.pdf"  # Replace with your PDF file path


converter = DocumentConverter()
result = converter.convert(pdf_file_path)
end_time = datetime.now()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time}")
result.document.export_to_text("C:\\test\\docling_extracted_text2.txt" )  # output: "## Docling Technical Report[...]"
   

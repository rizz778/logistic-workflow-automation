from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages

# class ChatState(TypedDict):
#     """Existing chat state definition for general chat routing."""
#     messages: Annotated[list, add_messages]

class PipelineState(TypedDict, total=False):
    """Unified state for the multi-agent trade document validation pipeline."""
<<<<<<< Updated upstream
    filename: str                         # Legacy/single filename
    file_path: str                        # Legacy/single local file path
    filenames: list[str]                  # List of names (e.g. ["bol.pdf", "invoice.jpg"])
    file_paths: list[str]                 # Local file paths on the server
    raw_text: str
    extracted_data: dict                  # Map of filename -> extracted JSON dictionary
    validation_results: dict              # Map of filename -> validation results dictionary
    cross_doc_results: dict               # Cross-document consistency discrepancies
    decision: str
    decision_reason: str
    amendment_draft: str | None
    logs: list[str]
    source: str                           # 'inbox' | 'manual_upload'
    email_sender: str
    email_subject: str
    email_body: str
    received_at: str                      # Timestamp when email arrived
=======
    filename: str
    file_path: str #helps in retrieving file from upload directory
    raw_text: str #raw text extracted from vision agent through  gemini model
    extracted_data: dict #extracted data stored in dict format with field value and confidence score
    validation_results: dict #stores validation resutls with keys and pass or not
    decision: str #stores decision with keys and values (auto approve, flag for review or draft for amendment)
    decision_reason: str #stores decision reason summarized by mistral
    amendment_draft: str | None #stores amendment draft for supplier in case of amendment draft required
    logs: list[str]
>>>>>>> Stashed changes

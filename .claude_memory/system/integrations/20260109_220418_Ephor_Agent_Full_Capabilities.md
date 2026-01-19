# Ephor Agent Full Capabilities

ephor-agent has full delegation via query-delegate API:

RESEARCH: web_search, search_on_x (Twitter), extract_url_data, search_on_library
CODE EXECUTION: code_execution (Python), bash_code_execution, text_editor_code_execution
FILE PROCESSING: CSV, JSON, XML, DOCX, XLSX, PDF, images, archives
DOCUMENT CREATION: Excel (.xlsx), PowerPoint (.pptx), Word (.docx), PDF
APIS: call_external_api for HTTP requests
MEMORY: Persistent storage across conversations
MCP: Can connect to local MCP servers
IMAGE: image_tool for generation and analysis

Commands:
- /Users/bsydes/.local/bin/ephor "query" → Text-only Opus 4.5 (fast reasoning)
- /Users/bsydes/.local/bin/ephor-agent "query" → Full agent with all tools

Use ephor for thinking, ephor-agent for doing.
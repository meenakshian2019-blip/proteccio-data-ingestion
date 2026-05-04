# Proteccio Discover - Week 1

## About the Project

This project is my implementation of the Data Ingestion & Source Integration Layer.
The objective was to build a backend module that can receive data from different sources, validate it, store it securely, and prepare it for further processing such as classification or analysis.
The project focuses mainly on backend functionality, modular code structure, and reliability.



## Features Implemented

### File Upload System
- Supports file upload through API
- Accepted formats: CSV, XLSX, PDF, PST, OST
- Unique file ID generated for every upload
- File size validation up to 500 MB
- Uploaded files stored in local `uploads/` folder

### Metadata Extraction
For every uploaded file, the system returns:
- File size
- Created time
- Modified time
- Unique file identifier

### Database Connector
- SQLite database connector implemented
- Database initialization endpoint added
- Table/schema listing supported

### Cloud Integration
- AWS S3 connector structure added
- Bucket listing supported using credentials from environment variables

### Data Normalization
Standardizes inconsistent field names from multiple sources.

Example:

- EmailAddress → email  
- user_email → email  
- PhoneNumber → phone

### Scheduling & Logging
- Background scheduler added for periodic ingestion jobs
- Logging enabled for monitoring and debugging



## Tech Stack Used

- Python
- Flask
- SQLite
- APScheduler
- Boto3
- Pandas



## Project Structure

proteccio_day1/
|-- app.py
|-- connectors/
|-- modules/
|-- uploads/
|-- logs/
|-- requirements.txt
|-- README.md


## API Usage Examples

### Upload File

POST /upload

Body (form-data):
key: file → upload any file

### API Ingestion

POST /api/ingest

Body (JSON):

{
  "url": "https://jsonplaceholder.typicode.com/users",
  "method": "GET"
}

### Normalize Data

POST /normalize/test

Body (JSON):

{
  "EmailAddress": "abc@gmail.com",
  "PhoneNumber": "9999999999"
}

### View History

GET /history



## Architecture Overview

The system follows a modular data ingestion pipeline:

Data Source → Connector → Extraction → Normalization → Metadata → Storage → Logging/History

Sources supported:
- Files (Upload API)
- Databases (SQLite + extensible connectors)
- Cloud (AWS S3)
- External APIs

Each module is designed independently for scalability and easy extension.


## Assumptions

- SQLite is used for demonstration purposes.
- MySQL, PostgreSQL, and MongoDB connectors are structured but not fully deployed.
- AWS credentials must be provided via environment variables.
- Large file handling is demonstrated with validation and modular design.
- Encryption is applied to sensitive identifiers, not full file content.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
python app.py
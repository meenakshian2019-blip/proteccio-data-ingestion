# Proteccio Discover - Week 1 & Week 2

## About the Project

This project is my implementation of the Proteccio Discover platform covering both:

- Week 1 → Data Ingestion & Source Integration Layer
- Week 2 → Data Discovery, Classification, Profiling & Risk Intelligence Layer

The system is designed to ingest data from multiple sources, normalize and analyze datasets, detect sensitive information, classify privacy-related data, generate profiling insights, map source relationships, and provide searchable privacy intelligence through APIs.

The project focuses mainly on:
- Backend API development
- Modular architecture
- Privacy intelligence workflows
- Security-focused implementation
- Scalable and reusable design



## Features Implemented

## Week 1 - Ingestion & Source Integration

### File Upload System
- Supports file upload through API
- Accepted formats:
  - CSV
  - XLSX
  - PDF
  - PST
  - OST
- Unique file ID generated for every upload
- File size validation up to 500 MB
- Uploaded files stored in local `uploads/` folder

### Metadata Extraction
For every uploaded file, the system extracts:
- File size
- Created time
- Modified time
- Unique file identifier
- Source name
- Source type
- Owner information

### Database Connector
- SQLite database connector implemented
- Database initialization endpoint added
- Table/schema listing supported
- Database timeout handling implemented

### Cloud Integration
- AWS S3 connector structure added
- Bucket listing supported using environment variables

### Data Normalization
Standardizes inconsistent field names from multiple sources.

Example:

- EmailAddress → email
- user_email → email
- PhoneNumber → phone

### Scheduling & Logging
- Background scheduler added
- Logging enabled for monitoring and debugging
- Audit trail support implemented



## Week 2 - Privacy Intelligence Layer

### Data Discovery Engine
The discovery engine scans structured and semi-structured data to identify sensitive information.

#### Supported Detection Types
- Email addresses
- Phone numbers
- Aadhaar numbers
- PAN numbers
- Passport numbers
- IP addresses
- Credit card numbers
- Bank account numbers

#### Detection Methods
- Regex matching
- Pattern matching
- Rule-based validation

#### Features
- Supports multiple detections per record
- Preserves source traceability
- Optimized regex execution
- Sensitive value masking



### Data Classification Engine

Classifies detected data into privacy categories.

#### Supported Classification Categories
- Personal Data
- Sensitive Personal Data
- Financial Data
- Public Data

#### Features
- Confidence score generation
- Multi-label classification support
- Classification consistency across datasets



### Data Mapping Engine

Maps discovered sensitive data back to source systems.

#### Features
- Source-to-record mapping
- Dataset lineage generation
- Source traceability
- Relationship mapping between systems



### Data Profiling Engine

Generates profiling intelligence for datasets.

#### Profiling Features
- Total records
- Total columns
- Null values
- Duplicate records
- Unique records
- Sensitive data density
- Classification distribution
- Risk distribution



### Risk Scoring Engine

Calculates sensitivity and risk level based on detected data combinations.

#### Risk Levels
- Low
- Medium
- High
- Critical

#### Scoring Factors
- Type of detected data
- Number of sensitive attributes
- Classification severity
- Combination-based sensitivity



### Search & Filter APIs

Implemented APIs for:
- Search by risk level
- Search by classification
- Search by source
- Search by detection type

#### Additional Features
- Pagination support
- Source-based filtering
- Searchable analysis history



### Dashboard Backend APIs

Implemented backend APIs for:
- Total scanned records
- Sensitive record count
- Classification distribution
- Risk distribution
- High-risk source count
- Profiling statistics



## Security Features

The project includes multiple security-focused implementations:

- Environment variable based configuration
- No hardcoded credentials
- API authentication using API keys
- Sensitive value masking
- Secure audit logging
- Input validation and sanitization
- Secure file handling
- Encrypted sensitive identifier storage
- Database timeout handling
- HTTPS-ready deployment support



## Tech Stack Used

- Python
- Flask
- SQLite
- Pandas
- APScheduler
- Boto3
- Python-dotenv



## Project Structure


proteccio_day1/
│
|-- app.py
|-- requirements.txt
|-- README.md
|-- .env
|-- connectors/
|-- modules/
│   |-- discovery.py
│   |-- classifier.py
│   |-- profiler.py
│   |-- mapper.py
│   |-- risk_scoring.py
│   |-- dashboard.py
│   |-- search.py
│   |-- audit.py
│
|-- uploads/
|-- logs/
|-- database/

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

### Analyze

POST /analyze
Headers:
x-api-key: proteccio123

### SearchByRisk
GET /search/risk?level=Critical&page=1&per_page=5

### SearchbyClassification
GET /search/classification?type=Sensitive Personal Data

### SearchbySource
GET /search/source?name=Customer CSV

### SearchbyDetectionType
GET /search/source?name=Customer CSV

### DashboardMetrics
GET /dashboard/metrics


## Architecture Overview

The system follows a modular data ingestion pipeline:

Data Source -> Ingestion Layer -> Normalization Engine -> Discovery Engine -> Classification Engine -> Mapping Engine -> Profiling Engine -> Risk Analysis -> Dashboard & Search APIs

Sources supported:
- Files (Upload API)
- Databases (SQLite + extensible connectors)
- Cloud (AWS S3)
- External APIs
- JSON datsets


## Assumptions

- SQLite is used for demonstration purposes.
- Flask is used for backend API implementation.
- AWS credentials must be configured through environment variables.
- The project is designed as a backend-focused implementation.
- Local storage is used for uploaded files.
- Authentication is implemented using API keys for simplicity.
- Render deployment is used for HTTPS support and hosting

## Deployment

The application is deployed using Render cloud hosting platform.

Live Deployment Link:



## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
python app.py

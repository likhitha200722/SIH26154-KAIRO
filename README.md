# KAIRO — Gen AI Platform for Automated Content Transformation

## About the Project

KAIRO is a Generative AI platform developed for Smart India Hackathon Problem Statement SIH26154.

The platform transforms a single source document into tailored communication outputs based on user-selected requirements such as audience, tone, language, detail level, objective, and output type.

The system focuses on:

* Fact preservation
* Source-grounded content generation
* Audience-specific transformation
* Content verification
* Multi-format output generation

## Problem Statement

Organizations often need to convert the same source information into different communication formats for different audiences.

Doing this manually is time-consuming and may lead to:

* Repeated work
* Inconsistent communication
* Loss of important facts
* Difficulty maintaining source consistency

KAIRO addresses this problem by providing a configurable AI-powered transformation pipeline.

## Proposed Solution

The platform follows a source-to-output workflow:

**Source Document → Understand → Configure → Transform → Verify → Export**

Users provide a source document and configure the desired transformation parameters.

The generated content is then checked against the source before being prepared for output.

## Key Features

* Single source to multiple communication formats
* Configurable audience and tone
* Language selection
* Adjustable detail level
* User-defined communication objective
* Generative AI based transformation
* Source-aware content verification
* Exportable generated outputs
* Modular backend architecture

## Transformation Parameters

Users can configure:

| Parameter    | Available Options                                           |
| ------------ | ----------------------------------------------------------- |
| Audience     | General Public, Students, Professionals, Technical Audience |
| Tone         | Clear and Professional, Formal, Simple, Educational         |
| Language     | English, Hindi, Telugu                                      |
| Detail Level | Concise, Balanced, Detailed                                 |
| Objective    | Inform, Educate, Summarize, Present                         |
| Output Type  | Advisory, Report, Presentation, Summary                     |

## System Architecture

The platform is divided into the following major components:

### Frontend

Built using Next.js and provides the user interface for:

* Uploading source documents
* Selecting transformation parameters
* Viewing generated results
* Interacting with the transformation workflow

### Backend / API Layer

Built using FastAPI and acts as the central controller.

It manages:

* Document uploads
* Document processing
* Transformation requests
* Communication between system modules
* Export requests

### Generative AI Engine

The AI engine uses Google Gemini to transform source content according to the selected parameters.

It receives:

* Source content
* Audience
* Tone
* Language
* Detail level
* Objective
* Output type

It returns the generated content to the backend.

### Verification Module

The verification module analyzes the source and generated content to identify inconsistencies and content drift.

It extracts and compares information such as:

* Topics
* Key facts
* Dates
* Locations
* Entities
* Generated claims

### Output & Export Module

The export module prepares generated content for supported document formats such as:

* PDF
* DOCX
* PPTX
* TXT

## Technology Stack

### Frontend

* Next.js
* React
* JavaScript
* Tailwind CSS

### Backend

* Python
* FastAPI
* Uvicorn
* SQLite
* Pydantic

### AI

* Google Gemini API
* Prompt Engineering

### Document Processing & Verification

* Python
* Text processing
* Fact and claim extraction
* Similarity and comparison logic

### Export

* Python document-generation libraries

## Workflow

* User uploads a source document.
* The backend stores and processes the document.
* The user selects transformation parameters.
* The backend sends the source and parameters to the AI engine.
* Gemini generates the requested content.
* The verification module compares the generated content with the source.
* The processed result is returned to the frontend.
* The output can be prepared for export.

## Project Structure

```text
SIH26154-KAIRO/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   └── ...
│
├── README.md
└── ...
```

## Running the Project

### Backend

Open a terminal and navigate to the backend folder:

```bash
cd backend
```

Activate the existing Python virtual environment if required.

Then start the FastAPI server:

```bash
uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### Frontend

Open a second terminal and navigate to the frontend folder:

```bash
cd frontend
```

Install the required dependencies:

```bash
npm install
```

Start the Next.js development server:

```bash
npm run dev
```

The frontend will run at:

```text
http://localhost:3000
```

The frontend communicates with the FastAPI backend through REST API endpoints.

## API Workflow

The backend provides API endpoints for the major stages of the transformation pipeline.

Typical workflow:

```text
Upload Document
      ↓
Analyze Document
      ↓
Configure Transformation
      ↓
Generate Content using Gemini
      ↓
Verify Generated Content
      ↓
Prepare Output
      ↓
Export
```

The FastAPI Swagger interface can be used to test and inspect the available endpoints.

## Security

* API keys and other secrets must not be committed to the repository.
* Gemini API credentials should remain on the backend.
* Environment variables should be used for sensitive configuration.
* Do not expose private credentials in frontend code.

## Current Project Status

The core project architecture and major modules have been developed for the SIH26154 solution.

### Implemented / Developed

* Next.js frontend workflow
* FastAPI backend
* Document upload and processing
* Document analysis
* Configurable transformation parameters
* Gemini-based content transformation
* Source-content verification logic
* Output generation and export functionality
* REST API communication between frontend and backend

### Ongoing Improvements

* Advanced claim matching and verification
* Improved frontend result visualization
* Further output-format integration
* UI refinement and usability improvements
* Deployment and production configuration

## Team KAIRO

KAIRO is a five-member team working on SIH26154.

### Team Roles

| Member Role              | Responsibility                                |
| ------------------------ | --------------------------------------------- |
| Frontend Developer       | User interface and transformation workflow    |
| Backend / API Developer  | FastAPI backend, APIs and document processing |
| AI / GenAI Engineer      | Gemini integration and content transformation |
| Verification Engineer    | Source analysis and content verification      |
| Output / Export Engineer | Generated output and document export          |

## Problem Statement Details

**Problem Statement ID:** SIH26154

**Title:** Gen AI Platform for Automated Content Transformation

**Organization:** National Technical Research Organisation (NTRO)

**Category:** Software

**Theme:** Smart Automation

**Team Name:** KAIRO

## Future Improvements

Planned improvements include:

* More advanced document understanding
* Improved factual consistency checking
* Better claim-level traceability
* More robust content-drift detection
* Additional languages
* More output formats
* Improved visualization of verification results
* Cloud deployment
* Production-ready authentication and security
* Scalable API architecture

## Conclusion

KAIRO provides a configurable Generative AI pipeline for transforming a single source document into audience-specific communication outputs while maintaining source grounding and verification.

The project combines document processing, Generative AI, verification, and output generation into a modular workflow designed for automated content transformation.

## License

This project is developed for Smart India Hackathon 2026 under Problem Statement SIH26154.


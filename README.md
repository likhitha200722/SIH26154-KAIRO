# KAIRO – Gen AI Platform for Automated Content Transformation

## Smart India Hackathon 2026

**Problem Statement ID:** SIH26154  
**Problem Statement:** Gen AI Platform for Automated Content Transformation  
**Theme:** Smart Automation  
**Category:** Software  
**Team Name:** KAIRO  

---

## 1. Problem Statement

Organisations receive information in different forms such as reports, articles, advisories, research papers, announcements and other source content.

Manually analysing this information and converting it into different communication formats is time-consuming and requires significant effort.

There is a need for an intelligent platform that can transform a common source of information into different communication deliverables based on the operator's requirements.

---

## 2. Proposed Solution

KAIRO is an AI-powered content transformation platform that converts a common source document into audience-specific and configurable communication outputs.

The operator provides source content and selects parameters such as:

- Target audience
- Tone
- Language
- Level of detail
- Communication objective
- Output type

The platform processes the source, transforms the content using Generative AI, validates the generated information against the source, and prepares the final output.

---

## 3. Key Features

- Source document ingestion
- Document and text analysis
- Configurable content transformation
- Audience-specific generation
- Tone and language control
- Detail-level control
- Generative AI transformation
- Source-grounded content generation
- Claim and fact validation
- Content drift detection
- Multiple output formats
- Export-ready output packages

---

## 4. System Workflow

Source
→ Understand
→ Configure
→ Transform
→ Ground
→ Validate
→ Structure
→ Output

### Source
Accept source documents and content.

### Understand
Extract text, tables, facts and claims from the source.

### Configure
Apply audience, tone, language and detail-level parameters.

### Transform
Use Generative AI to create the requested content.

### Ground
Maintain connection between generated claims and the original source.

### Validate
Compare generated content with the source and identify inconsistencies.

### Structure
Prepare the validated content as the requested output package.

---

## 5. Technology Stack

### Frontend
- Next.js
- React
- JavaScript
- HTML
- CSS
- Tailwind CSS

### Backend
- Python
- FastAPI
- Uvicorn
- REST API
- SQLite

### Generative AI
- Google Gemini API
- Python
- Prompt Engineering

### Validation
- Python
- Document/Text Processing
- Fact and Claim Matching
- Source Comparison

### Output Generation
- Python
- PDF generation
- DOCX generation
- PPTX generation
- TXT generation

---

## 6. System Architecture

Frontend
→ API Gateway
→ Backend
→ GenAI Transformation
→ Validation
→ Output Generation
→ User

The backend acts as the central orchestration layer between the frontend, AI services, validation module and output generation module.

---

## 7. Main Components

### Frontend
Provides the user interface for uploading source content, selecting transformation parameters and viewing results.

### Backend
Handles API requests, document management, transformation requests and communication between system modules.

### GenAI Engine
Uses Google Gemini to transform source content according to the selected parameters.

### Validator
Checks generated content against the original source and identifies possible inconsistencies or content drift.

### Output Generator
Converts the processed content into usable output formats such as PDF, DOCX, PPTX and TXT.

---

## 8. Configuration Parameters

The platform supports configurable generation parameters including:

- Audience
- Tone
- Language
- Detail Level
- Communication Objective
- Output Type

---

## 9. Installation and Setup

### Backend

Navigate to the backend directory:

```bash
cd backend

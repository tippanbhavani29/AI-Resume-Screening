# AI Resume Screening Platform

## Problem Statement

Recruiters spend significant time manually screening resumes.
This project automates resume evaluation using NLP and machine learning techniques.

## Features

- Resume PDF Parsing
- Skill Extraction
- JD vs Resume Matching
- Candidate Ranking
- Multi Resume Screening
- Analytics Dashboard
- Screening History

## Tech Stack

Backend:
- FastAPI
- Python
- SQLite

Frontend:
- Streamlit

NLP:
- spaCy
- TF-IDF
- Scikit-learn

## Project Architecture

Resume PDF
    ↓
Parser
    ↓
Preprocessing
    ↓
Skill Extraction
    ↓
Similarity Scoring
    ↓
Ranking Engine
    ↓
Database
    ↓
Dashboard

## Future Enhancements

- BERT Embeddings
- Resume Recommendations
- Recruiter Authentication
- Cloud Deployment
# Project Scope

## Project Title

**HireSense AI: NLP-Based Candidate Retrieval and Ranking System**

---

## Scope Overview

HireSense AI is an NLP-powered recruitment platform designed to automate resume screening and candidate ranking. The system analyzes job descriptions and resumes, extracts relevant skills, computes similarity scores, identifies skill gaps, and ranks candidates based on their suitability for a specific role.

The project aims to assist recruiters by reducing manual screening efforts and providing objective, data-driven candidate evaluations.

---

## In Scope

### Resume Processing

* Upload and parse PDF resumes.
* Extract textual information from resumes.
* Preprocess resume content using NLP techniques.

### Job Description Analysis

* Accept job descriptions as text input.
* Extract relevant skills and requirements.

### Candidate Matching

* Compare resumes against job descriptions.
* Calculate candidate-job relevance scores.
* Measure similarity using NLP-based techniques.

### Skill Gap Analysis

* Identify matched skills.
* Detect missing skills required for the role.

### Candidate Ranking

* Rank candidates based on matching scores.
* Generate ordered candidate lists for recruiters.

### Recruiter Dashboard

* Display candidate rankings.
* Visualize match scores and analytics.
* Maintain screening history.

### Data Storage

* Store screening results and candidate rankings using SQLite.

---

## Out of Scope

The following features are not included in the current version:

* Candidate interview scheduling
* Recruiter authentication and authorization
* Email notifications
* Background verification
* Integration with external ATS platforms
* Cloud deployment infrastructure
* Real-time collaboration features

---

## Deliverables

* FastAPI-based backend services
* Streamlit-based recruiter dashboard
* Resume parsing module
* NLP preprocessing pipeline
* Candidate matching and ranking engine
* Skill gap analysis module
* Analytics and reporting dashboard
* SQLite database integration
* Project documentation and source code repository

---

## Expected Outcome

The system will enable recruiters to:

* Upload resumes and job descriptions
* Automatically evaluate candidate suitability
* Identify missing skills and qualification gaps
* Rank candidates based on relevance scores
* Reduce manual screening effort
* Improve hiring efficiency and consistency

The final deliverable is an intelligent candidate retrieval and ranking platform that leverages NLP techniques to support faster and more effective recruitment decisions.

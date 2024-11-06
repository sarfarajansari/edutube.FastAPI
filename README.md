

# Edutube API 🎓📡

This repository hosts the **FastAPI backend** for the <a href="https://github.com/sarfarajansari/edutube">Edutube</a> platform, providing RESTful endpoints to manage subjects, topics, video searches, and concept extraction for a streamlined learning experience. 

## Features

- **Educational Subjects and Topics**: Endpoints to retrieve and manage subjects and related topics.
- **Video Search**: Fetches top YouTube videos for a selected topic.
- **Concept Extraction**: Processes video transcripts to identify and return key concepts.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **FastAPI** and **Uvicorn** for running the server

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/edutube-api.git
   cd edutube-api
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.


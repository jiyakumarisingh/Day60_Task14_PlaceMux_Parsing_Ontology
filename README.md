# PlaceMux — Day 60 / Task 14

## End-to-End Status Tracking & Parsing: Parsed Skills into Ontology

**Phase 2 | Week 4 | AI/ML Trust Layer | Altrodav Technologies Pvt. Ltd.**

---

## 1. Objective

The objective of Task 14 is to feed parsed resume and job-description skills into a canonical skill ontology and demonstrate the complete processing status history.

### Acceptance Criterion

> **Parsed skills feed the ontology.**

The implementation provides a focused, rule-based proof of concept that:

* Extracts recognized skills from plain text.
* Normalizes skill aliases to canonical skills.
* Maps parsed skills to ontology skill IDs.
* Tracks the complete processing status.
* Supports both resumes and job descriptions.
* Exposes the functionality through a FastAPI service.
* Provides automated tests for the core workflow.

This implementation is intentionally focused on the Task 14 requirement. It is **not an LLM parser or a production offer/e-sign workflow**.

---

## 2. What This Project Demonstrates

The complete processing flow is:

```text
Resume / Job Description
          |
          v
      Text Input
          |
          v
     Skill Parser
          |
          v
   Extracted Skill Phrases
          |
          v
 Skill Alias Normalization
          |
          v
    Skill Ontology
          |
          v
 Canonical Skill IDs
          |
          v
   Status Tracking
          |
          v
     API / Demo
```

Example:

```text
Input:
"Built ML projects using Python and SQL"

Parsed skills:
ML
Python
SQL

Ontology mapping:
ML       -> machine-learning
Python   -> python
SQL      -> sql
```

---

## 3. Project Structure

```text
Day60_Task14_PlaceMux_Parsing_Ontology/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── ontology.py
│   └── pipeline.py
│
├── data/
│   └── skills.json
│
├── tests/
│   └── test_pipeline.py
│
├── outputs/
│   └── .gitkeep
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Responsibilities

| File                     | Purpose                                                                |
| ------------------------ | ---------------------------------------------------------------------- |
| `app/main.py`            | FastAPI application and API routes                                     |
| `app/ontology.py`        | Ontology loading, alias resolution and skill extraction                |
| `app/pipeline.py`        | End-to-end document processing and status tracking                     |
| `data/skills.json`       | Canonical skills, aliases, categories and related skills               |
| `tests/test_pipeline.py` | Automated functional and API tests                                     |
| `outputs/.gitkeep`       | Keeps the output directory without storing unnecessary generated files |
| `run.py`                 | End-to-end command-line demonstration                                  |
| `requirements.txt`       | Python dependencies                                                    |
| `.gitignore`             | Files excluded from Git                                                |
| `README.md`              | Project documentation                                                  |

---

## 4. Core Components

### 4.1 Skill Ontology

The ontology is stored in:

```text
data/skills.json
```

Each ontology entry contains information such as:

```json
{
  "id": "machine-learning",
  "name": "Machine Learning",
  "aliases": [
    "machine learning",
    "ml"
  ],
  "category": "ai_ml",
  "related": [
    "python",
    "pandas"
  ]
}
```

The ontology provides:

* Canonical skill IDs.
* Canonical skill names.
* Skill aliases.
* Skill categories.
* Related-skill references.

The sample ontology contains 12 canonical skills.

---

### 4.2 Skill Parsing

`app/ontology.py` performs rule-based skill extraction.

The parser:

1. Reads plain text.
2. Checks known canonical names and aliases.
3. Uses case-insensitive matching.
4. Uses word boundaries to avoid partial matches.
5. Removes duplicate matches.
6. Resolves aliases to canonical ontology IDs.

Example:

```text
ML
Machine Learning
```

Both resolve to:

```text
machine-learning
```

---

### 4.3 End-to-End Pipeline

`app/pipeline.py` handles the complete processing workflow.

The status sequence is:

```text
received
    ->
parsing
    ->
parsed
    ->
ontology_mapping
    ->
completed
```

For every processed document, the pipeline records:

* Job/document ID.
* Document type.
* Current status.
* Parsed skill phrases.
* Canonical ontology IDs.
* Matched ontology skills.
* Status history.

---

## 5. Status Tracking

A successful document follows this status progression:

```text
received
    ->
parsing
    ->
parsed
    ->
ontology_mapping
    ->
completed
```

Example:

```text
Document: candidate-101

Status history:
received
parsing
parsed
ontology_mapping
completed
```

The status history makes the processing flow demonstrable and allows the final ontology integration step to be verified.

---

## 6. Demo

Run:

```powershell
python run.py
```

The demo processes both a resume and a job description.

### Example Resume

```text
Built ML projects with Python, SQL, pandas and FastAPI.
```

Expected mapping:

```text
Parsed skills:
['ML', 'Python', 'SQL', 'pandas', 'FastAPI']

Ontology IDs:
[
    'machine-learning',
    'python',
    'sql',
    'pandas',
    'fastapi'
]
```

Expected status:

```text
received -> parsing -> parsed -> ontology_mapping -> completed
```

### Example Job Description

```text
Looking for experience with machine learning, Python,
AWS and Docker.
```

Expected mapping:

```text
Parsed skills:
[
    'machine learning',
    'Python',
    'AWS',
    'Docker'
]

Ontology IDs:
[
    'machine-learning',
    'python',
    'aws',
    'docker'
]
```

Expected status:

```text
received -> parsing -> parsed -> ontology_mapping -> completed
```

The final demo should report:

```text
DEMO PASS: parsed skills feed the ontology
```

---

## 7. Requirements

Python **3.10 or newer** is required.

Main dependencies:

```text
FastAPI
Uvicorn
Pydantic
Pytest
HTTPX
```

All required dependencies are listed in:

```text
requirements.txt
```

---

## 8. Setup — Windows PowerShell

### Step 1: Open the project directory

```powershell
cd "D:\projects task\Day60_Task14_PlaceMux_Parsing_Ontology"
```

Use your actual project path if it is different.

### Step 2: Create virtual environment

```powershell
py -3.11 -m venv venv
```

### Step 3: Activate virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(venv)
```

### Step 4: Upgrade pip

```powershell
python -m pip install --upgrade pip
```

### Step 5: Install dependencies

```powershell
pip install -r requirements.txt
```

---

## 9. Run the Project

Run the end-to-end demo:

```powershell
python run.py
```

This demonstrates:

* Skill extraction.
* Alias normalization.
* Ontology mapping.
* Status progression.
* Resume processing.
* Job-description processing.

---

## 10. Run Tests

Run:

```powershell
python -m pytest -v
```

The tests cover:

* Canonical skill resolution.
* Alias resolution.
* Case-insensitive matching.
* Word-boundary matching.
* Skill deduplication.
* Resume processing.
* Job-description processing.
* Ontology integration.
* Status progression.
* Input validation.
* API endpoints.

A successful test run should show all tests passing.

---

## 11. Run the API

Start FastAPI:

```powershell
uvicorn app.main:app --reload
```

The service will normally run at:

```text
http://127.0.0.1:8000
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 12. API Endpoints

| Method | Endpoint                     | Purpose                                      |
| ------ | ---------------------------- | -------------------------------------------- |
| GET    | `/health`                    | Health check and ontology size               |
| POST   | `/parse`                     | Parse a resume/JD and map skills to ontology |
| GET    | `/status/{job_id}`           | Retrieve processing status and mapped skills |
| GET    | `/ontology/skills`           | List canonical ontology skills               |
| GET    | `/ontology/resolve/{phrase}` | Resolve a skill alias or canonical phrase    |

---

## 13. API Example — Parse

PowerShell:

```powershell
$body = @{
    text = "Built ML projects with Python and SQL"
    document_type = "resume"
    document_id = "candidate-123"
} | ConvertTo-Json

$result = Invoke-RestMethod `
    -Method Post `
    -Uri "http://127.0.0.1:8000/parse" `
    -ContentType "application/json" `
    -Body $body

$result | ConvertTo-Json -Depth 6
```

The response contains the processing result, including:

* Job/document ID.
* Document type.
* Parsed skills.
* Ontology IDs.
* Status.
* Status history.

---

## 14. API Example — Status

After parsing:

```powershell
Invoke-RestMethod `
    "http://127.0.0.1:8000/status/$($result.job_id)" |
    ConvertTo-Json -Depth 6
```

This returns the stored status history and ontology mapping for that document.

---

## 15. API Example — Ontology Resolution

Resolve an alias:

```powershell
Invoke-RestMethod `
    "http://127.0.0.1:8000/ontology/resolve/ML"
```

Expected result:

```text
ML -> machine-learning
```

Another example:

```powershell
Invoke-RestMethod `
    "http://127.0.0.1:8000/ontology/resolve/Python"
```

Expected result:

```text
Python -> python
```

---

## 16. Adding New Skills

The ontology can be extended by editing:

```text
data/skills.json
```

For example:

```json
{
  "id": "new-skill",
  "name": "New Skill",
  "aliases": [
    "new skill",
    "new-skill"
  ],
  "category": "example",
  "related": []
}
```

When adding a skill:

* Keep the skill ID unique.
* Keep aliases unambiguous.
* Use valid JSON.
* Keep `related` references valid.
* Restart the API after changing the ontology.

The ontology validates these constraints during startup.

---

## 17. Data Flow

The complete data flow is:

```text
Input Document
      |
      v
Document Validation
      |
      v
Status: received
      |
      v
Skill Parsing
      |
      v
Status: parsing
      |
      v
Recognized Skill Phrases
      |
      v
Status: parsed
      |
      v
Alias / Canonical Resolution
      |
      v
Status: ontology_mapping
      |
      v
Canonical Ontology IDs
      |
      v
Status: completed
```

This directly demonstrates the Task 14 acceptance criterion.

---

## 18. Example End-to-End Result

Input:

```text
Built machine learning applications using Python,
SQL, pandas and FastAPI.
```

Parser output:

```text
[
    "machine learning",
    "Python",
    "SQL",
    "pandas",
    "FastAPI"
]
```

Ontology output:

```text
[
    "machine-learning",
    "python",
    "sql",
    "pandas",
    "fastapi"
]
```

Status history:

```text
received
parsing
parsed
ontology_mapping
completed
```

Therefore:

```text
Parsed Skills
      |
      v
Ontology Mapping
      |
      v
Canonical Skill IDs
```

---

## 19. Testing Strategy

The test suite verifies the most important Task 14 behavior.

### Ontology Tests

Verify:

* Canonical names resolve correctly.
* Aliases resolve correctly.
* Matching is case-insensitive.
* Partial words are not incorrectly matched.
* Duplicate aliases produce one canonical skill.

### Pipeline Tests

Verify:

* Resume documents are processed.
* Job descriptions are processed.
* Parsed skills reach the ontology.
* Status history is complete and ordered.
* Invalid input is rejected.

### API Tests

Verify:

* `/health` works.
* `/parse` accepts valid requests.
* `/status/{job_id}` returns processing information.
* `/ontology/skills` returns ontology data.
* `/ontology/resolve/{phrase}` resolves known skills.

---

## 20. Scope

This implementation is intentionally limited to the requirements of Task 14.

### Included

* Plain-text resume parsing.
* Plain-text job-description parsing.
* Rule-based skill extraction.
* Alias normalization.
* Canonical ontology mapping.
* Status tracking.
* FastAPI service.
* Automated testing.
* CLI demonstration.

### Not Included

* LLM-based parsing.
* PDF parsing.
* DOCX parsing.
* OCR.
* Database persistence.
* Distributed status tracking.
* Authentication.
* Production deployment.
* Offer/e-sign workflow.

These features are outside the focused acceptance criterion of this task.

---

## 21. Limitations

* The parser accepts plain text only.
* PDF/DOCX ingestion and OCR are not implemented.
* Skill discovery is limited to skills defined in the ontology.
* Unknown skills are not automatically learned or added.
* The ontology contains an illustrative 12-skill seed dataset.
* Status records are stored in memory and reset when the application restarts.
* The implementation is intended as a single-process proof of concept.
* No production accuracy or recall claims are made.
* The project does not contain real resumes or personally identifiable information.

For a production implementation, persistent storage, authentication, approved PlaceMux ontology data, scalable processing, and a more advanced parsing layer would be required.

---

## 22. Security and Data Considerations

This project uses synthetic/sample text only.

No real resumes, personal information, credentials, API keys, or production data are included.

The API is intended for local demonstration and should not be exposed directly to the public internet without appropriate:

* Authentication.
* Authorization.
* Input controls.
* Rate limiting.
* Persistent storage security.
* Logging and monitoring.

---

## 23. Reproducibility

The project is designed so that the demonstration can be reproduced from a clean environment.

Use:

```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
python -m pytest -v
```

The ontology is loaded from:

```text
data/skills.json
```

Therefore, ontology changes can be reproduced by version-controlling the JSON file together with the application code.

---

## 24. GitHub Upload

Do not upload the virtual environment or generated Python cache files.

The repository should contain:

```text
app/
data/
tests/
outputs/
run.py
requirements.txt
README.md
.gitignore
```

The following should remain excluded:

```text
venv/
__pycache__/
.pytest_cache/
*.pyc
.env
```

Recommended repository name:

```text
Day60_Task14_PlaceMux_Parsing_Ontology
```

---

## 25. Acceptance Criterion

The Task 14 requirement is:

> **Parsed skills feed the ontology.**

This implementation demonstrates that requirement through the following sequence:

```text
Resume / JD
    |
    v
Parsed Skills
    |
    v
Alias Normalization
    |
    v
Canonical Ontology IDs
    |
    v
Completed Status
```

Example:

```text
ML
  ->
machine-learning
```

```text
Python
  ->
python
```

```text
SQL
  ->
sql
```

The mapped ontology IDs are returned by the processing pipeline and API.

---

## 26. Conclusion

This Day 60 / Task 14 implementation successfully demonstrates the complete required flow from parsed skills to a canonical ontology.

The project provides:

* Rule-based skill extraction.
* Alias and canonical skill normalization.
* Boundary-aware matching.
* Canonical ontology IDs.
* Resume and job-description processing.
* End-to-end status tracking.
* FastAPI endpoints.
* Automated tests.
* A reproducible CLI demonstration.

The implementation remains intentionally focused on the Task 14 acceptance criterion without adding unnecessary production infrastructure.

### Final Result

```text
Parsed Skills
      |
      v
Normalized Skills
      |
      v
Ontology Mapping
      |
      v
Canonical Skill IDs
      |
      v
Status: completed
```

**Task 14 Status: COMPLETED**

**Acceptance Criterion: PASS — Parsed skills successfully feed the ontology.**

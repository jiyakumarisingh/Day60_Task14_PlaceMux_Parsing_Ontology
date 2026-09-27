from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .pipeline import ParsingPipeline

app = FastAPI(title='PlaceMux - Day 60 Skill Parsing & Ontology', version='1.0.0')
pipeline = ParsingPipeline()


class ParseRequest(BaseModel):
    text: str = Field(min_length=1, max_length=100000)
    document_type: str
    document_id: str | None = None


@app.get('/health')
def health():
    return {'status': 'ok', 'ontology_skills': len(pipeline.ontology.skills)}


@app.post('/parse')
def parse_document(request: ParseRequest):
    try:
        return pipeline.process(request.text, request.document_type, request.document_id)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.get('/status/{job_id}')
def status(job_id: str):
    result = pipeline.get_status(job_id)
    if result is None:
        raise HTTPException(status_code=404, detail='Job not found')
    return result


@app.get('/ontology/skills')
def list_skills():
    return pipeline.ontology.list_skills()


@app.get('/ontology/resolve/{phrase}')
def resolve_skill(phrase: str):
    result = pipeline.ontology.resolve(phrase)
    if result is None:
        raise HTTPException(status_code=404, detail='Skill not found')
    return result

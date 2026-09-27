import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.ontology import SkillOntology
from app.pipeline import ParsingPipeline


def test_alias_normalization_and_relationships():
    ontology = SkillOntology()
    assert ontology.resolve(' ML ')['id'] == 'machine-learning'
    assert ontology.resolve('machine learning')['id'] == 'machine-learning'
    assert 'deep-learning' in ontology.resolve('ML')['related']


def test_extract_word_boundaries_and_deduplicate():
    result = SkillOntology().extract('ML and machine learning, Python. Not SQLalchemy.')
    assert [x['id'] for x in result] == ['machine-learning', 'python']


def test_end_to_end_resume_and_jd():
    pipeline = ParsingPipeline()
    for kind in ['resume', 'job_description']:
        result = pipeline.process('Python, ML and SQL', kind, 'doc-1')
        assert result['status'] == 'completed'
        assert result['ontology_skill_ids'] == ['python', 'machine-learning', 'sql']
        assert [x['status'] for x in result['history']] == [
            'received', 'parsing', 'parsed', 'ontology_mapping', 'completed']
        assert pipeline.get_status(result['job_id']) is result


def test_empty_and_invalid_document():
    pipeline = ParsingPipeline()
    with pytest.raises(ValueError):
        pipeline.process('  ', 'resume')
    with pytest.raises(ValueError):
        pipeline.process('Python', 'invalid')


def test_api_endpoints():
    client = TestClient(app)
    assert client.get('/health').json()['status'] == 'ok'
    result = client.post('/parse', json={'text': 'Experience in ML and Python',
                                          'document_type': 'resume'}).json()
    assert result['ontology_skill_ids'] == ['machine-learning', 'python']
    assert client.get('/status/' + result['job_id']).json()['status'] == 'completed'
    assert client.get('/ontology/resolve/ML').json()['id'] == 'machine-learning'
    assert len(client.get('/ontology/skills').json()) >= 1
    assert client.get('/status/unknown').status_code == 404
    assert client.post('/parse', json={'text': 'Python', 'document_type': 'other'}).status_code == 422

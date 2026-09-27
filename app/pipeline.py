from datetime import datetime, timezone
from uuid import uuid4

from .ontology import SkillOntology


def utc_now():
    return datetime.now(timezone.utc).isoformat()


class ParsingPipeline:
    """In-memory demo pipeline: records are lost when the process stops."""

    def __init__(self, ontology=None):
        self.ontology = ontology or SkillOntology()
        self.jobs = {}

    def process(self, text: str, document_type: str, document_id: str | None = None):
        if not text.strip():
            raise ValueError('Document text cannot be empty')
        if document_type not in ('resume', 'job_description'):
            raise ValueError('document_type must be resume or job_description')
        job_id = str(uuid4())
        record = {'job_id': job_id, 'document_id': document_id or job_id,
                  'document_type': document_type, 'status': 'received',
                  'history': [{'status': 'received', 'at': utc_now()}],
                  'parsed_skills': [], 'ontology_skill_ids': [], 'unmapped_skills': []}
        self.jobs[job_id] = record
        try:
            self._transition(record, 'parsing')
            extracted = self.ontology.extract(text)
            record['parsed_skills'] = extracted
            self._transition(record, 'parsed')
            self._transition(record, 'ontology_mapping')
            record['ontology_skill_ids'] = [skill['id'] for skill in extracted]
            self._transition(record, 'completed')
        except Exception as exc:
            record['error'] = str(exc)
            self._transition(record, 'failed')
        return record

    @staticmethod
    def _transition(record, status):
        record['status'] = status
        record['history'].append({'status': status, 'at': utc_now()})

    def get_status(self, job_id: str):
        return self.jobs.get(job_id)

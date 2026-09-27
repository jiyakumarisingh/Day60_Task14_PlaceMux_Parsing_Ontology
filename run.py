from app.pipeline import ParsingPipeline


def main():
    pipeline = ParsingPipeline()
    examples = [
        ('resume', 'candidate-101', 'Built ML pipelines with Python, SQL, pandas and FastAPI.'),
        ('job_description', 'job-201', 'Hiring for machine learning, Python, AWS and Docker.'),
    ]
    for kind, doc_id, text in examples:
        result = pipeline.process(text, kind, doc_id)
        print(f'\n{kind}: {doc_id} | status: {result["status"]}')
        print('Parsed skills:', [s['matched_text'] for s in result['parsed_skills']])
        print('Ontology IDs:', result['ontology_skill_ids'])
        print('Status history:', ' -> '.join(s['status'] for s in result['history']))
    print('\nDEMO PASS: parsed skills feed the ontology' if all(
        x['ontology_skill_ids'] for x in pipeline.jobs.values()) else '\nDEMO FAILED')


if __name__ == '__main__':
    main()

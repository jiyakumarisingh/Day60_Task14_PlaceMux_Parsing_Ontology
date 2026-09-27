import json
import re
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parents[1] / 'data' / 'skills.json'


def normalize(text: str) -> str:
    return re.sub(r'\s+', ' ', text.casefold().strip())


class SkillOntology:
    def __init__(self, path=DEFAULT_PATH):
        records = json.loads(Path(path).read_text(encoding='utf-8'))['skills']
        self.skills = {}
        self.aliases = {}
        for record in records:
            sid = record['id']
            if sid in self.skills:
                raise ValueError(f'Duplicate skill ID: {sid}')
            self.skills[sid] = record
            for alias in [record['name'], *record.get('aliases', [])]:
                key = normalize(alias)
                if key in self.aliases and self.aliases[key] != sid:
                    raise ValueError(f'Conflicting alias: {alias}')
                self.aliases[key] = sid
        for record in records:
            for related in record.get('related', []):
                if related not in self.skills:
                    raise ValueError(f'Unknown related skill: {related}')
        # Longer aliases first to avoid partial phrase matches.
        self.patterns = [(re.compile(r'(?<!\w)' + re.escape(alias) + r'(?!\w)', re.I), sid, alias)
                         for alias, sid in sorted(self.aliases.items(), key=lambda item: -len(item[0]))]

    def resolve(self, phrase: str):
        sid = self.aliases.get(normalize(phrase))
        return self.skills.get(sid) if sid else None

    def extract(self, text: str):
        matches = {}
        for pattern, sid, alias in self.patterns:
            for match in pattern.finditer(text):
                existing = matches.get(sid)
                if existing is None or match.start() < existing['offset']:
                    matches[sid] = {'id': sid, 'name': self.skills[sid]['name'],
                                    'category': self.skills[sid]['category'],
                                    'matched_text': match.group(), 'offset': match.start()}
        return sorted(matches.values(), key=lambda x: x['offset'])

    def list_skills(self):
        return list(self.skills.values())

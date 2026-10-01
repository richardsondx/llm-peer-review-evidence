"""Validate final matrices and expose differences without claiming either is correct."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIMS = ['agreement', 'error_detection', 'recall', 'score_bias', 'overconfidence', 'limitations']
STATUSES = {'verified', 'not_measured', 'not_reported', 'source_unavailable'}

def validate(model):
    data = json.loads((ROOT / model / 'matrix.json').read_text())
    rows = data['rows']
    assert len(rows) == 27 and {r['candidate_id'] for r in rows} == set(range(1, 28))
    assert data['cutoff'] == '2026-10-01'
    for row in rows:
        assert set(row['dimensions']) == set(DIMS)
        for dim, cell in row['dimensions'].items():
            assert cell['status'] in STATUSES and cell['finding'].strip(), (model, row['candidate_id'], dim)
            if cell['status'] == 'verified':
                assert cell['citations'], (model, row['candidate_id'], dim)
                for citation in cell['citations']:
                    assert citation['url'].startswith('https://') and citation['location'].strip()
    return data, {r['candidate_id']: r for r in rows}

def main():
    luna, lrows = validate('luna')
    sol, srows = validate('sol')
    disagreements = []
    for cid in range(1, 28):
        for dim in DIMS:
            left, right = lrows[cid]['dimensions'][dim], srows[cid]['dimensions'][dim]
            if left['status'] != right['status']:
                disagreements.append({'candidate_id': cid, 'dimension': dim, 'luna': left, 'sol': right})
    report = {
        'purpose': 'Structural validation and evidence-status differences; not a model accuracy benchmark.',
        'cutoff': '2026-10-01',
        'models': {name: {'model': d['extraction_model'], 'reasoning': d['reasoning_effort'], 'rows': 27, 'cells': 162,
                          'status_counts': dict(Counter(c['status'] for r in d['rows'] for c in r['dimensions'].values()))}
                   for name, d in [('luna', luna), ('sol', sol)]},
        'status_agreements': 162 - len(disagreements),
        'status_differences': disagreements,
        'note': 'Same status does not establish the same finding or numerical accuracy. Differences may reflect source versions, scope, or interpretation; review citations.'
    }
    (ROOT / 'comparison.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'models': report['models'], 'status_agreements': report['status_agreements'],
                      'status_differences': len(disagreements)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()

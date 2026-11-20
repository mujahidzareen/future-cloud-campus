"""Release integrity check for the imported, unmodified Quran reading files."""
import gzip,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
assets=root/('dist/assets' if (root/'dist/assets').is_dir() else 'docs/assets')/'quran'
index=json.loads((assets/'index.json').read_text())
assert index['version'] and len(index['chapters'])==114
packs={int(p.name.split('-')[1].split('.')[0]):json.loads(gzip.decompress(p.read_bytes())) for p in assets.glob('pack-*.json.gz')}
seen=set();total=0;notes=0
for chapter in index['chapters']:
 number=chapter['number'];rows=packs[chapter['pack']][str(number)]
 assert len(rows)==chapter['count']
 assert [r['aya'] for r in rows]==list(range(1,len(rows)+1))
 for row in rows:
  ref=(row['sura'],row['aya']);assert ref not in seen and ref[0]==number
  assert isinstance(row['arabic_text'],str) and row['arabic_text']
  assert isinstance(row['translation'],str) and row['translation']
  assert isinstance(row['footnotes'],str)
  notes+=bool(row['footnotes']);seen.add(ref);total+=1
assert total==6236
assert sum(len(group) for group in packs.values())==114
assert (assets/'Hafs_20.woff2').read_bytes()[:4]==b'wOF2'
print(f'Quran integrity: 114 surahs, {total} sequential unique ayahs, {notes} footnote-bearing ayahs, Hafs v20 WOFF2 verified.')

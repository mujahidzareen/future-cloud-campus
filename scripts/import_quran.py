"""Refresh the unmodified QuranEnc Urdu translation and matched Hafs v20 font/text.
Run before a release to pick up the publisher's current version. No credentials.
"""
import csv,io,json,sqlite3,tempfile,urllib.request,zipfile,hashlib
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/('dist/assets' if (ROOT/'dist/assets').is_dir() else 'docs/assets')
OUT=ASSETS/'quran';OUT.mkdir(parents=True,exist_ok=True)
def fetch(url):
 with urllib.request.urlopen(url,timeout=90) as r:return r.read()
def get(url):return json.loads(fetch(url))
meta=next(x for x in get('https://quranenc.com/api/v1/translations/list/ur?localization=en')['translations'] if x['key']=='urdu_junagarhi')
fontzip=zipfile.ZipFile(io.BytesIO(fetch('https://quranenc.com/downloads/assets/Hafs_20.zip')))
print('Font package:',fontzip.namelist())
for name in fontzip.namelist():
 if name.endswith('.woff2'):(OUT/'Hafs_20.woff2').write_bytes(fontzip.read(name))
fontcsv=next(n for n in fontzip.namelist() if n.endswith('.csv'))
rows=list(csv.DictReader(io.StringIO(fontzip.read(fontcsv).decode('utf-8-sig'))))
print('Arabic CSV columns:',rows[0].keys(),'count:',len(rows))
archive=zipfile.ZipFile(io.BytesIO(fetch(meta['database_url'])))
print('Translation package:',archive.namelist())
with tempfile.TemporaryDirectory() as tmp:
 name=next(n for n in archive.namelist() if n.endswith(('.sqlite','.db','.sqlite3')))
 p=Path(tmp)/'translation.sqlite';p.write_bytes(archive.read(name));conn=sqlite3.connect(p);conn.row_factory=sqlite3.Row
 tables=conn.execute("select name from sqlite_master where type='table'").fetchall()
 print('Tables:',[x[0] for x in tables])
 for t in tables:
  print(t[0],conn.execute('pragma table_info("'+t[0]+'")').fetchall()[0][:])
  print('Columns:',[r[1] for r in conn.execute('pragma table_info("'+t[0]+'")')])
  print('Row:',dict(conn.execute('select * from "'+t[0]+'" limit 1').fetchone()))
 (OUT/'import-meta.json').write_text(json.dumps(meta,ensure_ascii=False))

 arabic={(int(r['sura']),int(r['aya'])):r['uthmani'] for r in rows}
 translated=[dict(r) for r in conn.execute('select * from translations order by sura,aya')]
 assert len(arabic)==len(translated)==6236
 names=get('https://quranenc.com/api/v1/translations/sowar_names?iso_code=en')
 ur_names=get('https://quranenc.com/api/v1/translations/sowar_names?iso_code=ur')
 chapters=[];data={}
 for sura in range(1,115):
  verses=[dict(r,arabic_text=arabic[(r['sura'],r['aya'])]) for r in translated if r['sura']==sura]
  assert [v['aya'] for v in verses]==list(range(1,len(verses)+1))
  data[str(sura)]=verses
  chapters.append({'number':sura,'name':names[str(sura)],'urdu':ur_names[str(sura)],'count':len(verses),'pack':0 if sura==1 else (sura-1)//10+1})
 import gzip
 for pack in range(0,13):
  group={k:v for k,v in data.items() if (0 if int(k)==1 else (int(k)-1)//10+1)==pack}
  raw=json.dumps(group,ensure_ascii=False,separators=(',',':')).encode()
  (OUT/f'pack-{pack}.json.gz').write_bytes(gzip.compress(raw,mtime=0))
 attribution={'source':'QuranEnc.com','publisher':'Rowwad Translation Center','translator':'Muhammad Ibrahim Junagarhi','version':meta['version'],'translation_key':meta['key'],'description':meta['description'],'source_url':'https://quranenc.com/en/browse/urdu_junagarhi','terms_url':'https://quranenc.com/en/home/api/','font':'KFGQPC Uthmanic Hafs v20, matched to Quran_text.csv','font_source':'https://quranenc.com/downloads/assets/Hafs_20.zip','imported_at':datetime.now(timezone.utc).isoformat(),'chapters':chapters}
 (OUT/'index.json').write_text(json.dumps(attribution,ensure_ascii=False,separators=(',',':')))
 (OUT/'SOURCES.txt').write_text('Arabic: KFGQPC Uthmanic Hafs v20 font and matching Quran_text.csv, supplied by QuranEnc.com.\nUrdu translation: Muhammad Ibrahim Junagarhi; developed under the supervision of the Rowwad Translation Center. QuranEnc.com edition '+meta['version']+'.\n'+meta['description']+'\nTerms: https://quranenc.com/en/home/api/\nContent and footnotes are preserved unchanged. Refresh with scripts/import_quran.py before publishing updates. Report translation observations to the publisher through its source page.\n')
 (OUT/'import-meta.json').unlink(missing_ok=True)
 print('Imported 114 surahs / 6236 ayahs; Urdu version',meta['version'])

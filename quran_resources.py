"""User-supplied public Drive resources, observed 27 November 2026.

Keep original publisher files intact. English editions are featured separately;
the complete collections can also contain Arabic and Urdu original editions.
"""
from html import escape as e

ROOT_FOLDER = 'https://drive.google.com/drive/folders/1YiEhEEAtFyJ09RM_s8QkW3UDzW9B1kyn'
TRANSLATION = 'https://drive.google.com/file/d/1w7PVgNNh-8MQ0fbzCESE3TlTQ2e_CVWC/view'
QAIDA = 'https://drive.google.com/file/d/1CkT6vs_HDwsmtimH1r4Nw5xLj6s2Gme_/view'
MANNERS = 'https://drive.google.com/file/d/1gClJe0w68pyeNAYr1H4G9DwdlUz6bMi5/view'
TAJWEED = 'https://drive.google.com/file/d/1ASbZ4uMEizyv6087dTSXs1qbWoPSS35p/view'
JUZ = 'https://drive.google.com/drive/folders/1-XpfELEh-_qZ7l4BG7GmE_WUH2-8O-4B'

# Separate links preserve every supplied collection, including its nested files.
COLLECTIONS = [
 ('nazra','Quran & Mushaf','Arabic reading copies and the supplied English translation.','1N-7c0uAJzINc_VSL7exPFd-LK4_Av_9u'),
 ('qaida','Qaida books & page images','Noorani, Quranic and Madani Qaida editions, including English editions.','1MWFW3ibX9ZhziIqRUC2LZaJbuv9_d4mC'),
 ('qaida','English Qaida & Tajweed videos','Eight lessons: tanween, standing vowels, madd, leen, sukoon, shaddah, ikhfa and izhar.','1-s9es7ZwCPT35Z-fk9O2ggtCRt-EKS2a'),
 ('qaida','Letters & vowel practice','Letter recognition, vowel-mark activities and pronunciation practice sheets.','1jx1Od-hxFApyj24mbkW3sjQaXow1oPeI'),
 ('studies','Duas, daily adhkar & six Kalimas','Supplication cards and a separate folder of PDF resources.','1KR60I-L0_h6d9FSmfTyV_FGHPUCh_dfN'),
 ('studies','Islamic manners & character','Books on etiquette, good character and introductory Islamic knowledge.','1MxrZW3o_8mx63p7B4zTNWpFONUwJKKxG'),
 ('studies','Hadith for children','Separate collections of short hadith and children’s learning books.','1MOcXHv5I6b5VStE2rd5ZAye5Mu_fv9mv'),
 ('studies','Seerah, Prophets & Companions','Life of the Prophet, stories of the Prophets and stories of the Companions.','1E1sjgk5g8iap7wn8Y0h0m4IbrPRzHQby'),
 ('studies','Wudu, Salah & funeral prayer','Prayer guides, with dedicated Wudu, Salah and Janazah folders.','1Lmxsubfutq17Ecnxb7q531xmjZhBAkej'),
 ('studies','Beliefs & introduction to Islam','Faith, the five pillars, introductory books and learning posters.','1ouF-nWzc04lJW-aP7ZrTRrKfhiwuxE0Q'),
 ('tajweed','Tajweed books & rule charts','English books, activity pages and numbered rule-chart collections.','1Mp_tfqp_oAdb8Nbmn2y5YHPfmAAI9TsB'),
 ('studies','Arabic-language study collection','Original Arabic Qaida, Quran, supplications and Islamic learning books.','1MZw0TEPkk9HuEnafQLzQcoQ9UzoY1fsa'),
 ('qaida','Learning stars & rewards','The supplied STARS image collection for learner encouragement.','174lBSYkB_-VAU-BUB2KTIh1ICb46Etwq'),
 ('tajweed','Makharij pictures & videos','Articulation diagrams and individual letter-pronunciation demonstrations.','1vtBKG43tBRcyCpXMijgKuVgIk-DKnoX-'),
]

def card(title, description, url, kind='RESOURCE', action='Open resource'):
 external = url.startswith('https://')
 target = ' target="_blank" rel="noopener noreferrer"' if external else ''
 notice = '<span class="sr-only"> (opens in a new tab)</span>' if external else ''
 return f'<article class="quran-resource-card"><span class="resource-type">{e(kind)}</span><h3>{e(title)}</h3><p>{e(description)}</p><a class="btn secondary" href="{e(url,quote=True)}"{target}>{e(action)}{notice}<span aria-hidden="true">↗</span></a></article>'

def course_resources(slug):
 items = {
  'quran-translation': [('Quran: English translation','The supplied PDF attributed to Mufti Taqi Usmani. Read the complete original edition in Google Drive.',TRANSLATION,'ENGLISH · PDF','Read English translation')],
  'noorani-qaida': [('Noorani Qaida — English edition','The English edition supplied in your resource folder, with Arabic letter and reading exercises.',QAIDA,'ENGLISH · PDF','Read English Qaida'),('English video lessons','Eight supplied Qaida and Tajweed lessons, including vowel marks, sukoon, madd and shaddah.','https://drive.google.com/drive/folders/1-s9es7ZwCPT35Z-fk9O2ggtCRt-EKS2a','ENGLISH · 8 VIDEOS','Browse English videos')],
  'quran-reading': [('Quran Nazra — Juz 1–30','Thirty separate colour-coded, 16-line Quran PDFs. Choose a Juz in the original collection.',JUZ,'ARABIC · 30 PDFS','Choose a Juz'),('English translation','Read the supplied English translation alongside your Arabic reading.','/quran-translation/#english-translation','ENGLISH · TRANSLATION','Open Translation')],
  'islamic-studies': [('Islamic manners','The supplied Islamic Manners PDF opens to Islamic Etiquette, covering everyday manners and character.',MANNERS,'ENGLISH · PDF','Read Islamic manners')],
  'tajweed': [('Simplified Rules of Tajweed','The supplied English Tajweed PDF, with recitation rules and examples.',TAJWEED,'ENGLISH · PDF','Read English Tajweed')],
 }[slug]
 cards=''.join(card(*x) for x in items)
 return f'<section class="shell section quran-library quran-resources" id="course-resources"><div class="section-head"><span class="eyebrow">YOUR COURSE RESOURCES</span><h2>Keep the right resource close.</h2><p>English learning materials, with Arabic preserved for reading practice. Original files open in Google Drive, where you can read or use the available download control.</p></div><div class="quran-resource-grid">{cards}</div><p class="resource-backlink"><a href="/quran-education/#resource-collections">Browse all 14 supplied collections →</a></p></section>'

def collections():
 groups=[]
 for key,title in [('nazra','Quran Nazra & Translation'),('qaida','Noorani Qaida & reading foundations'),('studies','Islamic Studies'),('tajweed','Tajweed & Makharij')]:
  entries=[x for x in COLLECTIONS if x[0]==key]
  links=''.join(f'<a class="collection-link" href="https://drive.google.com/drive/folders/{e(folder)}" target="_blank" rel="noopener noreferrer"><span><strong>{e(name)}</strong><small>{e(desc)}</small></span><span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>' for _,name,desc,folder in entries)
  groups.append(f'<details class="resource-collection"><summary><span>{title}</span><small>{len(entries)} {"collection" if len(entries)==1 else "collections"}</small></summary><div class="collection-links">{links}</div></details>')
 return f'<section class="shell section quran-library quran-resources" id="resource-collections"><div class="section-head"><span class="eyebrow">THE COMPLETE SUPPLIED LIBRARY</span><h2>One collection. Every learning path.</h2><p>All 14 original folders are linked separately below, including their books, images, videos and nested folders. English editions are highlighted on each course page. These original collections also include Arabic and Urdu editions; their source files and folder names remain unchanged.</p></div><div class="resource-collections">{"".join(groups)}</div><p class="resource-backlink"><a href="{ROOT_FOLDER}" target="_blank" rel="noopener noreferrer">Open the complete source folder ↗</a></p></section>'

def translation_page():
 return f'<section class="shell section quran-library" id="english-translation"><div class="section-head"><span class="eyebrow">ENGLISH TRANSLATION</span><h2>Read with meaning.</h2><p>Explore the meanings of the Quran through the supplied English translation by Mufti Taqi Usmani. Open the complete original PDF, read at your own pace and return to the Arabic reader whenever you need.</p></div><div class="quran-resource-grid">{card("The complete English translation","Quran e Karim — English Translation by Mufti Taqi Usmani. The supplied edition contains 1,035 PDF pages.",TRANSLATION,"ENGLISH · ORIGINAL PDF","Read English translation")}{card("Continue Arabic reading","Open Quran Nazra, choose a surah and ayah, or browse the thirty supplied Juz PDFs.","/quran-reading/#quran-reader","QURAN NAZRA","Open Quran Nazra")}</div><aside class="learning-source"><strong>A simple reading routine</strong><p>Read a short Arabic passage, open the corresponding surah in the English PDF, then note questions to discuss with your teacher. A translation conveys meanings and is distinct from the Arabic Quran.</p><p>Prefer Urdu? The <a href="/quran-reading/#quran-reader">Quran Nazra reader</a> has one optional Urdu translation switch. It is off by default.</p></aside></section>'

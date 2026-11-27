"""Original clay scenes paired with the existing route-specific educational artwork."""
from html import escape
from artwork import ART

SCENE_COPY={
 'academic':'Two learners exploring a notebook and online lesson together',
 'science':'A learner exploring a model atom, laboratory flask and leaf specimen',
 'language':'A learner reading a storybook with an online tutor and alphabet blocks',
 'quran':'A teacher guiding a learner in respectful Quran reading',
 'planning':'An education adviser organising a lesson calendar and notebook',
 'resources':'A learner reading among sculptural books and original study materials',
 'global':'Two learners connecting through a globe and an online lesson',
 'family':'A parent and child reviewing a learning notebook together',
}

def scene_family(route):
 key=route.strip('/')
 if key in ('quran-education','quran-reading','quran-translation','noorani-qaida','tajweed','islamic-studies'):return 'quran'
 if key in ('science','chemistry','biology','physics') or any(x in key for x in ('forces','cells','energy','atoms')):return 'science'
 if key in ('english','languages') or any(x in key for x in ('grammar','writing')):return 'language'
 if key.startswith(('free-notes','journal')):return 'resources'
 if key in ('parents','reviews','progress','about','safeguarding'):return 'family'
 if key in ('countries','uk','usa','canada','uae','saudi-arabia','qatar','oman','other-countries','humanities') or key.startswith('curricula'):return 'global'
 if key in ('pricing','custom-package','contact','how-it-works','book-a-demo','privacy','cookies','terms','refund-cancellation'):return 'planning'
 if key=='tutors':return 'academic'
 return 'academic'

def render_scene(route,extra=''):
 key=route.strip('/');family=scene_family(key);label=ART.get(key,('Online learning',))[0]
 return f'''<figure class="page-illustration campus-page-scene scene-{family} tilt {extra}" data-page-scene><span class="campus-scene-halo" aria-hidden="true"></span><span class="campus-scene-orbit" aria-hidden="true"></span><picture><source media="(max-width:600px)" srcset="/assets/scenes/{family}-clay-v1-480.webp"><img class="campus-scene-main" src="/assets/scenes/{family}-clay-v1.webp" alt="{escape(label,quote=True)}. {SCENE_COPY[family]}. Original 3D clay illustration." width="900" height="900" decoding="async" fetchpriority="high"></picture><img class="campus-scene-topic" src="/assets/pages/{key.replace('/','-')}.svg" alt="" aria-hidden="true" width="160" height="120" decoding="async"><span class="campus-scene-dot" aria-hidden="true"></span></figure>'''

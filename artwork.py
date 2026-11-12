"""Render lightweight, subject-specific vector scenes for public pages."""
from pathlib import Path

def book():
    return """<g transform="rotate(-9 200 150)">
    <rect x="105" y="80" width="190" height="157" rx="15" fill="url(#blue)" filter="url(#shadow)"/>
    <path d="M120 210h167v20H124q-18-10-4-20" fill="#fff7e9"/>
    <path d="M123 75h155q17 0 17 17v121H123q-19 0-19 17V95q0-20 19-20" fill="url(#blue)"/>
    <path d="M132 87v112" stroke="#b7cbff" stroke-width="3" opacity=".6"/>
    <rect x="159" y="106" width="93" height="60" rx="9" fill="#ecf1ff" opacity=".9"/>
    <path d="M178 127h55m-55 12h43m-43 12h50" stroke="#6a7dc2" stroke-width="3" stroke-linecap="round"/>
    <path d="M240 212v34l-10-7-10 7v-34" fill="#9ee6cf"/>
    </g>"""

def open_book():
    return """<g filter="url(#shadow)" transform="rotate(-7 200 160)">
    <path d="M75 120q66-8 125 26 59-34 125-26l-14 112q-59-6-111 19-52-25-111-19z" fill="#236452"/>
    <path d="M82 110q63-6 118 25 55-31 118-25l-13 112q-55-5-105 20-50-25-105-20z" fill="url(#paper)"/>
    <path d="M200 137v102" stroke="#bc9f64" stroke-width="3"/>
    <path d="M109 135q42 1 73 17m-70 1q39 0 70 16m-67 2q38 1 67 16m-64 1q36 2 64 16m109-69q-42 1-73 17m70 1q-39 0-70 16m67 2q-38 1-67 16m64 1q-36 2-64 16" fill="none" stroke="#b89a62" stroke-width="3" stroke-linecap="round"/>
    <path d="M210 226v37l10-8 9 9-1-41" fill="#53ad8b"/>
    </g>"""

def laptop():
    return """<g transform="rotate(-5 200 160)" filter="url(#shadow)">
    <rect x="83" y="63" width="230" height="157" rx="18" fill="url(#blue)"/>
    <rect x="95" y="75" width="206" height="129" rx="10" fill="#edf3ff"/>
    <path d="M68 220h257l24 23q4 6-7 10H55q-11-4-7-10z" fill="url(#lavender)"/>
    <path d="M69 240h257" stroke="#fff" stroke-width="3" opacity=".7"/>
    <path d="m143 115-23 20 23 20m109-40 23 20-23 20m-42-26-15 53" stroke="#677be7" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <rect x="160" y="226" width="75" height="14" rx="4" fill="#bac6ef"/>
    </g>"""

def chart():
    return """<g transform="rotate(-5 200 155)" filter="url(#shadow)">
    <rect x="80" y="62" width="235" height="187" rx="22" fill="url(#white)"/>
    <path d="M109 90h65m-65 15h104" stroke="#c5cfee" stroke-width="7" stroke-linecap="round"/>
    <rect x="119" y="175" width="33" height="47" rx="8" fill="url(#mint)"/>
    <rect x="169" y="148" width="33" height="74" rx="8" fill="url(#lavender)"/>
    <rect x="219" y="119" width="33" height="103" rx="8" fill="url(#blue)"/>
    <path d="m117 158 58-27 54-31 37-4" fill="none" stroke="#4d6bc9" stroke-width="5" stroke-linecap="round"/>
    </g>"""

def globe():
    return """<g filter="url(#shadow)">
    <circle cx="200" cy="148" r="99" fill="url(#blue)"/>
    <ellipse cx="200" cy="148" rx="44" ry="99" fill="none" stroke="#d6ecff" stroke-width="2" opacity=".6"/>
    <path d="M104 144h192m-176-50q80 28 160 0m-160 108q80-28 160 0" fill="none" stroke="#d6ecff" stroke-width="2" opacity=".6"/>
    <path d="m153 71 32 9 3 18-20 14-5 23-25-3-10-20 10-21zm65 60 31-10 24 20-14 25-16-5-7 30-20-6-12-31z" fill="#a3dfcb"/>
    <path d="M125 228q75 37 150 0m-83 24v16m16-16v16" fill="none" stroke="#adb6df" stroke-width="9" stroke-linecap="round"/>
    <ellipse cx="200" cy="273" rx="54" ry="9" fill="url(#lavender)"/>
    </g>"""

def calendar():
    return """<g transform="rotate(-8 200 160)" filter="url(#shadow)">
    <rect x="100" y="70" width="202" height="176" rx="20" fill="url(#lavender)"/>
    <rect x="108" y="78" width="186" height="162" rx="15" fill="#fff"/>
    <path d="M108 98q0-20 20-20h146q20 0 20 20v29H108z" fill="url(#blue)"/>
    <path d="M149 62v32m104-32v32" stroke="#8da1df" stroke-width="11" stroke-linecap="round"/>
    <g fill="#e0e7f7"><rect x="134" y="147" width="25" height="22" rx="5"/><rect x="179" y="147" width="25" height="22" rx="5"/><rect x="224" y="147" width="25" height="22" rx="5"/><rect x="134" y="187" width="25" height="22" rx="5"/><rect x="224" y="187" width="25" height="22" rx="5"/></g>
    <rect x="173" y="181" width="37" height="35" rx="10" fill="url(#mint)"/>
    <path d="m182 198 6 6 14-14" fill="none" stroke="#286c5b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    </g>"""

def shield():
    return """<g transform="rotate(-8 200 150)" filter="url(#shadow)">
    <path d="M200 48q-44 30-97 37v85q0 64 97 103 97-39 97-103V85q-53-7-97-37z" fill="url(#blue)" stroke="#bbceff" stroke-width="3"/>
    <path d="M200 67q-40 24-79 30v73q0 50 79 83 79-33 79-83V97q-39-6-79-30z" fill="url(#lavender)" opacity=".8"/>
    <path d="m158 159 28 29 57-63" fill="none" stroke="#fff" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
    </g>"""

def document():
    return """<g transform="rotate(8 200 150)" filter="url(#shadow)">
    <rect x="119" y="57" width="170" height="215" rx="17" fill="url(#lavender)"/>
    <rect x="108" y="47" width="170" height="215" rx="17" fill="url(#white)"/>
    <path d="M138 86h60m-60 27h107m-107 24h107m-107 24h78m-78 24h99" stroke="#bcc8e6" stroke-width="8" stroke-linecap="round"/>
    <circle cx="220" cy="223" r="22" fill="url(#mint)"/>
    <path d="m210 223 7 7 14-16" fill="none" stroke="#2e755d" stroke-width="4" stroke-linecap="round"/>
    </g>"""

def speech():
    return """<g filter="url(#shadow)">
    <path d="M85 70h171q26 0 26 26v95q0 26-26 26h-89l-49 34 5-34H85q-26 0-26-26V96q0-26 26-26z" fill="url(#blue)"/>
    <g fill="#eaf3ff"><circle cx="117" cy="142" r="10"/><circle cx="169" cy="142" r="10"/><circle cx="221" cy="142" r="10"/></g>
    <path d="M254 176h65q22 0 22 22v36q0 22-22 22h-5l7 23-33-23h-34q-22 0-22-22v-36q0-22 22-22z" fill="url(#mint)"/>
    <path d="M256 209h58m-58 19h39" stroke="#498c7c" stroke-width="6" stroke-linecap="round"/>
    </g>"""

def flask():
    return """<g transform="rotate(-8 200 160)" filter="url(#shadow)">
    <path d="M167 60h65v20h-10v64l62 96q11 21-12 24H127q-23-3-12-24l62-96V80h-10z" fill="url(#white)" stroke="#b3c4e7" stroke-width="3"/>
    <path d="m155 190-31 52q-5 9 8 9h134q12 0 6-9l-31-52z" fill="url(#mint)"/>
    <circle cx="186" cy="216" r="10" fill="#fff" opacity=".75"/><circle cx="222" cy="238" r="7" fill="#fff" opacity=".7"/>
    <circle cx="202" cy="174" r="7" fill="#76cab8"/><circle cx="205" cy="124" r="8" fill="#b1a3f5"/>
    <path d="m151 214-17 28" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
    </g>"""

def puzzle():
    return """<g transform="rotate(-9 200 155)" filter="url(#shadow)">
    <path d="M106 79h67q-9-30 15-30t15 30h67v67q30-9 30 15t-30 15v67h-67q9-30-15-30t-15 30h-67v-67q30 9 30-15t-30-15z" fill="url(#lavender)" stroke="#e2daff" stroke-width="3"/>
    <path d="m193 128 58 5 16 23-12 58-35-9-9-35-27-15z" fill="url(#mint)" stroke="#c1ede1" stroke-width="3"/>
    <circle cx="148" cy="118" r="11" fill="#fff" opacity=".65"/>
    </g>"""

def calculator():
    return """<g transform="rotate(10 200 155)" filter="url(#shadow)">
    <rect x="122" y="47" width="155" height="224" rx="23" fill="url(#blue)"/>
    <rect x="139" y="67" width="121" height="50" rx="9" fill="#d7eee8"/>
    <path d="M159 92h25m30-7h18m-18 12h18" stroke="#537d7d" stroke-width="5" stroke-linecap="round"/>
    <g fill="#edf0ff"><rect x="142" y="135" width="26" height="26" rx="7"/><rect x="186" y="135" width="26" height="26" rx="7"/><rect x="142" y="178" width="26" height="26" rx="7"/><rect x="186" y="178" width="26" height="26" rx="7"/><rect x="142" y="221" width="26" height="26" rx="7"/><rect x="186" y="221" width="26" height="26" rx="7"/></g>
    <rect x="230" y="135" width="26" height="26" rx="7" fill="#f6d18b"/><rect x="230" y="178" width="26" height="69" rx="7" fill="#a0dfce"/>
    </g>"""

def cookie():
    return """<g filter="url(#shadow)">
    <path d="M294 119q-27 6-43-13-15-17-10-40-71-34-122 22-50 55-16 117 35 61 104 53 71-9 86-73 6-29 1-66z" fill="url(#gold)" stroke="#f4c889" stroke-width="3"/>
    <g fill="#937456"><circle cx="153" cy="116" r="11"/><circle cx="134" cy="171" r="9"/><circle cx="183" cy="156" r="11"/><circle cx="215" cy="207" r="9"/><circle cx="170" cy="223" r="8"/><circle cx="250" cy="157" r="8"/></g>
    <path d="M131 102q31-34 75-29" stroke="#fff0d5" stroke-width="7" fill="none" stroke-linecap="round"/>
    <circle cx="290" cy="73" r="9" fill="#e8ba7c"/><circle cx="315" cy="104" r="6" fill="#e8ba7c"/>
    </g>"""

def clock():
    return """<g transform="rotate(10 200 155)" filter="url(#shadow)">
    <circle cx="200" cy="155" r="101" fill="url(#lavender)"/>
    <circle cx="200" cy="155" r="84" fill="url(#white)"/>
    <path d="M200 85v12m70 58h-12m-58 70v-12m-70-58h12" stroke="#a4b3d9" stroke-width="6" stroke-linecap="round"/>
    <path d="M200 105v52l35 25" fill="none" stroke="#5269c2" stroke-width="10" stroke-linecap="round"/>
    <circle cx="200" cy="155" r="9" fill="#7ebfac"/>
    </g>"""

def briefcase():
    return """<g transform="rotate(-8 200 155)" filter="url(#shadow)">
    <rect x="156" y="66" width="87" height="42" rx="12" fill="none" stroke="#96a8e1" stroke-width="16"/>
    <rect x="84" y="99" width="232" height="156" rx="20" fill="url(#blue)"/>
    <path d="M84 143q116 61 232 0v-26q0-18-18-18H102q-18 0-18 18z" fill="url(#lavender)"/>
    <rect x="181" y="154" width="38" height="36" rx="8" fill="url(#gold)"/>
    <path d="M102 231h196" stroke="#fff" stroke-width="3" opacity=".25"/>
    </g>"""

def letters():
    return """<g transform="rotate(-9 200 160)" filter="url(#shadow)">
    <rect x="83" y="99" width="125" height="140" rx="23" fill="url(#lavender)"/>
    <path d="m108 209 34-85 34 85m-53-27h39" fill="none" stroke="#575ea6" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
    <rect x="200" y="70" width="111" height="136" rx="21" fill="url(#mint)"/>
    <path d="M230 106v65h23q28 0 23-20-2-13-21-14h-25m0 0h22q20-1 20-16 0-15-23-15z" fill="none" stroke="#3a7969" stroke-width="10" stroke-linecap="round"/>
    </g>"""

def arabic_letters():
    return """<g transform="rotate(-7 200 160)" filter="url(#shadow)">
    <rect x="82" y="88" width="125" height="150" rx="23" fill="url(#paper)"/>
    <path d="M146 119v89" fill="none" stroke="#95774b" stroke-width="12" stroke-linecap="round"/>
    <rect x="204" y="65" width="122" height="150" rx="22" fill="url(#mint)"/>
    <path d="M226 131v22q0 24 36 24t36-24v-22" fill="none" stroke="#3a7969" stroke-width="10" stroke-linecap="round"/>
    <circle cx="262" cy="194" r="5" fill="#3a7969"/>
    </g>"""

def landmark(kind):
    if kind == "uk":
        return """<g filter="url(#shadow)"><path d="M153 258V109h94v149z" fill="url(#paper)"/><path d="M147 112h106V93H147z" fill="#d8c5a0"/><path d="m171 93 29-55 29 55z" fill="url(#blue)"/><circle cx="200" cy="143" r="25" fill="url(#white)" stroke="#c9aa79" stroke-width="5"/><path d="M200 125v18l12 6m-38 41v49m26-49v49m26-49v49" stroke="#8e865f" stroke-width="4" stroke-linecap="round"/><path d="M141 259h118" stroke="#a39780" stroke-width="10" stroke-linecap="round"/></g>"""
    if kind == "usa":
        return """<g filter="url(#shadow)"><path d="m177 241 13-88-13-27 16-30 31 2 17 31-17 29 19 83z" fill="url(#mint)"/><path d="m189 126-42-37-21-43-11 4 15 51 49 51m42-14 35-23 10 13-39 29" fill="#8bd2b9" stroke="#73b9a3" stroke-width="3"/><path d="m188 97-8-20 15 10 10-26 8 28 20-12-7 23" fill="#81c6b0"/><path d="M165 242h87v23h-87z" fill="url(#lavender)"/><path d="M154 264h109v16H154z" fill="#b9b3db"/><path d="M115 44h25l-6-22-13-11z" fill="url(#gold)"/></g>"""
    return """<g filter="url(#shadow)"><path d="M125 249h151v22H125z" fill="url(#lavender)"/><path d="m190 247 4-99h12l4 99z" fill="#a4b9de"/><path d="M164 146h72v17h-72z" fill="url(#white)"/><ellipse cx="200" cy="142" rx="42" ry="12" fill="url(#blue)"/><path d="M200 58v72" stroke="#768abd" stroke-width="4"/><path d="m295 88 10 17 19-6-7 20 18 9-22 8-9 22-7-24-23-11 20-10z" fill="url(#peach)"/><path d="M296 134v38" stroke="#d59686" stroke-width="3"/><path d="M103 250v-65h37v65m117 0v-43h39v43" fill="url(#mint)"/></g>"""

ART = {
    "subjects": ("Explore academic subjects", book, calculator, "violet"),
    "mathematics": ("Mathematics calculator and geometric learning", calculator, puzzle, "violet"),
    "english": ("English letters and reading books", letters, book, "peach"),
    "science": ("Science experiment and laboratory notes", flask, book, "mint"),
    "computer-it": ("Computer programming laptop and project notes", laptop, document, "blue"),
    "logical-reasoning": ("Logical reasoning puzzles and time challenges", puzzle, clock, "gold"),
    "quran-education": ("Quran reading and guided study", open_book, globe, "mint"),
    "quran-reading": ("Open Quran and reading progress", open_book, chart, "mint"),
    "noorani-qaida": ("Arabic letter foundations and study book", arabic_letters, open_book, "gold"),
    "tajweed": ("Recitation practice and guided reading", open_book, speech, "blue"),
    "islamic-studies": ("Islamic learning and daily study", book, open_book, "mint"),
    "countries": ("Learning across countries and local times", globe, clock, "blue"),
    "uk": ("UK curriculum with a clock tower and books", lambda: landmark("uk"), book, "blue"),
    "usa": ("US curriculum with a landmark sculpture and learning notes", lambda: landmark("usa"), document, "mint"),
    "canada": ("Canadian curriculum with a skyline and maple leaf", lambda: landmark("canada"), book, "peach"),
    "how-it-works": ("Plan a learning journey with a calendar and lesson chat", calendar, speech, "blue"),
    "parents": ("Parent progress reports and learning plans", chart, calendar, "mint"),
    "faq": ("Helpful questions and answers for families", speech, book, "violet"),
    "about": ("Connected learning around the world", globe, laptop, "blue"),
    "contact": ("Contact admissions and plan a lesson", speech, calendar, "mint"),
    "careers": ("Teaching careers and learning materials", briefcase, book, "peach"),
    "privacy": ("Privacy shield and protected information", shield, document, "blue"),
    "cookies": ("Cookie preferences and website information", cookie, laptop, "gold"),
    "terms": ("Course terms and agreed lesson schedules", document, calendar, "violet"),
    "refund-cancellation": ("Lesson changes and cancellation information", clock, document, "peach"),
    "safeguarding": ("A protected learning environment", shield, book, "mint"),
    "book-a-demo": ("Book a demo lesson and meet a tutor", calendar, laptop, "blue"),
    "portal": ("Upcoming connected learning workspaces", laptop, shield, "violet"),
    "portal/parent": ("Upcoming parent workspace with progress and schedules", chart, shield, "mint"),
    "portal/teacher": ("Upcoming teacher workspace with lessons and planning", laptop, calendar, "blue"),
}

def leaf():
    return """<g filter="url(#shadow)"><path d="M105 220Q75 77 291 60q13 200-144 195z" fill="url(#mint)" stroke="#9dd3b9" stroke-width="3"/><path d="m120 266 139-155m-83 89-17-59m45 28 48 5m-103 52-19-51" fill="none" stroke="#4c9b80" stroke-width="7" stroke-linecap="round"/></g>"""

def gulf_tower():
    return """<g filter="url(#shadow)"><path d="M189 276V82h22v194m-40 0V139h18m22 137V139h18v137m-81 0V190h23m58 86V190h24v86" fill="url(#blue)" stroke="#a6bfe8" stroke-width="3"/><path d="M200 32v50m-14 37h28m-42 43h56m-76 57h96" stroke="#d1e4ff" stroke-width="4"/><path d="M123 277h153" stroke="#a7b3d7" stroke-width="10" stroke-linecap="round"/></g>"""

from additions import EXTRA_SUBJECTS, CURRICULA, GULF_COUNTRIES, ARTICLES, NOTES

ART.update({
    "physics": ("Forces and motion with a clock and laboratory flask", clock, flask, "blue"),
    "chemistry": ("Chemistry experiments with reaction notes", flask, document, "mint"),
    "biology": ("Biology leaf structures and study notes", leaf, book, "mint"),
    "languages": ("Language practice with letters and conversation", letters, speech, "peach"),
    "humanities": ("History and geography sources around the world", globe, document, "gold"),
    "business-economics": ("Business decisions, charts and planning", chart, briefcase, "violet"),
    "curricula": ("School courses connected through books and the world", book, globe, "blue"),
    "curricula/british": ("British school curriculum and lesson planning", lambda: landmark("uk"), calendar, "blue"),
    "curricula/american": ("US school learning and academic progress", lambda: landmark("usa"), chart, "mint"),
    "curricula/ib": ("International subjects and problem solving", globe, puzzle, "violet"),
    "curricula/pakistan": ("School textbooks and board-course planning", book, calendar, "gold"),
    "test-prep": ("Preparation with a practice paper and time planning", document, clock, "blue"),
    "pricing": ("Planning a lesson package and schedule", calendar, briefcase, "violet"),
    "custom-package": ("A tailored learning plan with goals and subject notes", puzzle, chart, "mint"),
    "free-notes": ("A free collection of subject books and practice notes", book, document, "peach"),
    "journal": ("Learning articles and study ideas", book, speech, "violet"),
    "progress": ("Progress review with learning goals and practice notes", chart, book, "blue"),
    "learning-levels": ("Learning from foundations to advanced school study", letters, globe, "mint"),
    "uae": ("UAE skyline and school learning", gulf_tower, book, "blue"),
    "saudi-arabia": ("Study planning for Saudi families", calendar, globe, "mint"),
    "qatar": ("Lessons for Qatar with a local schedule", gulf_tower, clock, "peach"),
    "oman": ("Study materials and scheduling for Oman", book, clock, "gold"),
    "other-countries": ("A local learning plan wherever you study", globe, speech, "blue"),
})
article_art = [(calendar, book), (laptop, speech), (globe, chart), (document, puzzle), (document, chart)]
for (slug,title,*_), (primary,secondary) in zip(ARTICLES, article_art):
    ART[f"journal/{slug}"] = (title, primary, secondary, "blue")
note_art = [(calculator,chart),(clock,calculator),(flask,calculator),(leaf,flask),(letters,document),(laptop,puzzle),(chart,calculator),(briefcase,globe),(globe,leaf),(document,globe),(chart,puzzle),(calculator,book)]
for (slug,title,*_), (primary,secondary) in zip(NOTES, note_art):
    ART[f"free-notes/{slug}"] = (title, primary, secondary, "mint")

def generate_artwork(destination):
    directory = Path(destination) / "assets" / "pages"
    directory.mkdir(parents=True, exist_ok=True)
    palettes = {"violet":("#eee8ff","#cbc0ef"),"peach":("#fff0e8","#e9c8bb"),"mint":("#e7f7ef","#bbdccc"),"blue":("#e9f0ff","#b5caee"),"gold":("#fff5dd","#e7d4aa")}
    for route, (title, primary, secondary, tone) in ART.items():
        light, dark = palettes[tone]
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" aria-label="{title.replace(chr(38), chr(38)+'amp;')}">
        <defs>
        <linearGradient id="blue" x2=".8" y2="1"><stop stop-color="#9ab7ff"/><stop offset=".5" stop-color="#637fe2"/><stop offset="1" stop-color="#3f56b7"/></linearGradient>
        <linearGradient id="lavender" x2=".8" y2="1"><stop stop-color="#eee8ff"/><stop offset=".6" stop-color="#c4b9ef"/><stop offset="1" stop-color="#9e91cf"/></linearGradient>
        <linearGradient id="mint" x2=".8" y2="1"><stop stop-color="#d8faed"/><stop offset="1" stop-color="#8ac7b4"/></linearGradient>
        <linearGradient id="paper" x2=".6" y2="1"><stop stop-color="#fff3d6"/><stop offset="1" stop-color="#e2c795"/></linearGradient>
        <linearGradient id="gold" x2=".8" y2="1"><stop stop-color="#ffe6ac"/><stop offset="1" stop-color="#dcad6a"/></linearGradient>
        <linearGradient id="peach" x2=".8" y2="1"><stop stop-color="#ffe5db"/><stop offset="1" stop-color="#e8a894"/></linearGradient>
        <linearGradient id="white" x2=".6" y2="1"><stop stop-color="#fff"/><stop offset="1" stop-color="#e3e8f5"/></linearGradient>
        <radialGradient id="bg"><stop stop-color="{light}"/><stop offset="1" stop-color="#fcfbff"/></radialGradient>
        <linearGradient id="platform" x2="0" y2="1"><stop stop-color="{light}"/><stop offset="1" stop-color="{dark}"/></linearGradient>
        <filter id="shadow" x="-45%" y="-45%" width="200%" height="220%"><feDropShadow dx="1" dy="9" stdDeviation="6" flood-color="#465180" flood-opacity=".22"/></filter>
        </defs>
        <rect width="480" height="360" rx="36" fill="url(#bg)"/>
        <ellipse cx="239" cy="166" rx="189" ry="100" fill="none" stroke="{dark}" opacity=".6" transform="rotate(-19 239 166)"/>
        <ellipse cx="239" cy="166" rx="180" ry="116" fill="none" stroke="{dark}" stroke-dasharray="2 7" opacity=".5" transform="rotate(21 239 166)"/>
        <ellipse cx="230" cy="303" rx="143" ry="25" fill="url(#platform)" filter="url(#shadow)"/>
        <g transform="translate(14 8)">{primary()}</g>
        <g transform="translate(288 145) scale(.36)">{secondary()}</g>
        <circle cx="79" cy="101" r="12" fill="url(#mint)" filter="url(#shadow)"/>
        <circle cx="366" cy="67" r="10" fill="url(#lavender)"/>
        <path d="M358 264q3 13 16 16-13 3-16 16-3-13-16-16 13-3 16-16z" fill="#b3a2e1"/>
        <path d="M104 48q2 8 10 10-8 2-10 10-2-8-10-10 8-2 10-10z" fill="#dbc396"/>
        </svg>"""
        (directory / (route.replace("/", "-") + ".svg")).write_text(svg, encoding="utf-8")

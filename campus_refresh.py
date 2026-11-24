"""Compact campus presentation, photo sources and school-stage roadmap."""
from html import escape as e
from urllib.parse import urlencode

# Editorial stock imagery only: no depicted person is identified as FCC staff or a customer.
PORTRAITS=[8617757,8423062,5212321,8326324,8422401,6325962,8618069,8423866,5212361,7156124,6700553,3779445]
def photo(photo_id,width=1000):
 return f'https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w={width}'

def stock_image(photo_id,alt,extra='',width=1000):
 return f'<img class="{extra}" src="{e(photo(photo_id,width),quote=True)}" alt="{e(alt,quote=True)}" width="{width}" height="{round(width*.75)}" loading="lazy" decoding="async" referrerpolicy="no-referrer">'

def feedback_empty():
 return f'''<div class="feedback-showcase"><figure class="feedback-photo">{stock_image(4260475,'A parent helping a child learn on a laptop; editorial stock photograph')}<figcaption>Learning together · stock photography</figcaption><span class="feedback-photo-tag" aria-hidden="true">Small steps.<br>Shared moments.</span></figure><div class="feedback-story"><span class="studio-label">THE FAMILY PERSPECTIVE</span><h3>Behind every lesson,<br><em>there’s a learning story.</em></h3><p>Questions asked. Ideas understood. A little more confidence with the next step.</p><div class="feedback-principles"><span>Patient guidance</span><span>Personal pace</span><span>Clear communication</span></div><div class="feedback-pending"><span class="feedback-pending-dot" aria-hidden="true"></span><p>Family reviews will appear here after families share their stories and approve them for publication.</p></div><a class="btn secondary" href="/contact/">Talk to the campus <span aria-hidden="true">↗</span></a></div></div>'''

def learning_roadmap(levels):
 focuses=[['Reading & writing','Number sense','Curiosity'],['Subject connections','Study habits','Independent thinking'],['Core concepts','Exam practice','Revision routines'],['Advanced topics','Course depth','Next-step planning']]
 images=['mathematics','science','test-prep','curricula']
 steps=[]
 for i,(level,title,desc) in enumerate(levels):
  href='/book-a-demo/?'+urlencode({'level':level})
  chips=''.join(f'<span>{e(x)}</span>' for x in focuses[i])
  steps.append(f'''<li class="roadmap-step" id="stage-{i+1}"><span class="roadmap-node" aria-label="Stage {i+1}">0{i+1}</span><article class="roadmap-card studio-reveal" data-studio-card><div class="roadmap-card-top"><span class="studio-label">{e(level)}</span><span class="roadmap-symbol" aria-hidden="true">{'✳' if i%2==0 else '↗'}</span></div><h3>{e(title)}</h3><p>{e(desc)}</p><div class="roadmap-focus">{chips}</div><div class="roadmap-card-bottom"><a class="studio-inline-link" href="{e(href,quote=True)}">Discuss this stage <span aria-hidden="true">↗</span></a><img src="/assets/pages/{images[i]}.svg" width="140" height="105" alt="" loading="lazy"></div></article></li>''')
 nav=''.join(f'<a href="#stage-{i+1}"><span>0{i+1}</span>{e(level)}</a>' for i,(level,*_) in enumerate(levels))
 return f'''<section class="shell section learning-path-intro"><div><span class="studio-label">ONE JOURNEY. YOUR OWN PACE.</span><h2>A little progress.<br><em>A bigger horizon.</em></h2></div><p>There’s no single starting line. Find the stage closest to your child’s current course, then shape the next step around their understanding.</p></section><nav class="shell roadmap-jumps" aria-label="Jump to a learning stage">{nav}</nav><section class="shell section roadmap-section" aria-label="Learning stages roadmap"><ol class="learning-roadmap">{''.join(steps)}</ol><div class="roadmap-destination"><span aria-hidden="true">✦</span><h3>The next chapter is yours.</h3><p>School-year and grade equivalents vary. Your school course and current understanding guide the plan.</p><a class="btn primary" href="/book-a-demo/">Find your starting point</a></div></section><section class="roadmap-fit-band"><div class="shell section roadmap-fit"><div><span class="studio-label">BUILT AROUND THE LEARNER</span><h2>The right stage.<br>The right next step.</h2></div><ol><li><span>01</span><div><h3>Share the course</h3><p>Tell us the school year, curriculum and current topic.</p></div></li><li><span>02</span><div><h3>Bring a recent question</h3><p>See where understanding feels secure and where support would help.</p></div></li><li><span>03</span><div><h3>Agree a manageable focus</h3><p>Choose a clear learning goal, lesson rhythm and starting point.</p></div></li></ol></div></section>'''

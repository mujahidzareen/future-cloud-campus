'use strict';
// Presentation only. The homepage hero, text, URLs and interactive workspaces are protected.
(()=>{
 const root=document.documentElement,main=document.querySelector('main'),reduce=matchMedia('(prefers-reduced-motion: reduce)'),wide=matchMedia('(min-width: 900px)');
 if(!main||!('IntersectionObserver' in window)||!CSS.supports('translate','0 1px'))return;
 const protectedArea='.discovery-hero,.studio-hero,.site-header,.site-footer,dialog,form,.quran-library,[data-quran-reader],[data-learning-workbook],[data-lesson],[data-lesson-peek],.reader-layout,.article-body,.reading-panel,.portal-main';
 const excluded=node=>Boolean(node.closest(protectedArea));
 const nodes=[],registered=new Set(),scenes=new Map(),active=new Set();let frame=0;
 const paused=()=>reduce.matches||root.classList.contains('motion-paused')||document.hidden;
 const add=(node,kind,delay=0)=>{
  if(excluded(node)||registered.has(node)||node.closest('[data-campus-motion]'))return;
  // Replace the previous entry effect on this node, retaining its layout and hover transform.
  node.classList.remove('studio-reveal','reveal');node.classList.add('is-revealed','visible');
  node.dataset.campusMotion=kind;
  if(node.matches('a,button')||node.querySelector('a,button,input,select,textarea'))node.dataset.campusStable='';
  node.style.setProperty('--campus-delay',`${delay}ms`);registered.add(node);nodes.push(node);
  if(kind==='visual'&&!node.querySelector('button,input,select,textarea,a'))scenes.set(node,{shift:0});
 };
 // Protected workspaces are skipped even when they share a visual class.
 main.querySelectorAll('.page-illustration,.faculty-teaser-art,.discovery-quran figure,.campus-story-scene,.campus-ceo-photo,.faculty-hero-art,.lesson-window,.feedback-showcase,.discovery-finale>img').forEach(node=>add(node,'visual'));
 const cards='.discovery-subject,.subject-card,.resource-card,.story-card,.plan-card,.faculty-card,.info-card,.discovery-resource,.campus-offer-grid>a,.campus-values-grid>article,.campus-next-grid>a,.roadmap-card,.exam-card,.feature-link';
 main.querySelectorAll(cards).forEach(node=>{
  if(node.closest('[data-review-carousel]'))return;
  const siblings=[...node.parentElement.children].filter(item=>item.matches(cards));add(node,'card',Math.min(siblings.indexOf(node),3)*85);
 });
 main.querySelectorAll('[data-review-carousel]').forEach(node=>add(node,'group'));
 main.querySelectorAll('h1,h2,.section-head>.eyebrow,.discovery-section-head .discovery-eyebrow,.campus-ceo-message>.studio-label').forEach(node=>add(node,node.matches('h1,h2')?'title':'label'));
 main.querySelectorAll('.discovery-section-head>p,.discovery-section-head>div>p,.discovery-lesson-copy>p,.faculty-teaser-copy>p,.campus-story>div>p,.campus-ceo-letter,.roadmap-fit>ol,.quote-checklist,.campus-method-grid,.discovery-course-links,.campus-purpose-grid>article>p').forEach(node=>add(node,'copy',70));
 if(!nodes.length)return;
 const clearScene=node=>{const data=scenes.get(node);if(data)data.shift=0;node.style.removeProperty('--campus-drift');node.style.removeProperty('--campus-zoom');node.style.removeProperty('--campus-turn');};
 const reveal=node=>{node.classList.add('campus-entered');};
 const revealTree=node=>{const owner=node.closest('[data-campus-motion]');if(owner)reveal(owner);node.querySelectorAll?.('[data-campus-motion]').forEach(reveal);};
 const paint=()=>{
  frame=0;if(paused()||!wide.matches){active.forEach(clearScene);return;}
  const height=innerHeight;
  active.forEach(node=>{
   if(!node.classList.contains('campus-entered')||node.matches(':focus-within')){clearScene(node);return;}
   const data=scenes.get(node),box=node.getBoundingClientRect(),origin=box.top-data.shift;
   const phase=Math.max(-1,Math.min(1,(height*.5-origin-box.height*.5)/(height*.5+box.height*.5)));
   data.shift=phase*22;
   node.style.setProperty('--campus-drift',`${data.shift.toFixed(2)}px`);
   node.style.setProperty('--campus-zoom',(1.008-Math.abs(phase)*.012).toFixed(4));
   node.style.setProperty('--campus-turn',`${(-phase*1.4).toFixed(2)}deg`);
  });
 };
 const schedule=()=>{if(!frame)frame=requestAnimationFrame(paint);};
 const enter=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){reveal(entry.target);enter.unobserve(entry.target);}}),{threshold:.08,rootMargin:'0px 0px -28px 0px'});
 const view=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting)active.add(entry.target);else{active.delete(entry.target);clearScene(entry.target);}});schedule();},{rootMargin:'90px'});
 const sync=()=>{
  if(paused()){nodes.forEach(reveal);scenes.forEach((_,node)=>clearScene(node));if(frame)cancelAnimationFrame(frame);frame=0;}
  else schedule();
 };
 try{
  nodes.forEach(node=>{if(node.getBoundingClientRect().top<innerHeight-24)reveal(node);enter.observe(node);});
  scenes.forEach((_,node)=>view.observe(node));
  root.classList.add('campus-motion-ready');
  addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule,{passive:true});
  if('ResizeObserver' in window)new ResizeObserver(schedule).observe(main);
  // Keyboard focus and fragment navigation always reveal their destination immediately.
  main.addEventListener('focusin',event=>{revealTree(event.target);schedule();});
  const showHash=()=>{if(!location.hash)return;let target;try{target=document.getElementById(decodeURIComponent(location.hash.slice(1)));}catch{return;}if(target)revealTree(target);};
  addEventListener('hashchange',showHash);addEventListener('pageshow',()=>{showHash();sync();});showHash();
  new MutationObserver(sync).observe(root,{attributes:true,attributeFilter:['class']});
  reduce.addEventListener('change',sync);wide.addEventListener('change',sync);document.addEventListener('visibilitychange',sync);sync();
 }catch{
  // Failing open keeps every piece of content visible if a browser cannot run the effect.
  root.classList.remove('campus-motion-ready');nodes.forEach(reveal);scenes.forEach((_,node)=>clearScene(node));
 }
})();

// Original orbital chapters and a continuous roadmap. No scroll hijacking or animation library.
(()=>{
 const root=document.documentElement,main=document.querySelector('main');if(!main||!('IntersectionObserver' in window))return;
 const reduce=matchMedia('(prefers-reduced-motion: reduce)'),wide=matchMedia('(min-width: 900px)'),fine=matchMedia('(hover:hover) and (pointer:fine)');
 const chapters=[...main.querySelectorAll('.discovery-subjects,.discovery-lesson,.discovery-quran,.discovery-feedback,.campus-story,.learning-roadmap')];
 const active=new Set(),resets=[];let frame=0;
 const paused=()=>reduce.matches||root.classList.contains('motion-paused')||document.hidden;
 const clamp=value=>Math.max(0,Math.min(1,value));
 const paint=()=>{
  frame=0;if(paused())return;
  active.forEach(node=>{
   const box=node.getBoundingClientRect(),height=innerHeight;
   const progress=clamp((height-box.top)/(height+box.height));
   node.style.setProperty('--chapter-progress',progress.toFixed(4));
   node.style.setProperty('--orbit-phase',`${((progress-.5)*(wide.matches?100:35)).toFixed(2)}deg`);
   node.style.setProperty('--chapter-curve',`${(50-Math.sin(progress*Math.PI)*27).toFixed(1)}px`);
   if(node.matches('.learning-roadmap')){
    node.style.setProperty('--road-progress',String(clamp((height*.6-box.top-24)/(box.height-24))));
    node.querySelectorAll('.roadmap-step').forEach(step=>step.classList.toggle('is-milestone-reached',step.getBoundingClientRect().top<height*.6));
   }
  });
 };
 const schedule=()=>{if(!frame&&!paused())frame=requestAnimationFrame(paint);};
 const view=new IntersectionObserver(entries=>{entries.forEach(({target,isIntersecting})=>{if(isIntersecting)active.add(target);else active.delete(target);});schedule();},{rootMargin:'100px'});
 chapters.forEach(node=>{node.dataset.campusChapter='';view.observe(node);});
 const excluded='.discovery-hero,.studio-hero,dialog,form,[data-quran-reader],.quran-library,[data-learning-workbook],[data-lesson],[data-lesson-peek],.article-body,.reading-panel,.reader-layout,.portal-main';
 main.querySelectorAll('.discovery-subject,.discovery-resource,.subject-card,.resource-card,.story-card,.plan-card,.faculty-card,.campus-offer-grid>a,.campus-values-grid>article,.campus-next-grid>a,.roadmap-card,.pricing-preview-card,.review-card').forEach(node=>{
  if(node.closest(excluded))return;node.dataset.campusSurface='';let raf=0,x=50,y=30,box;
  const clear=()=>{if(raf)cancelAnimationFrame(raf);raf=0;node.style.removeProperty('--surface-x');node.style.removeProperty('--surface-y');};resets.push(clear);
  node.addEventListener('pointerenter',()=>{box=node.getBoundingClientRect();},{passive:true});
  node.addEventListener('pointermove',event=>{if(paused()||!fine.matches||!box)return;x=clamp((event.clientX-box.left)/box.width)*100;y=clamp((event.clientY-box.top)/box.height)*100;if(!raf)raf=requestAnimationFrame(()=>{raf=0;node.style.setProperty('--surface-x',`${x.toFixed(1)}%`);node.style.setProperty('--surface-y',`${y.toFixed(1)}%`);});},{passive:true});
  node.addEventListener('pointerleave',clear,{passive:true});node.addEventListener('pointercancel',clear,{passive:true});
 });
 main.querySelectorAll('.btn').forEach(node=>{if(!node.closest(excluded))node.dataset.campusButton='';});
 const sync=()=>{if(paused()){if(frame)cancelAnimationFrame(frame);frame=0;resets.forEach(reset=>reset());}else schedule();};
 addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule,{passive:true});
 if('ResizeObserver' in window)new ResizeObserver(schedule).observe(main);
 new MutationObserver(sync).observe(root,{attributes:true,attributeFilter:['class']});
 reduce.addEventListener('change',sync);wide.addEventListener('change',sync);fine.addEventListener('change',sync);document.addEventListener('visibilitychange',sync);sync();
})();

'use strict';
// Small native interactions; normal document scrolling and links remain intact.
(()=>{
 const root=document.documentElement,reduce=matchMedia('(prefers-reduced-motion: reduce)'),fine=matchMedia('(hover:hover) and (pointer:fine)'),motionButton=document.querySelector('[data-motion-global]');
 try{if(sessionStorage.getItem('fcc-motion-paused')==='true'){root.classList.add('motion-paused');motionButton?.setAttribute('aria-pressed','true');motionButton?.setAttribute('aria-label','Resume animations');if(motionButton)motionButton.title='Resume animations';}}catch{}
 const paused=()=>reduce.matches||root.classList.contains('motion-paused');
 const revealNodes=[...document.querySelectorAll('.studio-reveal')];
 if('IntersectionObserver' in window&&!reduce.matches){
  const reveals=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-revealed');reveals.unobserve(entry.target);}}),{threshold:.08,rootMargin:'0px 0px -20px 0px'});
  root.classList.add('studio-motion-ready');revealNodes.forEach(node=>reveals.observe(node));
 }
 const revealAll=()=>revealNodes.forEach(node=>node.classList.add('is-revealed'));
 const progress=document.createElement('div');progress.className='studio-scroll-progress';progress.setAttribute('aria-hidden','true');document.body.append(progress);
 const stage=document.querySelector('[data-studio-scene]');let stageVisible=Boolean(stage),scrollFrame=0;
 const scrollPaint=()=>{scrollFrame=0;const total=document.documentElement.scrollHeight-innerHeight;root.style.setProperty('--scroll-progress',String(total>0?scrollY/total:0));if(stage&&stageVisible&&!paused()&&innerWidth>690){const rect=stage.getBoundingClientRect(),offset=Math.max(-30,Math.min(30,(innerHeight*.45-rect.top-rect.height*.5)*.065));stage.style.setProperty('--scene-shift',`${offset}px`);}else stage?.style.removeProperty('--scene-shift');};
 const scheduleScroll=()=>{if(!scrollFrame)scrollFrame=requestAnimationFrame(scrollPaint);};
 addEventListener('scroll',scheduleScroll,{passive:true});addEventListener('resize',scheduleScroll,{passive:true});
 if('ResizeObserver' in window)new ResizeObserver(scheduleScroll).observe(document.body);scheduleScroll();
 if('IntersectionObserver' in window){const view=new IntersectionObserver(entries=>entries.forEach(entry=>{entry.target.classList.toggle('motion-out-of-view',!entry.isIntersecting);if(entry.target===stage)stageVisible=entry.isIntersecting;}),{rootMargin:'80px'});document.querySelectorAll('[data-studio-scene],[data-studio-marquee],.studio-journey-flower,.studio-quran-picture').forEach(node=>view.observe(node));}
 const moves=[];
 const interactive=(node,xvar,yvar,scale,transformOnly=false)=>{
  let box=null,frame=0,lastX=0,lastY=0;
  const reset=()=>{if(frame)cancelAnimationFrame(frame);frame=0;node.style.removeProperty(xvar);node.style.removeProperty(yvar);};moves.push(reset);
  node.addEventListener('pointerenter',()=>{box=node.getBoundingClientRect();},{passive:true});
  node.addEventListener('pointermove',event=>{if(paused()||!fine.matches||!box)return;lastX=Math.max(-.5,Math.min(.5,(event.clientX-box.left)/box.width-.5));lastY=Math.max(-.5,Math.min(.5,(event.clientY-box.top)/box.height-.5));if(!frame)frame=requestAnimationFrame(()=>{frame=0;node.style.setProperty(xvar,`${transformOnly?lastX*scale:-lastY*scale}${transformOnly?'px':'deg'}`);node.style.setProperty(yvar,`${transformOnly?lastY*scale:lastX*scale}${transformOnly?'px':'deg'}`);});},{passive:true});
  node.addEventListener('pointerleave',reset,{passive:true});node.addEventListener('pointercancel',reset,{passive:true});
 };
 if(stage)interactive(stage,'--scene-x','--scene-y',12);
 document.querySelectorAll('[data-studio-card]').forEach(node=>interactive(node,'--card-x','--card-y',7));
 document.querySelectorAll('.btn').forEach(node=>interactive(node,'--magnet-x','--magnet-y',7,true));
 const motionChanged=()=>{try{sessionStorage.setItem('fcc-motion-paused',String(root.classList.contains('motion-paused')));}catch{}moves.forEach(reset=>reset());stage?.style.removeProperty('--scene-shift');if(paused())revealAll();scheduleScroll();};
 motionButton?.addEventListener('click',motionChanged);reduce.addEventListener('change',motionChanged);fine.addEventListener('change',motionChanged);
 document.addEventListener('visibilitychange',()=>{if(document.hidden){moves.forEach(reset=>reset());}});
})();

// Pathway choices update real destinations; enquiries retain the selected context.
document.querySelectorAll('[data-pathway-picker]').forEach(picker=>{
 const data=JSON.parse(picker.querySelector('[data-pathway-data]').textContent),stage=picker.querySelector('[data-pathway-stage]'),curriculum=picker.querySelector('[data-pathway-curriculum]');
 const enquiry=picker.querySelector('[data-pathway-enquiry]'),guide=picker.querySelector('[data-pathway-guide]'),resources=picker.querySelector('[data-pathway-resources]');
 const base=new URL('../',picker.querySelector('[data-pathway-maths]').href);
 const incoming=new URLSearchParams(location.search);
 const stageIndex=data.stages.findIndex(item=>item.name===incoming.get('stage'));
 if(stageIndex>=0)stage.value=String(stageIndex);
 const curriculumIndex=data.curricula.findIndex(item=>item.name===incoming.get('curriculum'));
 if(curriculumIndex>=0)curriculum.value=String(curriculumIndex);
 const render=(announce=false)=>{
  const selected=data.stages[Number(stage.value)],course=data.curricula[Number(curriculum.value)];
  picker.querySelector('[data-pathway-context]').textContent=`${selected.name} · ${course.name}`;
  picker.querySelector('[data-pathway-heading]').textContent=selected.title;
  picker.querySelector('[data-pathway-description]').textContent=selected.description;
  picker.querySelector('[data-pathway-course]').textContent=course.description;
  const url=new URL('book-a-demo/',base);url.searchParams.set('level',selected.name);url.searchParams.set('curriculum',course.name);url.searchParams.set('goal',`Explore ${selected.name.toLowerCase()} support. Confirm the school course and current topics.`);enquiry.href=url.href;
  guide.href=new URL(`curricula/${course.slug}/`,base).href;guide.textContent=`${course.name} guide`;
  const advanced=Number(stage.value)>1;
  resources.href=new URL(advanced?'free-notes/':'try-a-lesson/',base).href;resources.textContent=advanced?'Explore topic guides':'Try a foundation activity';
  picker.querySelector('[data-pathway-roadmap]').href=`#stage-${Number(stage.value)+1}`;
  document.querySelectorAll('.roadmap-step').forEach((item,i)=>item.classList.toggle('is-pathway-selected',i===Number(stage.value)));
  if(announce)picker.querySelector('[data-pathway-status]').textContent=`Showing ${selected.name}, ${course.name}. Subject links, learning resources and enquiry are ready.`;
 };
 stage.addEventListener('change',()=>render(true));curriculum.addEventListener('change',()=>render(true));render();
});

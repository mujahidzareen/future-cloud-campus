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
 let halo=null,haloFrame=0,pointerX=0,pointerY=0;
 if(fine.matches&&!reduce.matches){halo=document.createElement('div');halo.className='studio-cursor-halo';halo.setAttribute('aria-hidden','true');document.body.append(halo);
  document.addEventListener('pointermove',event=>{if(paused()||!fine.matches){halo.classList.remove('is-visible');return;}pointerX=event.clientX;pointerY=event.clientY;halo.classList.add('is-visible');halo.classList.toggle('is-over-link',Boolean(event.target.closest('a,button,summary')));if(!haloFrame)haloFrame=requestAnimationFrame(()=>{haloFrame=0;halo.style.transform=`translate(calc(${pointerX}px - 50%),calc(${pointerY}px - 50%))`;});},{passive:true});
  document.addEventListener('pointerleave',()=>halo.classList.remove('is-visible'),{passive:true});
 }
 const motionChanged=()=>{try{sessionStorage.setItem('fcc-motion-paused',String(root.classList.contains('motion-paused')));}catch{}moves.forEach(reset=>reset());stage?.style.removeProperty('--scene-shift');halo?.classList.remove('is-visible');if(paused())revealAll();scheduleScroll();};
 motionButton?.addEventListener('click',motionChanged);reduce.addEventListener('change',motionChanged);fine.addEventListener('change',motionChanged);
 document.addEventListener('visibilitychange',()=>{if(document.hidden){moves.forEach(reset=>reset());halo?.classList.remove('is-visible');}});
})();

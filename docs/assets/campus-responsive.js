'use strict';
// Pause the illustrations outside the viewport; the global motion switch handles user preference.
(()=>{
 if(!('IntersectionObserver' in window))return;
 const observer=new IntersectionObserver(entries=>entries.forEach(({target,isIntersecting})=>target.classList.toggle('scene-offscreen',!isIntersecting)),{rootMargin:'100px'});
 document.querySelectorAll('[data-page-scene]').forEach(scene=>observer.observe(scene));
})();

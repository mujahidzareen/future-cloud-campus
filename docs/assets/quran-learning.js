'use strict';
// Original foundation workbooks, progressively enhanced from readable HTML.
document.querySelectorAll('[data-learning-workbook]').forEach(book=>{
 const steps=[...book.querySelectorAll('[data-lesson-select]')],lessons=[...book.querySelectorAll('[data-learning-lesson]')],prev=book.querySelector('[data-learning-prev]'),next=book.querySelector('[data-learning-next]');
 let current=0;
 const show=(index,focus=false)=>{
  current=Math.max(0,Math.min(lessons.length-1,index));
  lessons.forEach((panel,i)=>panel.hidden=i!==current);
  steps.forEach((link,i)=>{if(i===current)link.setAttribute('aria-current','step');else link.removeAttribute('aria-current');});
  prev.disabled=current===0;next.disabled=current===lessons.length-1;
  book.querySelector('[data-learning-progress]').textContent=`Lesson ${current+1} of ${lessons.length}`;
  if(focus){history.replaceState(null,'',`#lesson-${current+1}`);lessons[current].querySelector('h3').focus({preventScroll:true});lessons[current].scrollIntoView({block:'start',behavior:'auto'});}
 };
 steps.forEach((link,i)=>link.addEventListener('click',event=>{event.preventDefault();show(i,true);}));
 prev.addEventListener('click',()=>show(current-1,true));next.addEventListener('click',()=>show(current+1,true));
 book.querySelector('[data-learning-controls]').hidden=false;
 const hash=location.hash.match(/^#lesson-(\d+)$/);show(hash?Number(hash[1])-1:0);
 window.addEventListener('hashchange',()=>{const h=location.hash.match(/^#lesson-(\d+)$/);if(h)show(Number(h[1])-1);});
});

const reader=document.querySelector('[data-quran-reader]');
if(reader){
 const script=document.querySelector('script[src*="quran-learning.js"]'),base=new URL('quran/',script.src);
 const select=reader.querySelector('[data-reader-surah]'),ayah=reader.querySelector('[data-reader-ayah]'),verses=reader.querySelector('[data-reader-verses]'),status=reader.querySelector('[data-reader-status]'),error=reader.querySelector('[data-reader-error]'),previous=reader.querySelector('[data-reader-prev]'),next=reader.querySelector('[data-reader-next]'),prevSurah=reader.querySelector('[data-reader-prev-surah]'),nextSurah=reader.querySelector('[data-reader-next-surah]'),toggle=reader.querySelector('[data-reader-translation]'),resume=reader.querySelector('[data-reader-resume]');
 const pageSize=20,cache=new Map();let catalogue,activeSurah=1,rows=[],start=0,request=0,size=32,saved=null,busy=false;
 try{const s=JSON.parse(localStorage.getItem('fcc-quran-position'));if(s&&Number.isInteger(s.surah)&&s.surah>=1&&s.surah<=114&&Number.isInteger(s.ayah)&&s.ayah>0&&s.ayah<=286)saved=s;}catch{}
 resume.hidden=!saved;
 const setBusy=value=>{busy=value;verses.setAttribute('aria-busy',String(value));reader.querySelector('[type=submit]').disabled=value;previous.disabled=value||start===0;next.disabled=value||start+pageSize>=rows.length;prevSurah.disabled=value||activeSurah===1;nextSurah.disabled=value||activeSurah===114;};
 const el=(tag,className,text)=>{const node=document.createElement(tag);if(className)node.className=className;if(text!==undefined)node.textContent=text;return node;};
 const updateURL=target=>{const url=new URL(location.href);url.searchParams.set('surah',String(activeSurah));url.searchParams.set('ayah',String(target));history.replaceState(null,'',url);};
 const render=(target=0)=>{
  const info=catalogue.chapters[activeSurah-1],fragment=document.createDocumentFragment();
  rows.slice(start,start+pageSize).forEach(row=>{
   const article=el('article','reader-verse');article.id=`ayah-${row.aya}`;article.dataset.ayah=String(row.aya);
   const top=el('div','verse-top'),reference=el('span','verse-reference',`${activeSurah}:${row.aya}`),save=el('button','verse-save',saved?.surah===activeSurah&&saved?.ayah===row.aya?'Saved here':'Save position');save.type='button';save.setAttribute('aria-label',`Save reading position at ${activeSurah}:${row.aya}`);
   save.addEventListener('click',()=>{try{const position={surah:activeSurah,ayah:row.aya};localStorage.setItem('fcc-quran-position',JSON.stringify(position));saved=position;resume.hidden=false;reader.querySelectorAll('.verse-save').forEach(b=>b.textContent='Save position');save.textContent='Saved here';status.textContent=`Saved ${info.name}, ayah ${row.aya} in this browser.`;}catch{status.textContent='Saving is unavailable in this browser. You can keep this page URL to return to the selected ayah.';}});
   top.append(reference,save);const arabic=el('p','quran-arabic notranslate',row.arabic_text);arabic.lang='ar';arabic.dir='rtl';arabic.translate=false;
   const translation=el('div','verse-translation notranslate');translation.lang='ur';translation.dir='rtl';translation.translate=false;translation.hidden=!toggle.checked;translation.append(el('p','quran-urdu',row.translation));
   if(row.footnotes){const details=el('details','verse-footnotes');details.append(el('summary','',`Footnotes · ${activeSurah}:${row.aya}`),el('p','',row.footnotes));translation.append(details);}
   article.append(top,arabic,translation);if(row.aya===target)article.classList.add('is-selected-ayah');fragment.append(article);
  });
  verses.replaceChildren(fragment);reader.querySelector('[data-reader-title]').textContent=`${activeSurah}. ${info.name}`;reader.querySelector('[data-reader-count]').textContent=`${rows.length} ayahs`;
  reader.querySelector('[data-reader-page]').textContent=`Ayahs ${start+1}–${Math.min(start+pageSize,rows.length)} of ${rows.length}`;
  status.textContent=`${info.name} · ayahs ${start+1} to ${Math.min(start+pageSize,rows.length)} loaded.`;
  setBusy(false);updateURL(target||start+1);
 };
 const loadPack=async pack=>{
  if(cache.has(pack))return cache.get(pack);
  const response=await fetch(new URL(`pack-${pack}.json.gz?v=${reader.dataset.quranVersion}`,base),{credentials:'same-origin'});if(!response.ok)throw new Error('download');
  const bytes=new Uint8Array(await response.arrayBuffer());let text;
  if(bytes[0]===31&&bytes[1]===139){if(!('DecompressionStream' in window))throw new Error('browser');text=await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'))).text();}
  else text=new TextDecoder().decode(bytes);
  const data=JSON.parse(text);cache.set(pack,data);return data;
 };
 const open=async(surah,target=1)=>{
  const token=++request;activeSurah=Math.max(1,Math.min(114,Number(surah)||1));select.value=String(activeSurah);error.hidden=true;verses.replaceChildren();setBusy(true);status.textContent='Loading Quran reading text…';
  try{
   if(!catalogue){const r=await fetch(new URL(`index.json?v=${reader.dataset.quranVersion}`,base),{credentials:'same-origin'});if(!r.ok)throw new Error('catalogue');catalogue=await r.json();}
   const info=catalogue.chapters[activeSurah-1];ayah.max=String(info.count);target=Math.max(1,Math.min(info.count,Number(target)||1));ayah.value=String(target);
   const pack=await loadPack(info.pack);if(token!==request)return;
   const values=pack[String(activeSurah)];if(!Array.isArray(values)||values.length!==info.count||values.some((r,i)=>r.sura!==activeSurah||r.aya!==i+1||typeof r.arabic_text!=='string'||typeof r.translation!=='string'))throw new Error('validation');
   rows=values;start=Math.floor((target-1)/pageSize)*pageSize;render(target);if(target>start+1)document.getElementById(`ayah-${target}`)?.scrollIntoView({block:'start',behavior:'auto'});
  }catch(cause){if(token!==request)return;rows=[];setBusy(false);error.hidden=false;reader.querySelector('[data-reader-error-copy]').textContent=cause.message==='browser'?'This browser cannot open the local reading files. Please use an up-to-date browser or read on QuranEnc.com.':'The reading file could not be loaded. Try again, or use the source reader below.';status.textContent='Reader unavailable. No verse text has been substituted.';}
 };
 const page=direction=>{if(busy)return;start=Math.max(0,Math.min(Math.floor((rows.length-1)/pageSize)*pageSize,start+direction*pageSize));ayah.value=String(start+1);render();verses.tabIndex=-1;verses.focus({preventScroll:true});verses.scrollIntoView({block:'start',behavior:'auto'});};
 select.addEventListener('change',()=>open(select.value,1));
 reader.querySelector('[data-reader-form]').addEventListener('submit',event=>{event.preventDefault();if(!busy)open(select.value,ayah.value);});
 previous.addEventListener('click',()=>page(-1));next.addEventListener('click',()=>page(1));prevSurah.addEventListener('click',()=>open(activeSurah-1));nextSurah.addEventListener('click',()=>open(activeSurah+1));
 toggle.addEventListener('change',()=>reader.querySelectorAll('.verse-translation').forEach(node=>node.hidden=!toggle.checked));
 const resize=delta=>{size=Math.max(24,Math.min(48,size+delta));reader.style.setProperty('--quran-size',`${size}px`);reader.querySelector('[data-reader-size]').textContent=`${size}px`;reader.querySelector('[data-reader-smaller]').disabled=size===24;reader.querySelector('[data-reader-larger]').disabled=size===48;};
 reader.querySelector('[data-reader-smaller]').addEventListener('click',()=>resize(-4));reader.querySelector('[data-reader-larger]').addEventListener('click',()=>resize(4));
 resume.addEventListener('click',()=>{if(saved)open(saved.surah,saved.ayah);});reader.querySelector('[data-reader-retry]').addEventListener('click',()=>open(select.value,ayah.value));
 const query=new URLSearchParams(location.search);open(query.get('surah')||1,query.get('ayah')||1);
}

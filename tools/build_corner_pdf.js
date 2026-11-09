const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const l of fs.readFileSync('jobs.txt','utf8').trim().split('\n')){const [h,o]=l.split('\t');
await p.goto('file://'+path.resolve(h));await p.pdf({path:o,format:'A4',printBackground:true,displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style="font-size:8px;width:100%;text-align:center;color:#666"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',margin:{top:'18mm',bottom:'18mm',left:'16mm',right:'16mm'}});console.log(o);}
await b.close();})();

import http from 'k6/http';
import {check} from 'k6';
// Copiar los cuatro PDF oficiales con estos nombres y conservar sus hashes en el informe.
const pdfs = [open('./pdfs/1.pdf','b'),open('./pdfs/2.pdf','b'),open('./pdfs/3.pdf','b'),open('./pdfs/4.pdf','b')];
export const options={stages:[{duration:'10s',target:100},{duration:'20s',target:100},{duration:'10s',target:0}],thresholds:{http_req_failed:['rate==0']}};
export default function(){
  const response=http.post((__ENV.BASE_URL||'http://localhost:8081')+'/extract',pdfs[(__VU+__ITER)%4],{headers:{'Content-Type':'application/pdf'},timeout:'30s'});
  check(response,{'HTTP 200':r=>r.status===200,'contrato válido':r=>{try{const b=r.json();return typeof b.content==='string'&&Number.isInteger(b.page_count)}catch{return false}}});
}

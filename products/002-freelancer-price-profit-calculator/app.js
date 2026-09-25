const $=id=>document.getElementById(id);
const money=n=>new Intl.NumberFormat('en-IE',{style:'currency',currency:'EUR',maximumFractionDigits:2}).format(n);
function calculate(){
 const hours=+$('hours').value||0, rate=+$('rate').value||0, fee=(+$('fee').value||0)/100, tax=(+$('tax').value||0)/100, costs=+$('costs').value||0, discount=(+$('discount').value||0)/100;
 const base=hours*rate+costs, min=base*(1-discount), rec=Math.ceil((hours*rate+costs)/(1-fee)/(1-tax)/10)*10*(1-discount), prem=Math.ceil(rec*1.25/10)*10;
 const revenue=rec, feeAmt=revenue*fee, taxAmt=revenue*tax, profit=revenue-feeAmt-taxAmt-costs, margin=revenue?profit/revenue:0;
 [['minimum',min],['recommended',rec],['premium',prem],['revenue',revenue],['feeOut',-feeAmt],['costOut',-costs],['taxOut',-taxAmt],['profit',profit]].forEach(([id,v])=>$(id).textContent=money(v));
 $('margin').textContent=Math.round(margin*100)+'%'; $('effective').textContent=money(hours?profit/hours:0);
 $('donutProfit').textContent=Math.round(margin*100)+'%'; $('legendProfit').textContent=money(profit); $('legendTax').textContent=money(taxAmt); $('legendFee').textContent=money(feeAmt); $('legendCost').textContent=money(costs);
 $('bar1v').textContent=money(min);$('bar2v').textContent=money(rec);$('bar3v').textContent=money(prem);
 const max=Math.max(min,rec,prem)||1; $('bar1').style.height=(min/max*100)+'%';$('bar2').style.height=(rec/max*100)+'%';$('bar3').style.height=(prem/max*100)+'%';
 $('quoteTotal').textContent=money(rec);$('quoteTotal2').textContent=money(rec);$('quoteProject').textContent=$('projectName').value||'Project';
 $('miniRev').textContent=money(revenue);$('miniDeductions').textContent='− '+money(feeAmt+taxAmt);$('miniProfit').textContent=money(profit);
 $('profitRevenue').textContent=money(revenue);$('profitFees').textContent=money(feeAmt);$('profitTax').textContent=money(taxAmt);$('profitNet').textContent=money(profit);
 const rows=[['Minimum',hours,min],['Recommended',hours,rec],['Premium',hours,prem]];
 $('scenarioBody').innerHTML=rows.map(r=>{const p=r[2]*(1-fee-tax)-costs;return '<tr><td>'+r[0]+'</td><td>'+r[1]+'</td><td>'+money(r[2])+'</td><td>'+money(p)+'</td><td>'+Math.round((p/r[2])*100)+'%</td></tr>'}).join('');
}
document.querySelectorAll('.nav,.module').forEach(el=>el.addEventListener('click',()=>{const target=el.dataset.target;if(!target)return;document.querySelectorAll('.view').forEach(v=>v.classList.remove('active-view'));$(target).classList.add('active-view');document.querySelectorAll('.nav').forEach(n=>n.classList.remove('active'));const n=document.querySelector('.nav[data-target="'+target+'"]');if(n)n.classList.add('active');window.scrollTo({top:0,behavior:'smooth'});}));
document.querySelectorAll('#projectName,#hours,#rate,#revisions,#fee,#tax,#costs,#discount').forEach(el=>el.addEventListener('input',calculate));
calculate();
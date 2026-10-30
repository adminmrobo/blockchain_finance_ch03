LAB.start({anchor:'D',init:function(){
function attackerSuccess(q,z){var p=1.0-q;if(p<=q)return 1;var lambda=z*(q/p),sum=1.0,i,k;for(k=0;k<=z;k++){var poisson=Math.exp(-lambda);for(i=1;i<=k;i++)poisson*=lambda/i;sum-=poisson*(1-Math.pow(q/p,z-k));}return Math.max(0,Math.min(1,sum));}
function sig(v){return v>=1?'1':v>=1e-7?v.toFixed(7):v.toExponential(2);}
function sgn(v){return (v>0?'+':v<0?'−':'')+Math.abs(v);}
function cost(power,equip){return power*1+equip;}
function sim(pf,rg){var H=[];for(var i=0;i<40;i++)H.push({k:'home',h:1,c:1.6+0.02*i});[8,6,4].forEach(function(h,j){H.push({k:'farm',n:'채굴장 '+'ABC'[j],h:h,c:cost(pf,0.8)});});
  var R=150,out=[];for(var y=1;y<=10;y++){var tot=H.reduce(function(a,b){return a+b.h},0),r=R/tot;
    out.push({y:y,tot:tot,r:r,home:H.filter(function(m){return m.k==='home'}).reduce(function(a,b){return a+b.h},0)/tot,alive:H.filter(function(m){return m.k==='home'&&m.h>0}).length,
      shares:H.filter(function(m){return m.h>0}).map(function(m){return m.h/tot}).sort(function(a,b){return b-a}),farms:H.filter(function(m){return m.k==='farm'}).map(function(m){return m.h/tot})});
    H.forEach(function(m){var p=m.h*(r-m.c);if(m.k==='home'){if(p<0)m.h=0;}else if(p>0)m.h+=0.5*p/0.8;});R*=1+rg/100;}
  return out;}
function minCol(sh){var s=0;for(var i=0;i<sh.length;i++){s+=sh[i];if(s>0.5)return i+1;}return sh.length;}
var PF=0.5,RG=-5,OUT=sim(PF,RG),FC=[C.robo,C.info,C.stain];

/* ① */
(function(){var c1=$('#c1'),c1b=$('#c1b'),t=0;
  slider('r1p',function(v){PF=v/100;OUT=sim(PF,RG);upd();window.__p2upd&&window.__p2upd();},function(v){return (v/100).toFixed(1)});
  slider('r1r',function(v){RG=v;OUT=sim(PF,RG);upd();window.__p2upd&&window.__p2upd();},sgn);
  function drawA(){var W=fit(c1,230),H=230,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=40,B=H-34,T=26,bw=(W-L-20)/10;
    [0,0.5,1].forEach(function(g){var y=B-(B-T)*g;txt(x,Math.round(g*100)+'%',L-6,y+4,{a:'right',s:10,c:C.muted});});
    x.strokeStyle=C.amber;x.setLineDash([4,3]);x.beginPath();x.moveTo(L,B-(B-T)*0.5);x.lineTo(W-16,B-(B-T)*0.5);x.stroke();x.setLineDash([]);
    OUT.forEach(function(o,i){var X=L+i*bw+4,y=B,segs=[[o.home,C.fly]].concat(o.farms.map(function(f,j){return [f,FC[j]]}));
      segs.forEach(function(s){var h=(B-T)*s[0];x.fillStyle=s[1];x.fillRect(X,y-h,bw-8,h);y-=h;});txt(x,o.y+'년',X+(bw-8)/2,H-16,{a:'center',s:10,c:C.muted});});
    txt(x,'■ 집 채굴자',L,16,{s:11,c:C.fly,w:700});['A','B','C'].forEach(function(n,j){txt(x,'■ 채굴장 '+n,L+90+j*80,16,{s:11,c:FC[j],w:700});});
    stamp(x,W,'예시값');}
  function drawB(dt){t+=dt;var W=fit(c1b,150),H=150,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var yr=REDUCE?9:Math.floor(t*0.8)%10,o=OUT[yr],L=12,cols=20,cw=Math.min(16,(W*0.5-L)/cols);
    for(var i=0;i<40;i++){var on=i<o.alive,X=L+(i%cols)*cw,Y=40+Math.floor(i/cols)*20;x.fillStyle=on?C.amber:'#3a3d55';rr(x,X,Y,cw-4,14,2);x.fill();}
    txt(x,'집 채굴기 '+o.alive+'/40대 켜짐',L,H-14,{s:12,c:C.muted});
    var FX=W*0.55;o.farms.forEach(function(f,j){var n=Math.round(f*o.tot),Y=36+j*34;txt(x,'채굴장 '+'ABC'[j],FX,Y+12,{s:11,c:FC[j],w:700});for(var k=0;k<Math.min(n,40);k++){x.fillStyle=FC[j];rr(x,FX+70+k*((W-FX-90)/40),Y+2,(W-FX-90)/40-1,14,1);x.fill();}txt(x,n+'대',W-14,Y+12,{a:'right',s:11});});
    txt(x,(yr+1)+'년째',W-14,H-14,{a:'right',s:12,w:700});stamp(x,W,'설명용 장면');}
  function upd(){var a=OUT[0],z=OUT[9];
    kpis($('#k1'),[[Math.round(a.home*100)+'% → '+Math.round(z.home*100)+'%','집 채굴자의 계산력 몫 (1년 → 10년)','r'],[z.alive+'/40','10년째 남은 집 채굴자',z.alive?'a':'r'],[minCol(a.shares)+' → '+minCol(z.shares)+'곳','과반에 필요한 최소 채굴자 수','m'],[cost(PF,0.8).toFixed(1)+' : 1.6~2.4','단가 채굴장 : 집','a']]);
    $('#eq1').innerHTML='대당 수익 r = <b>전체 보상</b> ÷ <em>전체 계산력</em> · 이익 = 장비 수 × (r − <i>단가</i>) · 단가 = 전기료 + 장비';
    var y5=OUT.filter(function(o){return o.home<0.5})[0];
    ins($('#ins1'),[['r','첫해 집 채굴자 몫은 '+Math.round(a.home*100)+'%였지만 10년째에는 '+Math.round(z.home*100)+'%예요.'+(y5?' '+y5.y+'년째부터 채굴장 몫이 절반을 넘었어요.':'')],['a','과반에 필요한 최소 채굴자 수는 '+minCol(a.shares)+'곳에서 '+minCol(z.shares)+'곳으로 줄었어요. 채굴장 전기료를 1.0까지 올려 보면 쏠림이 느려져요.']]);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);upd();})();

/* ② */
(function(){var c2=$('#c2'),c2b=$('#c2b'),dist='y10',k=2,t=0,race=null;
  $$('#lv2 [data-dist]').forEach(function(b){b.addEventListener('click',function(){dist=b.dataset.dist;press('#lv2 [data-dist]',b);newRace();upd();});});
  slider('r2k',function(v){k=v;newRace();upd();});
  function sh(){return (dist==='y1'?OUT[0]:OUT[9]).shares;}
  function q(){return sh().slice(0,k).reduce(function(a,b){return a+b},0);}
  function newRace(){var r=rng(302),a=0,h=0,s=[],qq=q();for(var i=0;i<40;i++){if(r()<qq)a++;else h++;s.push([h,a]);}race={s:s};t=0;}
  function drawA(){var W=fit(c2,230),H=230,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var s=sh(),n=Math.min(s.length,24),L=40,B=H-30,T=24,bw=Math.min(60,(W-L-20)/n),cum=0;
    [0,0.5,1].forEach(function(g){txt(x,Math.round(g*100)+'%',L-6,B-(B-T)*g+4,{a:'right',s:10,c:C.muted});});
    x.strokeStyle=C.amber;x.setLineDash([4,3]);x.beginPath();x.moveTo(L,B-(B-T)*0.5);x.lineTo(W-16,B-(B-T)*0.5);x.stroke();x.setLineDash([]);txt(x,'50%',W-16,B-(B-T)*0.5-5,{a:'right',s:10,c:C.amber});
    x.strokeStyle=C.text;x.beginPath();for(var i=0;i<n;i++){var v=s[i],X=L+i*bw;x.fillStyle=i<k?C.eye:C.gfp;x.fillRect(X+2,B-(B-T)*v,bw-4,(B-T)*v);cum+=v;var px=X+bw/2,py=B-(B-T)*cum;i?x.lineTo(px,py):x.moveTo(px,py);}x.stroke();
    if(s.length>n)txt(x,'… 외 '+(s.length-n)+'명',W-16,B+18,{a:'right',s:10,c:C.muted});txt(x,'막대: 채굴자별 몫 (큰 순서) · 선: 누적',L,H-8,{s:11,c:C.muted});stamp(x,W,'①의 모형 · 예시값');}
  function drawB(dt){t+=dt;var W=fit(c2b,150),H=150,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);if(!race)newRace();var n=REDUCE?40:Math.min(40,Math.floor(t*5)),st=n?race.s[n-1]:[0,0],L=130,cw=Math.min(16,(W-L-20)/40);
    [['나머지 (정직)',st[0],C.gfp,50],['상위 '+k+'곳 (담합)',st[1],C.eye,100]].forEach(function(r){txt(x,r[0],12,r[3]+5,{s:12,w:700,c:r[2]});for(var i=0;i<r[1];i++){x.fillStyle=r[2];rr(x,L+i*cw,r[3]-7,cw-3,14,2);x.fill();}txt(x,r[1]+'',L+r[1]*cw+6,r[3]+5,{s:11});});
    stamp(x,W,'설명용 장면 · 블록 40개');}
  function upd(){var qq=q(),P=attackerSuccess(qq,6),mc=minCol(sh());
    kpis($('#k2'),[[mc+'곳','과반에 필요한 최소 채굴자 수','r'],[(qq*100).toFixed(1)+'%','상위 '+k+'곳의 몫 q',qq>0.5?'r':'a'],[sig(P),'6블록을 기다린 뒤 공격 성공 확률',P>=1?'r':P<0.001?'g':'a'],[sh().length+'명','남아 있는 채굴자','m']]);
    $('#eq2').innerHTML='q = 상위 <b>'+k+'</b>곳 몫의 합 = <em>'+(qq*100).toFixed(1)+'%</em> → P(q, 6) = <i>'+sig(P)+'</i> (2-07의 백서 식)';
    ins($('#ins2'),[[qq>0.5?'r':'a',(dist==='y1'?'첫해':'10년째')+' 분포에서 상위 '+k+'곳이 손잡으면 몫은 '+(qq*100).toFixed(1)+'%, 6블록을 기다린 뒤 공격 성공 확률은 '+sig(P)+'.'+(qq>0.5?' 과반이라 기다려도 막을 수 없어요.':'')],['m','이 분포에서 과반에 필요한 최소 채굴자 수는 '+mc+'곳이에요.']]);drawA();}
  window.__p2upd=function(){newRace();upd();};mod(c2b,drawB,true);addEventListener('resize',upd);newRace();upd();})();

Duel({names:{fly:'초파리 (집 한 대)',robo:'Money-Robo (채굴장)'},higherIsBetter:false,drawMargin:0,
  run:function(){return {fly:cost(1.0,1.0),robo:cost(0.5,0.8)};},bar:function(v){return v/2.5;},fmt:function(v){return v.toFixed(1);},
  lesson:'규모가 클수록 계산 단가가 낮다. 그래서 계산력은 채굴장으로 모인다',
  say:function(r){return '계산력 한 단위의 연간 단가는 초파리 쪽 '+r.fly.toFixed(1)+', Money-Robo 쪽 '+r.robo.toFixed(1)+'이에요(예시 단위). 같은 보상을 받으면 단가가 낮은 쪽이 남아요.';}});
}});

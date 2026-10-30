LAB.start({anchor:'C',init:function(){
var NM=['A','B','C','D','E'],COL=[C.info,C.stain,C.amber,C.gfp,C.robo];
function shares(e){var o=(1-e)/4;return [o,o,o,o,e];}
function draw100(sh,seed,n){var r=rng(seed),w=sh.map(function(){return 0});for(var b=0;b<(n||100);b++){var u=r(),a=0;for(var i=0;i<sh.length;i++){a+=sh[i];if(u<a||i===sh.length-1){w[i]++;break;}}}return w;}
function energy(mode,n,blocks){return mode==='pow'?n*10*1*blocks:n*0.01*blocks;}

/* ① 두 가지 추첨 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),mode='pow',e=0.2,res=null,t=0,sd=0;
  $$('#lv1 [data-mode]').forEach(function(b){b.addEventListener('click',function(){mode=b.dataset.mode;press('#lv1 [data-mode]',b);upd();});});
  function run(){var sh=shares(e);res={pow:draw100(sh,31+sd,1000),pos:draw100(sh,32+sd,1000)};}
  slider('r1e',function(v){e=v/100;run();upd();});
  $('#b1Run').addEventListener('click',function(){sd+=2;run();upd();});run();
  function drawA(){var W=fit(c1,230),H=230,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var sh=shares(e),L=40,bw=(W-L-200)/5;
    txt(x,'만든 블록 (1,000개 중)',L,22,{s:12,c:C.muted});
    NM.forEach(function(n,i){var X=L+i*bw,base=H-40,sc=(base-50)/600;
      [['pow',0],['pos',1]].forEach(function(m){var v=res?res[m[0]][i]:0,h=Math.min(base-40,v*sc),xx=X+8+m[1]*(bw/2-6);x.globalAlpha=m[0]===mode?1:0.35;x.fillStyle=COL[i];rr(x,xx,base-h,bw/2-14,h,3);x.fill();x.globalAlpha=1;if(res)txt(x,v,xx+(bw/2-14)/2,base-h-5,{a:'center',s:11,w:700});});
      txt(x,n+' ('+Math.round(sh[i]*100)+'%)',X+bw/2,base+18,{a:'center',s:12,c:COL[i],w:700});});
    txt(x,'왼쪽 막대: 작업증명 · 오른쪽: 지분증명',L,H-6,{s:11,c:C.muted});
    var EX=W-170;txt(x,'쓴 에너지 (예시 단위)',EX,46,{s:12,c:C.muted});[['작업증명','pow',C.eye],['지분증명','pos',C.gfp]].forEach(function(r,i){var y=70+i*60,v=energy(r[1],5,1000),w=Math.max(3,140*Math.log10(1+v)/4);
      txt(x,r[0],EX,y,{s:12,w:700,c:r[2]});x.fillStyle=r[2];rr(x,EX,y+8,w,16,4);x.fill();txt(x,fmt(v),EX,y+42,{s:13,w:700});});
    stamp(x,W,'예시값 · 시드 '+(31+sd)+'·'+(32+sd));}
  function drawB(dt){t+=dt;var W=fit(c1b,150),H=150,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var on=REDUCE?0:t;
    if(mode==='pow'){for(var i=0;i<5;i++){var X=60+i*(W-120)/4,Y=78;x.fillStyle=C.panel2;rr(x,X-28,Y-28,56,56,8);x.fill();x.save();x.translate(X,Y);x.rotate(on*6+i);x.strokeStyle=COL[i];x.lineWidth=3;for(var k=0;k<3;k++){x.rotate(2.094);x.beginPath();x.moveTo(0,0);x.lineTo(0,-18);x.stroke();}x.restore();x.lineWidth=1;txt(x,NM[i],X,Y+44,{a:'center',s:11,c:COL[i]});}
      txt(x,'블록 하나마다 채굴기 다섯 대가 모두 돈다',12,20,{s:12,c:C.muted});}
    else{var cx=W/2,cy=78;x.fillStyle=C.panel2;rr(x,cx-60,cy-34,120,68,10);x.fill();txt(x,'추첨함',cx,cy-12,{a:'center',s:12,c:C.muted});var k=Math.floor(on*1.2)%5;
      x.fillStyle=COL[k];rr(x,cx-18,cy,36,22,4);x.fill();txt(x,NM[k],cx,cy+16,{a:'center',s:12,w:700,c:'#13141f'});
      for(var j=0;j<5;j++){var X2=60+j*(W-120)/4;if(Math.abs(X2-cx)<90)continue;x.globalAlpha=j===k?1:0.3;x.fillStyle=COL[j];x.beginPath();x.arc(X2,cy,12,0,7);x.fill();x.globalAlpha=1;}
      txt(x,'블록 하나마다 몫만큼 넣은 제비에서 한 장을 뽑는다',12,20,{s:12,c:C.muted});}
    stamp(x,W,'설명용 장면');}
  function upd(){var ep=energy('pow',5,1000),es=energy('pos',5,1000);
    kpis($('#k1'),[[Math.round(e*100)+'%','E의 몫 (계산력 = 지분)','a'],[res?res.pow[4]+'개':'—','E가 만든 블록 · 작업증명','m'],[res?res.pos[4]+'개':'—','E가 만든 블록 · 지분증명','m'],[fmt(ep)+' : '+fmt(es),'에너지 작업증명 : 지분증명','r']]);
    $('#eq1').innerHTML='뽑힐 확률(i) = <b>몫(i)</b> · 에너지: 작업증명 = <em>n</em> × 10분 × 블록 수, 지분증명 = <em>n</em> × <i>0.01</i> × 블록 수';
    var m=[];if(res)m.push(['g','E의 몫 '+Math.round(e*100)+'%에서 E가 만든 블록은 작업증명 '+res.pow[4]+'개, 지분증명 '+res.pos[4]+'개. 기대값 '+Math.round(e*1000)+'개에 두 방식 모두 가까워요.']);
    m.push(['a','에너지는 작업증명 '+fmt(ep)+'단위, 지분증명 '+fmt(es)+'단위(예시값). 블록을 쓰는 사람은 같아도 경쟁에 든 비용이 달라요.']);
    if(e>0.5)m.push(['r','E의 몫이 50%를 넘었어요. 어느 방식이든 한 참여자가 과반을 쥐면 사슬을 좌우할 수 있어요(2-07, 51% 공격).']);ins($('#ins1'),m);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);upd();})();

/* ② 비교표 다시 읽기 */
var CRIT=[['보안성',3,2],['에너지 효율성',1,2],['탈중앙화 정도',2,1.5],['확장성',1,2],['진입 장벽 (낮을수록 좋음)',1,1.5],['처리 속도',1,2],['51% 공격 비용',3,3],['환경 영향 (작을수록 좋음)',1,2]];
function score(w){var a=0,b=0;CRIT.forEach(function(c,i){a+=w[i]*c[1];b+=w[i]*c[2];});return [a,b];}
(function(){var c2=$('#c2'),c2b=$('#c2b'),w=CRIT.map(function(){return 1}),t=0,ang=0;
  var PRE={sec:[3,0,3,0,0,0,2,0],eco:[0,3,0,1,0,2,0,3],even:[1,1,1,1,1,1,1,1]};
  $('#w2').innerHTML=CRIT.map(function(c,i){return '<div class="group"><span class="glabel">'+c[0]+'</span><input type="range" id="rw'+i+'" min="0" max="3" step="1" value="1" aria-label="'+c[0]+' 가중치"><span class="val" id="vw'+i+'">1</span></div>'}).join('');
  CRIT.forEach(function(c,i){slider('rw'+i,function(v){w[i]=v;upd();});});
  $$('#lv2 [data-pre]').forEach(function(b){b.addEventListener('click',function(){w=PRE[b.dataset.pre].slice();w.forEach(function(v,i){$('#rw'+i).value=v;$('#vw'+i).textContent=v;});press('#lv2 [data-pre]',b);upd();});});
  function drawA(){var W=fit(c2,250),H=250,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=170,bw=(W-L-120)/2,mx=9;
    txt(x,'작업증명',L,20,{s:12,w:700,c:C.eye});txt(x,'지분증명',L+bw+40,20,{s:12,w:700,c:C.gfp});
    CRIT.forEach(function(c,i){var y=30+i*24;txt(x,c[0],12,y+14,{s:11,c:w[i]?C.text:C.muted});
      [[c[1],0,C.eye],[c[2],1,C.gfp]].forEach(function(r){var v=w[i]*r[0],X=L+r[1]*(bw+40);x.globalAlpha=w[i]?1:0.25;x.fillStyle=r[2];rr(x,X,y+3,Math.max(2,bw*v/mx),14,3);x.fill();x.globalAlpha=1;txt(x,v.toFixed(1),X+Math.max(2,bw*v/mx)+5,y+14,{s:10,c:C.muted});});});
    var s=score(w);txt(x,'합계 '+s[0].toFixed(1)+' 대 '+s[1].toFixed(1),12,H-8,{w:700,c:s[0]>s[1]?C.eye:s[1]>s[0]?C.gfp:C.amber});stamp(x,W,'교안 평가를 점수로 옮김');}
  function drawB(dt){t+=dt;var W=fit(c2b,170),H=170,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var s=score(w),tot=Math.max(1,s[0]+s[1]),target=Math.max(-0.35,Math.min(0.35,(s[1]-s[0])/tot*1.2));
    ang+=(target-ang)*(REDUCE?1:Math.min(1,dt*4));var cx=W/2,cy=60,L=Math.min(220,W*0.3);
    x.fillStyle=C.accent;rr(x,cx-6,cy,12,80,3);x.fill();rr(x,cx-40,cy+78,80,10,3);x.fill();
    x.save();x.translate(cx,cy);x.rotate(ang);x.strokeStyle=C.amber;x.lineWidth=4;x.beginPath();x.moveTo(-L,0);x.lineTo(L,0);x.stroke();x.lineWidth=1;x.restore();
    [[-1,'작업증명',C.eye,s[0]],[1,'지분증명',C.gfp,s[1]]].forEach(function(p){var px=cx+p[0]*L*Math.cos(ang),py=cy+p[0]*L*Math.sin(ang);x.fillStyle=p[2];rr(x,px-40,py+10,80,26,6);x.fill();txt(x,p[1]+' '+p[3].toFixed(1),px,py+28,{a:'center',s:11,w:700,c:'#13141f'});});
    stamp(x,W,'설명용 장면');}
  function upd(){var s=score(w),lead=s[0]>s[1]?'작업증명':s[1]>s[0]?'지분증명':'동점';
    kpis($('#k2'),[[s[0].toFixed(1),'작업증명 점수',s[0]>=s[1]?'g':'m'],[s[1].toFixed(1),'지분증명 점수',s[1]>=s[0]?'g':'m'],[lead,'앞선 쪽','a'],[w.reduce(function(a,b){return a+b},0)+'','가중치 합','m']]);
    $('#eq2').innerHTML='점수 = Σ <b>가중치</b>(기준) × <em>교안 평가 점수</em>(기준) · 매우 높음 3, 높음·빠름 2, 중간 1.5, 낮음·제한적·느림 1';
    var m=[[s[0]===s[1]?'a':'g','지금 가중치로는 '+(lead==='동점'?'두 방식이 동점이에요.':lead+'이 '+Math.max(s[0],s[1]).toFixed(1)+'점 대 '+Math.min(s[0],s[1]).toFixed(1)+'점으로 앞서요.')]];
    if(w[6]>0)m.push(['m','51% 공격 비용은 두 방식 모두 "매우 높음"(3점)이라 가중치를 올려도 차이가 생기지 않아요.']);
    ins($('#ins2'),m);drawA();}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

Duel({names:{fly:'초파리 (작업증명)',robo:'Money-Robo (지분증명)'},higherIsBetter:false,drawMargin:0,
  run:function(){return {fly:energy('pow',10,100),robo:energy('pos',10,100)};},bar:function(v){return Math.max(0.02,Math.log10(v)/5);},fmt:function(v){return fmt(v)+'단위';},
  lesson:'에너지만 보면 지분증명이 훨씬 적게 든다. 보안과 탈중앙화는 다른 저울에 올려야 한다',
  say:function(r){return '블록 100개에 쓴 에너지는 초파리 쪽 '+fmt(r.fly)+'단위, Money-Robo 쪽 '+fmt(r.robo)+'단위예요(예시 단위). 약 '+fmt(r.fly/r.robo)+'배 차이고, 막대는 로그 눈금이에요.';}});
}});

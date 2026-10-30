LAB.start({anchor:'D',init:function(){
function gauss(r){var u=Math.max(1e-9,r()),v=r();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}
function walk(sigma,k,seed){var r=rng(seed),P=[1],tag=1,re=[],del=[];for(var d=1;d<=30;d++){var ch=sigma*gauss(r),p=P[d-1]*(1+ch);P.push(p);
    if(Math.abs(ch)>0.03)del.push(d);if(Math.abs(p/tag-1)>k){re.push(d);tag=p;}}return {P:P,re:re,del:del};}

/* ① 변동성과 가격표 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),s=0.04,k=0.05,seed=44,W_,t=0;
  slider('r1s',function(v){s=v/1000;upd();},function(v){return (v/10).toFixed(1)});slider('r1k',function(v){k=v/100;upd();});
  $('#b1Seed').addEventListener('click',function(){seed+=11;upd();});
  function drawA(){var W=fit(c1,230),H=230,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=50,Rr=W-20,T=30,B=H-34,P=W_.P,lo=Math.min.apply(null,P),hi=Math.max.apply(null,P),pad=Math.max(0.02,(hi-lo)*0.1);lo-=pad;hi+=pad;
    function X(d){return L+(Rr-L)*d/30}function Y(v){return B-(B-T)*(v-lo)/(hi-lo)}
    W_.del.forEach(function(d){x.fillStyle='rgba(240,96,77,.15)';x.fillRect(X(d)-(Rr-L)/60,T,(Rr-L)/30,B-T);});
    x.strokeStyle=C.robo;x.lineWidth=2.5;x.beginPath();P.forEach(function(v,d){d?x.lineTo(X(d),Y(v)):x.moveTo(X(d),Y(v));});x.stroke();x.lineWidth=1;
    W_.re.forEach(function(d){x.fillStyle=C.amber;x.beginPath();x.arc(X(d),Y(P[d]),5,0,7);x.fill();});
    [lo+pad,(lo+hi)/2,hi-pad].forEach(function(v){txt(x,v.toFixed(2),L-6,Y(v)+4,{a:'right',s:10,c:C.muted});});
    [0,10,20,30].forEach(function(d){txt(x,d+'일',X(d),H-16,{a:'center',s:10,c:C.muted});});
    txt(x,'가격 지수 (첫날 = 1)',L,H-4,{s:10,c:C.muted});txt(x,'● 가격표 고친 날',L,18,{s:11,c:C.amber,w:700});txt(x,'▮ 거래가 미뤄진 날 (하루 3% 넘게 움직임)',L+110,18,{s:11,c:C.eye});stamp(x,W,'예시값 · 시드 '+seed);}
  function drawB(dt){t+=dt;var W=fit(c1b,150),H=150,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var d=REDUCE?30:1+Math.floor(t*2)%30,P=W_.P,ch=P[d]/P[d-1]-1,isRe=W_.re.indexOf(d)>=0,isDel=W_.del.indexOf(d)>=0;
    x.fillStyle=C.panel2;rr(x,W/2-120,40,240,70,10);x.fill();txt(x,'커피 한 잔',W/2,62,{a:'center',s:12,c:C.muted});
    var tags=W_.re.filter(function(r){return r<=d}),tagP=tags.length?P[tags[tags.length-1]]:1;txt(x,(0.0001/tagP).toFixed(6)+' (가격표)',W/2,92,{a:'center',s:16,w:700,c:isRe?C.amber:C.text});
    drawSprite(x,SPR.a,80,80,3);drawSprite(x,SPR.b,W-80,80,3);
    if(isDel)txt(x,ch>0?'오를 것 같아 손님이 내기를 미룸':'내릴 것 같아 주인이 받기를 꺼림',W/2,132,{a:'center',s:12,w:700,c:C.eye});else if(isRe)txt(x,'가격표를 고쳐 씀',W/2,132,{a:'center',s:12,w:700,c:C.amber});
    txt(x,d+'일째 · 하루 변화 '+(ch*100).toFixed(1)+'%',12,20,{s:12,c:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){W_=walk(s,k,seed);var cal=walk(0.001,k,seed);
    kpis($('#k1'),[[(s*100).toFixed(1)+'%','하루 변동 폭 (예시값)','a'],[W_.re.length+'번','30일 동안 가격표 고친 횟수',W_.re.length>3?'r':W_.re.length?'a':'g'],[W_.del.length+'일','거래가 미뤄진 날',W_.del.length?'r':'g'],[cal.re.length+'번','하루 0.1%일 때 고친 횟수 (비교)','m']]);
    $('#eq1').innerHTML='가격<sub>내일</sub> = 가격<sub>오늘</sub> × (1 + <b>'+(s*100).toFixed(1)+'%</b> × 난수) · 가격표 기준에서 <em>'+Math.round(k*100)+'%</em> 넘게 벗어나면 고침 · <i>3%</i> 넘게 움직인 날은 거래 미룸';
    ins($('#ins1'),[[W_.re.length>3?'r':'a','하루 변동 폭 '+(s*100).toFixed(1)+'%에서 30일 동안 가격표를 '+W_.re.length+'번 고쳤고, '+W_.del.length+'일은 거래가 미뤄졌어요.'],['m','같은 조건에서 하루 0.1%라면 '+cal.re.length+'번이에요. 값이 흔들리면 "가치의 척도"와 "교환의 매개"가 함께 흔들려요. 실제 가격 자료가 아닌 예시예요.']]);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);upd();})();

/* ② 두 견해 */
function btcSupply(year){var blocks=840000+year*52560,s=0,b=0,i=0;while(b<blocks&&i<34){var n=Math.min(210000,blocks-b);s+=n*Math.floor(5e9/Math.pow(2,i));b+=n;i++;}return s;}
(function(){var c2=$('#c2'),c2b=$('#c2b'),g=0.06,u=0.04,view='pro',t=0;
  slider('r2g',function(v){g=v/100;upd();});slider('r2u',function(v){u=v/100;upd();});
  $$('#lv2 [data-view]').forEach(function(b){b.addEventListener('click',function(){view=b.dataset.view;press('#lv2 [data-view]',b);upd();});});
  function drawA(){var W=fit(c2,230),H=230,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=50,Rr=W-110,T=30,B=H-34,yrs=20,b0=btcSupply(0),hi=Math.max(140,100*Math.pow(1+g+u,yrs));
    function X(y){return L+(Rr-L)*y/yrs}function Y(v){return B-(B-T)*(v-90)/(hi-90)}
    x.fillStyle='rgba(214,114,214,.15)';x.beginPath();for(var y=0;y<=yrs;y++)x.lineTo(X(y),Y(100*Math.pow(1+g+u,y)));for(var y2=yrs;y2>=0;y2--)x.lineTo(X(y2),Y(100*Math.pow(1+Math.max(0,g-u),y2)));x.fill();
    x.strokeStyle=C.stain;x.lineWidth=2;x.beginPath();for(var y3=0;y3<=yrs;y3++){var v=100*Math.pow(1+g,y3);y3?x.lineTo(X(y3),Y(v)):x.moveTo(X(y3),Y(v));}x.stroke();
    x.strokeStyle=C.amber;x.lineWidth=3.5;x.beginPath();for(var y4=0;y4<=yrs;y4++){var v2=100*btcSupply(y4)/b0;y4?x.lineTo(X(y4),Y(v2)):x.moveTo(X(y4),Y(v2));}x.stroke();x.lineWidth=1;
    txt(x,'비트코인 (규칙)',Rr+6,Y(100*btcSupply(yrs)/b0)+4,{s:11,w:700,c:C.amber});txt(x,'법정화폐 (시나리오)',Rr+6,Y(100*Math.pow(1+g,yrs))+4,{s:11,w:700,c:C.stain});
    [100,Math.round((100+hi)/2)].forEach(function(v){txt(x,v,L-6,Y(v)+4,{a:'right',s:10,c:C.muted});});[0,10,20].forEach(function(y){txt(x,(2024+y)+'',X(y),H-16,{a:'center',s:10,c:C.muted});});
    txt(x,'공급량 지수 (2024 = 100) · 띠: 정책 불확실성 범위',L,18,{s:11,c:C.muted});stamp(x,W,'법정화폐는 예시 시나리오');}
  function drawB(dt){t+=dt;var W=fit(c2b,170),H=170,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var P=[['실물화폐','효용가치',C.accent,true],['법정화폐','국가의 지불수단 보증',C.info,true],['비트코인',view==='pro'?'정해진 알고리즘 발행':'시장참여자의 평가뿐',C.amber,view==='pro']];
    P.forEach(function(p,i){var X=W*(0.17+i*0.33),top=40,hgt=p[3]?80:36;x.fillStyle=C.panel2;rr(x,X-70,22,140,22,4);x.fill();txt(x,p[0],X,38,{a:'center',s:12,w:700});
      x.fillStyle=p[2];x.globalAlpha=p[3]?0.9:0.35;rr(x,X-14,top+8,28,hgt,3);x.fill();x.globalAlpha=1;if(!p[3]){x.strokeStyle=C.eye;x.setLineDash([4,3]);x.strokeRect(X-14,top+8,28,80);x.setLineDash([]);}
      txt(x,p[1],X,H-14,{a:'center',s:11,c:p[3]?C.text:C.eye});});
    txt(x,view==='pro'?'인정하는 견해: 비트코인은 발행 규칙이 기둥':'비판하는 견해: 비트코인에는 효용·보증 기둥이 없다',12,14,{s:11,c:C.muted});stamp(x,W,'교안 p.38·40을 그림으로');}
  function upd(){var b0=btcSupply(0),b20=btcSupply(20),f20=Math.pow(1+g,20);
    kpis($('#k2'),[['+'+((b20/b0-1)*100).toFixed(1)+'%','비트코인 20년 공급 증가 (규칙대로)','g'],['+'+((f20-1)*100).toFixed(0)+'%','법정화폐 20년 공급 증가 (시나리오)','a'],['±'+Math.round(u*100)+'%p','시나리오의 정책 불확실성','m'],[view==='pro'?'인정':'비판','보고 있는 견해','m']]);
    $('#eq2').innerHTML='비트코인: 공급 = <b>반감기 규칙</b>(3-03) · 법정화폐: 공급 = 100 × (1 + <em>'+Math.round(g*100)+'%</em> ± <i>'+Math.round(u*100)+'%p</i>)<sup>년</sup>';
    var M=view==='pro'?['g','인정하는 견해: 굵은 노란 선은 2024년부터 20년 동안 '+((b20/b0-1)*100).toFixed(1)+'%만 늘고, 미리 정확히 그릴 수 있어요. 정책에 따라 갈라지는 띠가 없어요.']:['r','비판하는 견해: 발행이 예측 가능해도 값을 받치는 기둥이 문제예요. 실물화폐는 효용, 법정화폐는 국가 보증이 있지만 비트코인은 시장참여자의 평가뿐이라고 봐요.'];
    ins($('#ins2'),[M,['m','법정화폐 쪽 수치는 예시 시나리오예요. 이 페이지는 어느 견해가 맞는지 판정하지 않아요.']]);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

Duel({names:{fly:'초파리 (원화 가격표)',robo:'Money-Robo (비트코인 가격표)'},higherIsBetter:false,drawMargin:0,
  run:function(){return {fly:walk(0.001,0.05,44).re.length,robo:walk(0.04,0.05,44).re.length};},bar:function(v){return Math.max(0.01,v/15);},fmt:function(v){return v+'번';},
  lesson:'값이 크게 흔들리면 가격표를 자주 고쳐야 한다. 결제 수단으로서는 안정성이 먼저다',
  say:function(r){return '30일 동안 가격표를 고친 횟수는 초파리 쪽 '+r.fly+'번, Money-Robo 쪽 '+r.robo+'번이에요. 같은 시드, 다른 변동 폭(0.1% 대 4%, 예시값)이에요.';}});
}});

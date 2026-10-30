LAB.start({anchor:'D',init:function(){
/* ① 누가 무엇을 보나 */
var FIELDS=['이름','금액','시각','주소·계좌'];
var VIEW={bank:{public:[0,0,0,0],party:[1,1,1,0],third:[1,1,1,1]},btc:{public:[0,1,1,1],party:[0,1,1,1],third:[0,0,0,0]}};
var WHO={public:'아무나 (대중)',party:'거래 상대',third:'은행·중개자'};
(function(){var c1=$('#c1'),c1b=$('#c1b'),who='public',t=0;
  $$('#lv1 [data-who]').forEach(function(b){b.addEventListener('click',function(){who=b.dataset.who;press('#lv1 [data-who]',b);upd();});});
  function box(x,X,Y,w,label,col,hl){x.fillStyle=hl?col:C.panel2;rr(x,X,Y,w,34,6);x.fill();txt(x,label,X+w/2,Y+22,{a:'center',s:12,w:700,c:hl?'#13141f':C.text});}
  function arrow(x,a,b,Y,col){x.strokeStyle=col;x.lineWidth=2;x.beginPath();x.moveTo(a,Y);x.lineTo(b-6,Y);x.stroke();x.beginPath();x.moveTo(b-6,Y-5);x.lineTo(b,Y);x.lineTo(b-6,Y+5);x.fill();x.lineWidth=1;}
  function cut(x,X,Y){x.strokeStyle=C.eye;x.lineWidth=3;x.beginPath();x.moveTo(X-6,Y-14);x.lineTo(X+6,Y+14);x.stroke();x.lineWidth=1;}
  function drawA(){var W=fit(c1,230),H=230,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var w=Math.min(120,(W-80)/5.6),g=(W-20-5*w)/5,X=function(i){return 14+i*(w+g)};
    txt(x,'전통적 모델 (은행)',14,24,{s:12,w:700,c:C.muted});var Y1=40;
    box(x,X(0),Y1,w,'신원',C.amber,false);box(x,X(1),Y1,w,'거래',C.amber,false);box(x,X(2),Y1,w,'은행 (제3자)',C.info,who==='third');box(x,X(3),Y1,w,'거래 상대',C.gfp,who==='party');box(x,X(4),Y1,w,'대중',C.stain,who==='public');
    x.fillStyle=C.text;[0,1,2].forEach(function(i){arrow(x,X(i)+w,X(i+1),Y1+17,C.text);});cut(x,X(4)-g/2,Y1+17);
    txt(x,'비트코인 모델',14,120,{s:12,w:700,c:C.muted});var Y2=136;
    box(x,X(0),Y2,w,'신원',C.amber,false);box(x,X(1),Y2,w,'거래 (공개)',C.amber,false);box(x,X(3),Y2,w,'거래 상대',C.gfp,who==='party');box(x,X(4),Y2,w,'대중',C.stain,who==='public');
    cut(x,X(1)-g/2,Y2+17);x.fillStyle=C.text;arrow(x,X(1)+w,X(3),Y2+17,C.text);x.strokeStyle=C.text;x.beginPath();x.moveTo(X(3)+w,Y2+17);x.lineTo(X(4),Y2+17);x.stroke();
    if(who==='third')txt(x,'중개자 없음',X(2)+w/2,Y2+22,{a:'center',s:12,c:C.info});
    txt(x,'빨간 사선: 정보가 끊기는 곳',14,H-10,{s:11,c:C.eye});stamp(x,W,'백서 10절 그림을 단순화');}
  function drawB(dt){t+=dt;var W=fit(c1b,170),H=170,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    [['은행 모델','bank',W*0.04],['비트코인 모델','btc',W*0.52]].forEach(function(m){var X=m[2],w=W*0.44;x.fillStyle=C.panel2;rr(x,X,30,w,120,10);x.fill();txt(x,WHO[who]+'의 화면 — '+m[0],X+12,52,{s:12,w:700});
      FIELDS.forEach(function(f,i){var on=VIEW[m[1]][who][i],Y=76+i*18;txt(x,(on?'✓ ':'✗ ')+f,X+16,Y,{s:12,c:on?C.gfp:C.muted});
        if(on){var sample=[['홍길동'],['0.05 BTC'],['10:42'],[m[1]==='btc'?'bc1q…7f3a':'123-45-…']][i][0];txt(x,sample,X+w-14,Y,{a:'right',s:12,c:C.text});}});});
    stamp(x,W,'설명용 장면');}
  function upd(){var b=VIEW.bank[who].reduce(function(a,c){return a+c},0),c=VIEW.btc[who].reduce(function(a,c){return a+c},0);
    kpis($('#k1'),[[WHO[who],'보는 사람','a'],[b+'/4','은행 모델에서 보이는 항목','m'],[c+'/4','비트코인 모델에서 보이는 항목','m'],[VIEW.btc[who][0]?'보임':'안 보임','비트코인 모델에서 이름',VIEW.btc[who][0]?'r':'g']]);
    $('#eq1').innerHTML='은행: <b>내역을 감춤</b>(제3자까지만) · 비트코인: <em>내역 공개</em> + <i>신원 ↔ 주소 연결 끊기</i>';
    var M={public:['g','대중은 은행 모델에서 아무것도 못 보지만, 비트코인 모델에서는 금액·시각·주소를 봐요. 이름만 빠져 있어요.'],party:['a','거래 상대는 은행 모델에서 이름을 알 수 있지만, 비트코인 모델에서는 주소만 알아요. 상대가 따로 알려 준 정보(택배 주소 등)는 예외예요.'],third:['m','은행 모델에서 은행은 모든 것을 알아요. 비트코인 모델에는 그런 제3자가 없어요. 단 거래소 같은 중개자를 거치면 그 사업자가 아는 정보가 생겨요.']};
    ins($('#ins1'),[M[who]]);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);upd();})();

/* ② 묶이는 거래 */
function clusters(mode,m,seed){var n=20,par=[];for(var i=0;i<n;i++)par.push(mode==='reuse'?0:i);
  function f(a){while(par[a]!==a)a=par[a]=par[par[a]];return a;}var r=rng(seed),links=[];
  for(var k=0;k<m;k++){var c=2+Math.floor(r()*2),set=[];while(set.length<c){var a=Math.floor(r()*n);if(set.indexOf(a)<0)set.push(a);}links.push(set);if(mode!=='reuse')set.slice(1).forEach(function(b){par[f(b)]=f(set[0]);});}
  return {f:f,links:links};}
function exposed(mode,m,seed,leak){var C_=clusters(mode,m,seed),root=C_.f(leak),cnt=0;for(var i=0;i<20;i++)if(C_.f(i)===root)cnt++;return {cnt:cnt,C:C_};}
var DUEL_LEAK=clusters('fresh',4,35).links[0][0];
(function(){var c2=$('#c2'),c2b=$('#c2b'),mode='fresh',m=4,leak=DUEL_LEAK,t=0,ls=135;
  $$('#lv2 [data-mode]').forEach(function(b){b.addEventListener('click',function(){mode=b.dataset.mode;press('#lv2 [data-mode]',b);t=0;upd();});});
  slider('r2m',function(v){m=v;t=0;upd();});
  $('#b2Leak').addEventListener('click',function(){ls+=7;leak=Math.floor(rng(ls)()*20);t=0;upd();});
  function pos(i,W,H){var a=i/20*Math.PI*2-Math.PI/2;return [W/2+Math.cos(a)*Math.min(W*0.38,170),H/2+6+Math.sin(a)*(H/2-34)];}
  function drawA(){var W=fit(c2,250),H=250,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var E=exposed(mode,m,35,leak),root=E.C.f(leak);
    if(mode==='reuse'){var p=[W/2,H/2+6];for(var i=0;i<20;i++){var q=pos(i,W,H);x.strokeStyle='rgba(240,96,77,.5)';x.beginPath();x.moveTo(p[0],p[1]);x.lineTo(q[0],q[1]);x.stroke();}x.fillStyle=C.eye;x.beginPath();x.arc(p[0],p[1],14,0,7);x.fill();txt(x,'주소 1개',p[0],p[1]+32,{a:'center',s:11,w:700,c:C.eye});}
    else E.C.links.forEach(function(s){for(var j=1;j<s.length;j++){var a=pos(s[0],W,H),b=pos(s[j],W,H);x.strokeStyle=E.C.f(s[0])===root?C.eye:C.amber;x.lineWidth=2;x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke();x.lineWidth=1;}});
    for(var i2=0;i2<20;i2++){var q2=pos(i2,W,H),hit=E.C.f(i2)===root;x.fillStyle=hit?C.eye:C.gfp;x.beginPath();x.arc(q2[0],q2[1],i2===leak?10:7,0,7);x.fill();if(i2===leak)txt(x,'드러난 주소',q2[0],q2[1]-14,{a:'center',s:11,w:700,c:C.eye});}
    txt(x,'점: 받은 거래 20건의 주소 · 노란 선: 모아 쓰기로 묶임 · 빨강: 드러난 덩어리',12,H-8,{s:11,c:C.muted});stamp(x,W,'예시값 · 시드 35');}
  function drawB(dt){t+=dt;var W=fit(c2b,150),H=150,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var E=exposed(mode,m,35,leak),root=E.C.f(leak),idx=[],cw=(W-40)/20;
    for(var i=0;i<20;i++)if(E.C.f(i)===root)idx.push(i);var shown=REDUCE?idx.length:Math.min(idx.length,Math.floor(t*6)+1);
    for(var k=0;k<20;k++){var X=20+k*cw,hit=idx.indexOf(k),on=hit>=0&&hit<shown;x.fillStyle=on?C.eye:C.panel2;rr(x,X+2,50,cw-4,40,4);x.fill();txt(x,'받음 '+(k+1),X+cw/2,74,{a:'center',s:9,c:on?'#13141f':C.muted});}
    txt(x,'드러난 받은 거래: '+shown+' / 20건',20,H-16,{s:12,w:700,c:C.eye});stamp(x,W,'설명용 장면');}
  function upd(){var E=exposed(mode,m,35,leak),Ef=exposed('fresh',m,35,leak).cnt;
    kpis($('#k2'),[[mode==='reuse'?'1개':'20개','처음 주소 수','a'],[m+'번','여러 조각을 모아 쓴 횟수','m'],[E.cnt+'건','함께 드러나는 받은 거래',E.cnt>10?'r':E.cnt>1?'a':'g'],[Ef+' : 20','새 주소 : 재사용 (이 조건)','m']]);
    $('#eq2').innerHTML='드러나는 거래 = 드러난 주소가 속한 <b>덩어리의 크기</b> · 덩어리는 <em>재사용</em>과 <i>여러 입력 거래</i>로 커진다';
    var msg=mode==='reuse'?['r','주소 하나를 재사용하면 그 주소가 드러나는 순간 20건이 모두 드러나요.']:[E.cnt>1?'a':'g','거래마다 새 주소를 썼지만 모아 쓰기 '+m+'번으로 묶인 덩어리 때문에 '+E.cnt+'건이 함께 드러났어요.'];
    ins($('#ins2'),[msg,['m','모아 쓰기 횟수를 0으로 내리면 새 주소 쪽은 1건만 드러나요. 횟수를 늘릴수록 덩어리가 커져요.']]);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

Duel({names:{fly:'초파리 (거래마다 새 주소)',robo:'Money-Robo (주소 하나 재사용)'},higherIsBetter:false,drawMargin:0,
  run:function(){return {fly:exposed('fresh',4,35,DUEL_LEAK).cnt,robo:exposed('reuse',4,35,DUEL_LEAK).cnt};},bar:function(v){return v/20;},fmt:function(v){return v+'건';},
  lesson:'거래마다 새 주소를 쓰면 하나가 드러나도 피해가 덩어리 크기로 줄어든다',
  say:function(r){return '주소 하나가 드러났을 때 함께 드러난 받은 거래는 초파리 쪽 '+r.fly+'건, Money-Robo 쪽 '+r.robo+'건이에요. 초파리 쪽도 모아 쓰기로 묶인 만큼은 드러났어요.';}});
}});

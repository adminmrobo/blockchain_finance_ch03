LAB.start({anchor:'D',init:function(){
var FLOWS=(function(){var r=rng(37),F=[];for(var i=0;i<20;i++)F.push({len:1+Math.floor(r()*7),u:r()});return F;})();
function traced(h,p){return FLOWS.filter(function(f){return f.len<=h&&f.u<p}).length;}
function isCk(f,p){return f.u<p;}

/* ① 공개 장부 추적 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),h=6,p=0.7,t=0;
  slider('r1h',function(v){h=v;upd();});slider('r1p',function(v){p=v/100;upd();});
  function drawA(){var W=fit(c1,260),H=260,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=70,Rr=W-150,T=46,rowH=(H-T-24)/20;
    function X(k){return L+(Rr-L)*k/7}
    for(var k=0;k<=7;k++){txt(x,k+'홉',X(k),38,{a:'center',s:10,c:C.muted});}
    x.strokeStyle=C.amber;x.setLineDash([4,3]);x.beginPath();x.moveTo(X(h)+8,T-6);x.lineTo(X(h)+8,H-14);x.stroke();x.setLineDash([]);
    x.fillStyle=C.eye;x.beginPath();x.arc(L-34,T+10*rowH,10,0,7);x.fill();txt(x,'몸값',L-34,T+10*rowH+26,{a:'center',s:11,w:700,c:C.eye});
    FLOWS.forEach(function(f,i){var y=T+i*rowH+rowH/2,ok=f.len<=h&&isCk(f,p),seen=Math.min(f.len,h);
      x.strokeStyle='rgba(157,155,184,.35)';x.beginPath();x.moveTo(L-24,T+10*rowH);x.lineTo(X(0),y);x.lineTo(X(f.len),y);x.stroke();
      x.strokeStyle=ok?C.gfp:C.info;x.lineWidth=2;x.beginPath();x.moveTo(X(0),y);x.lineTo(X(seen),y);x.stroke();x.lineWidth=1;
      for(var k2=1;k2<f.len;k2++){x.fillStyle=k2<=h?C.info:'#3a3d55';x.beginPath();x.arc(X(k2),y,2.5,0,7);x.fill();}
      var ex=X(f.len);if(isCk(f,p)){x.fillStyle=f.len<=h?C.gfp:'rgba(94,227,156,.3)';rr(x,ex-6,y-5,12,10,2);x.fill();}else{x.fillStyle='#55587a';x.beginPath();x.arc(ex,y,4,0,7);x.fill();}});
    txt(x,'■ 확인 지점',Rr+24,T+30,{s:11,c:C.gfp});txt(x,'● 확인 안 된 지갑',Rr+24,T+48,{s:11,c:C.muted});txt(x,'점선: 따라간 범위',L,H-4,{s:10,c:C.amber});stamp(x,W,'모형 가정 · 시드 37');}
  function drawB(dt){t+=dt;var W=fit(c1b,150),H=150,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var f=FLOWS.filter(function(f){return f.len>=4})[0]||FLOWS[0],n=f.len,L=60,Rr=W-80,step=REDUCE?n:Math.min(n,Math.floor(t*1.2)%(n+3));
    for(var k=0;k<=n;k++){var X=L+(Rr-L)*k/n;x.fillStyle=k===0?C.eye:k===n?(isCk(f,p)?C.gfp:'#55587a'):C.panel2;rr(x,X-22,56,44,28,5);x.fill();
      txt(x,k===0?'몸값':k===n?(isCk(f,p)?'확인 지점':'지갑'):'주소 '+k,X,74,{a:'center',s:10,w:700,c:k===0||k===n?'#13141f':C.text});if(k<n){x.strokeStyle=C.muted;x.beginPath();x.moveTo(X+22,70);x.lineTo(L+(Rr-L)*(k+1)/n-22,70);x.stroke();}}
    var mx=L+(Rr-L)*Math.min(step,n)/n;x.strokeStyle=C.amber;x.lineWidth=3;x.beginPath();x.arc(mx,48,12,0,7);x.stroke();x.beginPath();x.moveTo(mx+8,56);x.lineTo(mx+16,66);x.stroke();x.lineWidth=1;
    txt(x,step>=n?(isCk(f,p)?'확인 지점에 닿음 → 사람과 연결':'확인 안 된 지갑에서 끝남'):'공개 장부에서 다음 거래를 찾는 중… ('+step+'/'+n+'홉)',12,H-14,{s:12,w:700,c:step>=n?(isCk(f,p)?C.gfp:C.muted):C.muted});stamp(x,W,'설명용 장면');}
  function upd(){var n=traced(h,p),all=FLOWS.filter(function(f){return isCk(f,p)}).length;
    kpis($('#k1'),[[h+'홉','따라간 최대 홉 수','a'],[n+'/20','신원까지 연결된 갈래',n>10?'g':'a'],[all+'/20','확인 지점에서 끝나는 갈래 (전체)','m'],[(20-all)+'갈래','끝까지 따라가도 남는 갈래','r']]);
    $('#eq1').innerHTML='연결된 갈래 = 길이 ≤ <b>'+h+'</b>홉 이고 끝이 <em>확인 지점</em>(비율 '+Math.round(p*100)+'%)인 갈래';
    ins($('#ins1'),[[n?'g':'a','공개 장부를 '+h+'홉까지 따라가니 20갈래 중 '+n+'갈래가 신원 확인 지점에 닿았어요.'],['m','확인 지점에 닿지 않고 끝나는 '+(20-all)+'갈래는 몇 홉을 따라가도 사람과 연결되지 않아요. 모두 모형 가정이에요.']]);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);upd();})();

/* ② 국경과 규제 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),exit='yes',n=3,t=0;
  $$('#lv2 [data-exit]').forEach(function(b){b.addEventListener('click',function(){exit=b.dataset.exit;press('#lv2 [data-exit]',b);upd();});});
  slider('r2n',function(v){n=v;upd();});
  function route(){var bank=[['보내는 사람',0],['송금 은행',1],['국제 송금 심사',1],['받는 은행',1],['받는 사람',0]],dir=[['보내는 지갑',0]];for(var i=0;i<n;i++)dir.push(['지갑 '+(i+1),0]);if(exit==='yes')dir.push(['현금화 창구',1]);dir.push(['받는 사람',0]);return {bank:bank,dir:dir};}
  function drawA(){var W=fit(c2,220),H=220,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var R=route();
    [['은행 해외 송금',R.bank,60,'약 1~3일 (예시값)'],['지갑 간 직접 이체',R.dir,150,'약 1시간 (6블록 확정, 2-07)']].forEach(function(row){txt(x,row[0]+' · '+row[3],14,row[2]-26,{s:12,w:700,c:C.muted});var m=row[1].length,bw=Math.min(110,(W-40)/m-10);
      row[1].forEach(function(s,i){var X=14+i*((W-28)/m);x.fillStyle=s[1]?C.amber:C.panel2;rr(x,X,row[2]-12,bw,30,6);x.fill();txt(x,s[0],X+bw/2,row[2]+7,{a:'center',s:10,w:700,c:s[1]?'#13141f':C.text});
        if(i<m-1){x.strokeStyle=C.muted;x.beginPath();x.moveTo(X+bw,row[2]+3);x.lineTo(14+(i+1)*((W-28)/m),row[2]+3);x.stroke();}});});
    txt(x,'노란 칸: 신원 확인 지점 (모형 가정)',14,H-8,{s:11,c:C.amber});stamp(x,W,'모형 가정');}
  function drawB(dt){t+=dt;var W=fit(c2b,150),H=150,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var R=route();
    [[R.bank,50,0.25],[R.dir,110,1.2]].forEach(function(row){var m=row[0].length,ph=REDUCE?m-1:(t*row[2])%(m-1+0.999),i=Math.floor(ph),f=ph-i,stop=row[0][Math.min(m-1,i+1)][1]&&f>0.6;
      row[0].forEach(function(s,k){var X=30+k*((W-60)/(m-1));x.fillStyle=s[1]?C.amber:C.panel2;x.beginPath();x.arc(X,row[1],s[1]?9:5,0,7);x.fill();});
      var X0=30+i*((W-60)/(m-1)),X1=30+Math.min(m-1,i+1)*((W-60)/(m-1));coin(x,X0+(X1-X0)*(stop?0.85:f),row[1]-14,6);});
    txt(x,'위: 은행 송금 (창구마다 확인) · 아래: 직접 이체',12,20,{s:12,c:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){var R=route(),cb=R.bank.filter(function(s){return s[1]}).length,cd=R.dir.filter(function(s){return s[1]}).length;
    kpis($('#k2'),[[cb+'곳','은행 해외 송금의 확인 지점','g'],[cd+'곳','직접 이체의 확인 지점',cd?'a':'r'],[n+'개','거쳐 가는 지갑','m'],[exit==='yes'?'가능':'없음','장부를 거슬러 올라갈 연결 지점',exit==='yes'?'g':'r']]);
    $('#eq2').innerHTML='확인 지점: 은행 경로 <b>'+cb+'</b>곳 · 직접 이체 <em>'+cd+'</em>곳 (거쳐 가는 지갑 수와 무관)';
    ins($('#ins2'),[[cd?'a':'r',exit==='yes'?'직접 이체는 지갑 '+n+'개를 거쳐도 확인 지점이 없다가, 현금화 창구에서 1곳이 생겨요. 거기서 공개 장부를 거슬러 올라가 앞선 이동을 이어 볼 수 있어요(①칸).':'현금화 창구를 거치지 않으면 확인 지점이 하나도 없어요. 교안이 말한 "규제 우회"예요.'],['m','확인 지점의 수와 시간은 모형 가정이에요. 실제 절차는 나라와 사업자마다 달라요.']]);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

Duel({names:{fly:'초파리 (6홉까지 추적)',robo:'주판봇 (바로 연결된 것만)'},higherIsBetter:true,drawMargin:0,
  run:function(){return {fly:traced(6,0.7),robo:traced(1,0.7)};},bar:function(v){return Math.max(0.01,v/20);},fmt:function(v){return v+'갈래';},
  lesson:'주소에 이름이 없어도 공개 장부의 길은 남는다. 끝까지 따라가면 신원 확인 지점에 닿는다',
  say:function(r){return '신원 확인 지점까지 연결된 갈래는 초파리 쪽 '+r.fly+'갈래, 주판봇 쪽 '+r.robo+'갈래예요. 같은 20갈래, 같은 확인 지점 비율(모형 가정)이에요.';}});
}});

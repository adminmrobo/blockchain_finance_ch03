LAB.start({anchor:'C',init:function(){
function subsidySat(i){return i>63?0:Math.floor(5e9/Math.pow(2,i));}
function cumSat(n){var s=0;for(var i=0;i<n;i++)s+=210000*subsidySat(i);return s;}
var TOTAL=cumSat(34);
function btc(s){return s/1e8;}
function fb(v,d){return v.toLocaleString('ko-KR',{minimumFractionDigits:d||0,maximumFractionDigits:d==null?8:d});}
function year(i){return i===4?'2024년 4월':i===0?'2009년':'약 '+(2009+4*i)+'년';}

/* ① 반감기와 한도 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),ep=4,unit='btc',t=0;
  slider('r1e',function(v){ep=v;upd();});
  $$('#lv1 [data-u]').forEach(function(b){b.addEventListener('click',function(){unit=b.dataset.u;press('#lv1 [data-u]',b);upd();});});
  function drawA(){var W=fit(c1,240),H=240,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=56,Rr=W-56,T=40,B=H-34,n=34;
    function X(i){return L+(Rr-L)*i/n}function Ys(v){return B-(B-T)*v/50}function Yc(v){return B-(B-T)*v/21e6}
    x.strokeStyle=C.amber;x.setLineDash([4,3]);x.beginPath();x.moveTo(L,Yc(21e6));x.lineTo(Rr,Yc(21e6));x.stroke();x.setLineDash([]);txt(x,'상한 2,100만',L+(Rr-L)*0.45,Yc(21e6)-6,{s:10,c:C.amber});
    for(var i=0;i<n;i++){var s=btc(subsidySat(i));x.fillStyle=i===ep?C.robo:'rgba(130,184,255,.45)';x.fillRect(X(i)+1,Ys(s),(Rr-L)/n-2,B-Ys(s));}
    x.strokeStyle=C.gfp;x.lineWidth=2.5;x.beginPath();for(var j=0;j<=n;j++){var px=X(j),py=Yc(btc(cumSat(j)));j?x.lineTo(px,py):x.moveTo(px,py);}x.stroke();x.lineWidth=1;
    x.fillStyle=C.gfp;x.beginPath();x.arc(X(ep),Yc(btc(cumSat(ep))),5,0,7);x.fill();
    [0,25,50].forEach(function(v){txt(x,v,L-6,Ys(v)+4,{a:'right',s:10,c:C.info});});txt(x,'보상 BTC',L-6,T-10,{a:'right',s:10,c:C.info});
    [0,1e7,2e7].forEach(function(v){txt(x,v/1e4+'만',Rr+4,Yc(v)+4,{s:10,c:C.gfp});});
    [0,4,8,16,24,33].forEach(function(i){txt(x,i+'',X(i)+(Rr-L)/n/2,H-16,{a:'center',s:10,c:C.muted});});txt(x,'반감기',L,H-4,{s:10,c:C.muted});
    stamp(x,W,'규칙대로 계산');}
  function drawB(dt){t+=dt;var W=fit(c1b,150),H=150,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var s=btc(subsidySat(ep)),r=Math.max(1.5,14*Math.sqrt(s/50));
    for(var k=0;k<8;k++){var X=60+k*(W-120)/7;x.fillStyle=C.panel2;rr(x,X-20,100,40,24,4);x.fill();txt(x,'블록',X,116,{a:'center',s:10,c:C.muted});
      var ph=REDUCE?1:((t*0.7+k*0.125)%1),y=30+ph*58;if(s>0)coin(x,X,y,r);}
    txt(x,'반감기 '+ep+'번째: 블록마다 '+fb(s)+' BTC',12,20,{s:12,c:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){var s=subsidySat(ep),cum=cumSat(ep);
    kpis($('#k1'),[[unit==='btc'?fb(btc(s))+' BTC':fmt(s)+' 사토시','반감기 '+ep+'번째 블록 보상 ('+year(ep)+')','a'],[(100*cum/TOTAL).toFixed(2)+'%','이 시기 시작까지 누적 발행 비율','m'],[unit==='btc'?fb(btc(TOTAL),4)+' BTC':fmt(TOTAL)+' 사토시','33번째까지 더한 총 발행량','g'],[fb(21e6-btc(TOTAL),4)+' BTC','2,100만과의 차이','r']]);
    $('#eq1').innerHTML='보상(<b>'+ep+'</b>) = ⌊5,000,000,000 ÷ 2<sup>'+ep+'</sup>⌋ = <em>'+fmt(s)+'</em> 사토시 · 총량 = Σ 210,000 × 보상(i) = <i>'+fmt(TOTAL)+'</i> 사토시';
    var m=[];if(ep===4)m.push(['g','4번째 반감기(2024년 4월, 블록 840,000)에 보상은 3.125 BTC가 되었어요. 이때까지 총량의 '+(100*cum/TOTAL).toFixed(2)+'%가 발행되었어요.']);
    else if(s===0)m.push(['r',ep+'번째 반감기부터 보상은 0사토시예요. 새 코인 발행이 끝나요.']);
    else if(s<100)m.push(['a','보상이 '+s+'사토시까지 줄었어요. 정수로 나누니 다음 시기에는 끝자리가 잘려요.']);
    else m.push(['m','반감기 '+ep+'번째('+year(ep)+')의 보상은 '+fb(btc(s))+' BTC, 이 시기 시작까지 누적 '+(100*cum/TOTAL).toFixed(2)+'%.']);
    m.push(['a','끝까지 더하면 '+fb(btc(TOTAL),4)+' BTC. 교안의 "2,100만"보다 '+fb(21e6-btc(TOTAL),4)+' BTC 적어요.']);ins($('#ins1'),m);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);upd();})();

/* ② 보상에서 수수료로 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),fee=0.5,t=0;
  slider('r2f',function(v){fee=v/10;upd();},function(v){return (v/10).toFixed(1)});
  function cross(){for(var i=0;i<34;i++)if(fee>btc(subsidySat(i)))return i;return -1;}
  function drawA(){var W=fit(c2,230),H=230,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=50,B=H-34,T=44,n=12,bw=(W-L-20)/n,mx=52;
    function Y(v){return B-(B-T)*Math.min(v,mx)/mx}
    [0,25,50].forEach(function(v){txt(x,v,L-6,Y(v)+4,{a:'right',s:10,c:C.muted});});
    for(var i=0;i<n;i++){var s=btc(subsidySat(i)),X=L+i*bw+4;x.fillStyle=C.amber;x.fillRect(X,Y(s),bw-8,B-Y(s));x.fillStyle=C.stain;x.fillRect(X,Y(s+fee),bw-8,Y(s)-Y(s+fee));
      var sh=fee/(s+fee);txt(x,Math.round(sh*100)+'%',X+(bw-8)/2,Y(s+fee)-5,{a:'center',s:10,c:sh>0.5?C.stain:C.muted});txt(x,i+'',X+(bw-8)/2,H-16,{a:'center',s:10,c:C.muted});}
    txt(x,'■ 새 코인',L,16,{s:11,c:C.amber,w:700});txt(x,'■ 수수료',L+80,16,{s:11,c:C.stain,w:700});txt(x,'막대 위: 수수료 몫',L+160,16,{s:11,c:C.muted});txt(x,'반감기',L,H-4,{s:10,c:C.muted});
    stamp(x,W,'수수료는 예시값');}
  function drawB(dt){t+=dt;var W=fit(c2b,170),H=170,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var i=REDUCE?8:Math.floor(t*0.8)%12,s=btc(subsidySat(i)),tot=s+fee,mx=50+fee;
    [['새 코인',s,C.amber,W*0.3],['수수료',fee,C.stain,W*0.7]].forEach(function(p){var r=Math.max(4,46*Math.sqrt(p[1]/mx));x.fillStyle=p[2];x.globalAlpha=0.85;x.beginPath();x.arc(p[3],84,r,0,7);x.fill();x.globalAlpha=1;
      txt(x,p[0]+' '+fb(p[1],3),p[3],146,{a:'center',s:12,w:700,c:p[2]});});
    txt(x,'반감기 '+i+'번째 · 수수료 몫 '+Math.round(100*fee/tot)+'%',12,20,{s:12,c:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){var c=cross(),s4=btc(subsidySat(4));
    kpis($('#k2'),[[fb(fee,1)+' BTC','블록당 수수료 (예시값)','a'],[Math.round(100*fee/(s4+fee))+'%','4번째 반감기 시기의 수수료 몫','m'],[c>=0?c+'번째':'—','수수료가 새 코인보다 처음 커지는 반감기','g'],[c>=0?year(c):'—','그 시기 (어림)','m']]);
    $('#eq2').innerHTML='블록 수입 = <b>새 코인</b>(반감기마다 절반) + <em>수수료</em>(입력 합 − 출력 합) · 수수료 몫 = 수수료 ÷ 수입';
    var m=[];if(fee===0)m.push(['r','수수료가 0이면 33번째 반감기 뒤 블록 수입도 0이에요. 채굴할 이유가 사라져요.']);
    else m.push(['g','블록당 수수료 '+fb(fee,1)+' BTC라면 '+c+'번째 반감기('+year(c)+')부터 수수료가 새 코인보다 커져요.']);
    m.push(['a','이 모형은 수수료를 시기와 관계없이 같다고 둬요. 실제 수수료는 거래 수요에 따라 오르내려요.']);ins($('#ins2'),m);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

Duel({names:{fly:'초파리 (사토시까지 더하기)',robo:'Money-Robo (2,100만 어림)'},higherIsBetter:false,drawMargin:0.1,
  run:function(){var exact=btc(TOTAL);return {fly:Math.abs(exact-exact),robo:Math.abs(21e6-exact)};},bar:function(v){return Math.min(1,v/0.1);},fmt:function(v){return fb(v,4)+' BTC';},
  lesson:'2,100만은 규칙을 더한 값의 어림이다. 정확한 값과 0.0231 BTC 차이',
  say:function(r,res){return '실제 합계와의 차이는 초파리 쪽 '+fb(r.fly,4)+' BTC, Money-Robo 쪽 '+fb(r.robo,4)+' BTC예요. 차이가 0.1 BTC 기준 안이라 '+(res==='D'?'무승부예요.':'승패가 갈렸어요.');}});
}});

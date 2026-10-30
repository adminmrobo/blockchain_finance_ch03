LAB.start({anchor:'C',init:function(){
var FEE=0.001,INIT=[0.5,0.3,0.15,0.05];
function r3(v){return Math.round(v*1000)/1000;}
function pick(coins,amt,mode){var order=coins.map(function(c,i){return i}).sort(function(a,b){return mode==='big'?coins[b].v-coins[a].v:coins[a].v-coins[b].v}),sel=[],s=0;
  for(var k=0;k<order.length&&s<amt+FEE-1e-9;k++){sel.push(order[k]);s+=coins[order[k]].v;}return s>=amt+FEE-1e-9?{sel:sel,sum:r3(s)}:null;}
function bf(v,d){return v.toFixed(d==null?3:d);}

/* ① 조각으로 된 잔액 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),W0,amt=0.7,mode='big',last=null,t=0,n=0;
  function reset(){W0=INIT.map(function(v,i){return {v:v,id:'조각 '+(i+1)}});last=null;n=0;upd();}
  slider('r1a',function(v){amt=v*0.05;upd();},function(v){return (v*0.05).toFixed(2)});
  $$('#lv1 [data-pick]').forEach(function(b){b.addEventListener('click',function(){mode=b.dataset.pick;press('#lv1 [data-pick]',b);upd();});});
  $('#b1Send').addEventListener('click',function(){var p=pick(W0,amt,mode);if(!p){last={fail:true};upd();return;}n++;
    var ins_=p.sel.map(function(i){return W0[i]}),change=r3(p.sum-amt-FEE),keep=W0.filter(function(c,i){return p.sel.indexOf(i)<0});
    last={ins:ins_,pay:r3(amt),change:change,sum:p.sum};if(change>0)keep.push({v:change,id:'거스름 '+n,ch:true});W0=keep;t=0;upd();});
  $('#b1Reset').addEventListener('click',reset);
  function bal(){return r3(W0.reduce(function(a,c){return a+c.v},0));}
  function drawA(){var W=fit(c1,230),H=230,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    txt(x,'입력 (쓴 조각)',20,22,{s:12,c:C.muted});txt(x,'출력 (새 조각)',W*0.62,22,{s:12,c:C.muted});
    if(!last||last.fail){txt(x,last&&last.fail?'잔액이 모자라 보낼 수 없어요 (잔액 '+bf(bal())+' BTC)':'"보내기"를 눌러 보세요',20,H/2,{s:13,c:last?C.eye:C.muted});
      txt(x,'지갑: '+W0.map(function(c){return bf(c.v)}).join(' · ')+' BTC',20,H-14,{s:12});stamp(x,W,'예시값');return;}
    var bw=Math.min(180,W*0.28),cx=W*0.45;last.ins.forEach(function(c,i){var y=40+i*44;x.fillStyle='#efe6d2';rr(x,20,y,bw,34,6);x.fill();txt(x,c.id+'  '+bf(c.v)+' BTC',30,y+22,{s:12,w:700,c:'#3a3040'});
      x.strokeStyle=C.amber;x.beginPath();x.moveTo(20+bw,y+17);x.lineTo(cx-30,H/2-10);x.stroke();});
    x.fillStyle=C.panel2;rr(x,cx-30,H/2-40,60,60,8);x.fill();txt(x,'거래',cx,H/2-6,{a:'center',s:12,w:700});
    var outs=[['받는 사람',last.pay,C.gfp]];if(last.change>0)outs.push(['거스름돈 (나)',last.change,C.info]);
    outs.forEach(function(o,i){var y=50+i*60,X=W*0.62;x.strokeStyle=o[2];x.beginPath();x.moveTo(cx+30,H/2-10);x.lineTo(X,y+17);x.stroke();x.fillStyle=o[2];rr(x,X,y,bw,34,6);x.fill();txt(x,o[0]+'  '+bf(o[1])+' BTC',X+10,y+22,{s:12,w:700,c:'#13141f'});});
    txt(x,'수수료 '+bf(FEE)+' BTC = 입력 '+bf(last.sum)+' − 출력 '+bf(r3(last.pay+last.change)),W*0.62,H-40,{s:11,c:C.stain});
    txt(x,'지갑: '+W0.map(function(c){return bf(c.v)}).join(' · ')+' BTC',20,H-14,{s:12});stamp(x,W,'예시값');}
  function drawB(dt){t+=dt;var W=fit(c1b,150),H=150,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var ph=REDUCE?1:Math.min(1,t*0.6);
    if(!last||last.fail){txt(x,'보내면 쓴 증서는 찢어지고 새 증서가 생겨요',12,H/2,{s:12,c:C.muted});stamp(x,W,'설명용 장면');return;}
    last.ins.forEach(function(c,i){var X=30+i*120,Y=50,g=ph*14;x.globalAlpha=1-ph*0.7;x.fillStyle='#efe6d2';rr(x,X,Y-g,50,50,4);x.fill();rr(x,X+52,Y+g,50,50,4);x.fill();x.globalAlpha=1;txt(x,bf(c.v),X+50,Y+30,{a:'center',s:11,w:700,c:'#3a3040'});});
    var outs=[[last.pay,C.gfp]];if(last.change>0)outs.push([last.change,C.info]);outs.forEach(function(o,i){var X=W-140-i*130,Y=50;x.globalAlpha=ph;x.fillStyle=o[1];rr(x,X,Y,110,50,6);x.fill();x.globalAlpha=1;if(ph>0.5)txt(x,bf(o[0])+' BTC',X+55,Y+30,{a:'center',s:12,w:700,c:'#13141f'});});
    txt(x,ph<1?'찢는 중…':'쓴 증서는 다시 쓸 수 없고, 새 증서 '+outs.length+'장이 생겼다',12,H-14,{s:12,c:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){var p=pick(W0,amt,mode);
    kpis($('#k1'),[[bf(bal())+' BTC','지갑 잔액 = 조각의 합','a'],[W0.length+'개','지갑의 조각 수','m'],[p?p.sel.length+'개':'—','이번에 쓸 입력 조각',p?'g':'r'],[p?bf(r3(p.sum-amt-FEE))+' BTC':'잔액 부족','생길 거스름돈',p?'m':'r']]);
    $('#eq1').innerHTML='입력 합 <b>'+(p?bf(p.sum):'—')+'</b> = 지불 <em>'+bf(amt,2)+'</em> + 거스름돈 + 수수료 <i>'+bf(FEE)+'</i>';
    var m=[];if(last&&!last.fail)m.push(['g',last.ins.length+'개 조각('+last.ins.map(function(c){return bf(c.v)}).join(' + ')+')을 통째로 쓰고, '+bf(last.pay)+' BTC 지불'+(last.change>0?'과 '+bf(last.change)+' BTC 거스름돈':'')+' 조각을 새로 만들었어요.']);
    if(last&&last.fail)m.push(['r','지갑 조각을 다 더해도 금액과 수수료에 모자라요.']);
    m.push(['a','"큰 조각부터"는 입력 수가 적고, "작은 조각부터"는 잔돈 조각을 정리해요. 어느 쪽이든 잔액 칸은 없고 조각만 바뀌어요.']);ins($('#ins1'),m);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',function(){drawA();drawB(0);});reset();$('#b1Send').click();})();

/* ② 퍼지는 거래 */
var NET=(function(){var r=rng(34),N=[],E=[];for(var i=0;i<30;i++)N.push({x:0.04+0.92*r(),y:0.1+0.8*r()});N[0].x=0.03;N[0].y=0.5;N[29].x=0.97;N[29].y=0.5;
  function d(a,b){return Math.hypot(N[a].x-N[b].x,(N[a].y-N[b].y)*0.6)}var adj=N.map(function(){return []});
  function link(a,b){if(a===b||adj[a].indexOf(b)>=0)return;adj[a].push(b);adj[b].push(a);E.push([a,b]);}
  N.forEach(function(n,i){N.map(function(m,j){return j}).sort(function(a,b){return d(i,a)-d(i,b)}).slice(1,4).forEach(function(j){link(i,j);});});
  for(var g=0;g<5;g++){var seen=bfs([0]).dist;var lost=seen.indexOf(Infinity);if(lost<0)break;var best=-1,bd=9;for(var k=0;k<30;k++)if(seen[k]<Infinity&&d(k,lost)<bd){bd=d(k,lost);best=k;}link(best,lost);}
  function bfs(src){var dist=N.map(function(){return Infinity}),q=src.slice();src.forEach(function(s){dist[s]=0;});while(q.length){var u=q.shift();adj[u].forEach(function(v){if(dist[v]===Infinity){dist[v]=dist[u]+1;q.push(v);}});}return {dist:dist};}
  return {N:N,E:E,bfs:bfs};})();
function spread(sc){var a=NET.bfs([0]).dist,b=sc==='double'?NET.bfs([29]).dist:null;return NET.N.map(function(n,i){if(!b)return {h:a[i],w:'A'};return a[i]<=b[i]?{h:a[i],w:'A'}:{h:b[i],w:'B'};});}
(function(){var c2=$('#c2'),c2b=$('#c2b'),sc='one',S=spread('one'),t=99,go=false,miner=null;
  $$('#lv2 [data-sc]').forEach(function(b){b.addEventListener('click',function(){sc=b.dataset.sc;press('#lv2 [data-sc]',b);S=spread(sc);t=99;miner=pickMiner();upd();});});
  $('#b2Go').addEventListener('click',function(){t=0;go=true;miner=pickMiner();upd();});
  var seedM=7;function pickMiner(){seedM+=3;return Math.floor(rng(seedM)()*30);}miner=pickMiner();
  function maxH(){return Math.max.apply(null,S.map(function(s){return s.h}));}
  function drawA(dt){t+=dt||0;var W=fit(c2,250),H=250,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var hop=REDUCE?99:Math.floor(t*1.6),P=function(n){return [20+(W-40)*n.x,16+(H-40)*n.y]};
    NET.E.forEach(function(e){var a=P(NET.N[e[0]]),b=P(NET.N[e[1]]);x.strokeStyle='rgba(157,155,184,.25)';x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke();});
    NET.N.forEach(function(n,i){var p=P(n),s=S[i],on=s.h<=hop;x.fillStyle=on?(s.w==='A'?C.gfp:C.eye):'#3a3d55';x.beginPath();x.arc(p[0],p[1],i===0||(sc==='double'&&i===29)?9:6,0,7);x.fill();});
    var p0=P(NET.N[0]);txt(x,'지갑 A',p0[0]+12,p0[1]-10,{s:11,c:C.gfp,w:700});if(sc==='double'){var p9=P(NET.N[29]);txt(x,'지갑 B',p9[0]-12,p9[1]-10,{a:'right',s:11,c:C.eye,w:700});}
    txt(x,'홉 '+Math.min(hop,maxH())+'/'+maxH(),12,H-8,{s:11,c:C.muted});stamp(x,W,sc==='double'?'설명용 모형 · 같은 조각 두 거래':'설명용 모형 · 시드 34');}
  function drawB(dt){var W=fit(c2b,150),H=150,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var done=REDUCE||Math.floor(t*1.6)>maxH(),w=S[miner].w;
    x.fillStyle=C.panel2;rr(x,20,40,120,60,8);x.fill();txt(x,'다음 블록',80,64,{a:'center',s:12,w:700});txt(x,'노드 '+(miner+1)+'이 찾음',80,86,{a:'center',s:11,c:C.muted});
    if(done){x.fillStyle=w==='A'?C.gfp:C.eye;rr(x,170,48,170,44,6);x.fill();txt(x,'거래 '+w+' 담김 → 확정 시작',255,75,{a:'center',s:12,w:700,c:'#13141f'});
      if(sc==='double'){var o=w==='A'?'B':'A';x.globalAlpha=0.5;x.fillStyle=o==='A'?C.gfp:C.eye;rr(x,370,48,200,44,6);x.fill();x.globalAlpha=1;txt(x,'거래 '+o+': 이미 쓰인 조각 → 거부',470,75,{a:'center',s:12,w:700,c:'#13141f'});}}
    else txt(x,'전파가 끝나기를 기다리는 중…',170,75,{s:12,c:C.muted});
    stamp(x,W,'설명용 장면');drawA(dt);}
  function upd(){var a=S.filter(function(s){return s.w==='A'}).length;
    kpis($('#k2'),[[maxH()+'홉','망 전체에 닿기까지','a'],[a+'개','거래 A를 먼저 본 노드','g'],[sc==='double'?(30-a)+'개':'—','거래 B를 먼저 본 노드',sc==='double'?'r':'m'],['거래 '+S[miner].w,'다음 블록에 담긴 거래','m']]);
    $('#eq2').innerHTML='노드가 거래를 받으면: <b>검증</b> → <em>내 장부에 추가</em> → <i>이웃에게 전파</i> · 같은 조각을 쓰는 두 번째 거래는 거부';
    var m=[];if(sc==='one')m.push(['g','거래 하나가 '+maxH()+'홉 만에 노드 30개 모두에 닿았어요.']);
    else m.push(['r','망이 갈렸어요: 거래 A를 먼저 본 노드 '+a+'개, 거래 B를 먼저 본 노드 '+(30-a)+'개.'],['g','다음 블록을 찾은 노드 '+(miner+1)+'은 거래 '+S[miner].w+'를 담았어요. 이 블록을 받은 노드들은 다른 쪽 거래를 이미 쓰인 조각으로 보고 거부해요.']);
    ins($('#ins2'),m);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

Duel({names:{fly:'초파리 (은행식)',robo:'Money-Robo (비트코인식)'},higherIsBetter:false,drawMargin:0,
  run:function(){var n=1000;return {fly:n*(1+1+1),robo:n*1};},bar:function(v){return v/3000;},fmt:function(v){return fmt(v)+'개';},
  lesson:'거래 하나가 내역이자 증서면 맞춰 볼 문서가 줄어든다',
  say:function(r){return '송금 1,000건에 생긴 서로 다른 문서는 초파리 쪽 '+fmt(r.fly)+'개, Money-Robo 쪽 '+fmt(r.robo)+'개예요. 은행식은 두 은행의 원장과 확인증을 서로 맞춰야 해요.';}});
}});

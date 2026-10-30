import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from template import say
from build import CHAPTER, ROOT, SRC
RES = {'3-01': ('R', 'Money-Robo 승'), '3-02': ('R', 'Money-Robo 승'), '3-03': ('D', '무승부'), '3-04': ('R', 'Money-Robo 승'),
       '3-05': ('F', '초파리 승'), '3-06': ('F', '초파리 승'), '3-07': ('F', '초파리 승')}
COL = {'F': 'var(--c-fly)', 'R': 'var(--c-robo)', 'D': 'var(--amber)', 'X': 'var(--c-fly)'}
DESC = {'3-01': '계산 경쟁으로 뽑을까, 지분으로 뽑을까. 교안의 비교표를 내 기준으로 다시 읽는다.',
        '3-02': '전기료와 장비 단가가 계산력을 채굴장으로 모은다. 상위 몇 곳이면 과반인가.',
        '3-03': '21만 블록마다 절반. 사토시까지 더하면 20,999,999.9769 BTC, 그 뒤엔 수수료.',
        '3-04': '잔액 칸은 없다. 쓰지 않은 거래 조각과 거스름돈, 그리고 망에 퍼지는 거래.',
        '3-05': '은행은 감추고 비트코인은 끊는다. 주소 재사용과 모아 쓰기가 거래를 묶는다.',
        '3-06': '세 기능은 갖췄지만 변동성이 쓰기를 막는다. 인정하는 견해와 비판하는 견해.',
        '3-07': '익명성의 그늘과 공개 장부의 단서. 블록체인 편 21편을 닫는다.'}
cards = []
for p in CHAPTER['pages']:
    info = json.load(open(os.path.join(SRC, f"info_{p['num']}.json")))
    r, rt = RES[p['num']]
    cards.append(f'<a href="{p["file"]}"><span class="n">{p["num"]}</span> <b>{info["title"]}</b><p>{DESC[p["num"]]}</p>'
                 f'<p class="glabel">대결: {info["duel"]}</p><span class="res" style="color:{COL[r]};border-color:{COL[r]}">{r} · {rt}</span></a>')
tally = {'F': 0, 'R': 0, 'D': 0}
for r, _ in RES.values(): tally['F' if r in 'FX' else r] += 1
html = f'''<!DOCTYPE html><html lang="ko"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>블록체인 3장 비트코인</title>
<meta name="description" content="블록체인 편 3장 「비트코인」 목차: 합의 방식, 채굴장, 반감기, 거래, 익명성, 화폐성, 범죄 악용과 추적의 일곱 편">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/lab.css">
</head><body>
<div id="prog" aria-hidden="true"></div>
<nav class="top" aria-label="바로가기"><a class="logo" href="index.html"><i></i>{CHAPTER['short']}</a><a class="l" href="#toc">목차</a><a class="l" href="#ladder">사다리</a><a class="l" href="#score">대결 결산</a><a class="l" href="#about">이 저장소</a></nav>
<header class="hero" id="top"><div class="hex"></div>
  <div class="hero-bg" data-img="bg_ch3_index" role="img" aria-label="금화와 장부가 쌓인 회계실을 픽셀로 그린 배경"><canvas id="heroCv" aria-hidden="true"></canvas></div>
  <div class="wrap"><div class="hero-text">
    <div class="eyebrow">연구실 해설 대시보드 · 블록체인 편</div>
    <h1>3장 비트코인</h1>
    <p class="q">그 장부 위의 돈은 어떻게 만들어지고, 거래되고, 숨고, 드러날까? 그리고 그것은 화폐일까?</p>
    <p class="lead">2장이 장부를 지키는 기술이었다면, 3장은 그 장부 위의 돈, 비트코인입니다. 합의 방식 비교 → 채굴장과 중앙화 → 반감기와 발행 한도 → 거래가 곧 증서 → 익명성과 전자지갑 → 화폐인가 → 범죄 악용과 추적. 블록체인 편의 마지막 장입니다.</p></div>
    <div class="dialog">{say('doc','front','doc_e08','한 편에 두 칸씩, 모두 열네 칸의 사다리예요. 3-01부터 순서대로 읽으면 각 칸이 앞 칸의 한계에서 시작해요.')}
    {say('asst','smile','asst_e13','반감기(3-03)는 사토시까지 직접 더하고, 3-02의 공격 확률은 2-07의 백서 식을, 3-05의 노출 계산은 3-04의 거래 구조를 다시 써요.')}</div>
  </div></header>
<section class="level" id="toc"><div class="wrap"><h2>목차</h2><div class="toc">{''.join(cards)}</div></div></section>
<section class="level" id="ladder"><div class="wrap"><h2>한 장으로 보는 사다리</h2>
  <div class="tw"><table class="tb"><thead><tr><th>편</th><th>다루는 것</th><th>핵심 장치</th><th>남는 약점 → 다음 편</th></tr></thead><tbody>
  <tr><td>3-01</td><td>합의 방식</td><td>계산력 추첨 vs 지분 추첨, 비교표 가중치</td><td>"탈중앙화 높음"은 실제 분포에 달림</td></tr>
  <tr><td>3-02</td><td>채굴장과 중앙화</td><td>단가 차이 → 쏠림, 과반에 필요한 최소 수</td><td>채굴자가 왜 비용을 내나 → 보상</td></tr>
  <tr><td>3-03</td><td>반감기와 발행 한도</td><td>21만 블록마다 절반, 사토시 단위 합계</td><td>보상이 0이 되면 수수료로</td></tr>
  <tr><td>3-04</td><td>거래가 곧 증서</td><td>UTXO 조각 쓰기, 검증·추가·전파</td><td>모든 노드가 모든 거래를 봄</td></tr>
  <tr><td>3-05</td><td>익명성과 전자지갑</td><td>내역 공개 + 신원 연결 끊기</td><td>재사용·모아 쓰기로 묶임</td></tr>
  <tr><td>3-06</td><td>화폐인가</td><td>세 기능 vs 변동성, 두 견해</td><td>판정은 독자에게</td></tr>
  <tr><td>3-07</td><td>범죄 악용과 추적</td><td>공개 장부를 따라 확인 지점까지</td><td>확인 지점에 닿지 않는 흐름 · 편 끝</td></tr></tbody></table></div>
</div></section>
<section class="level" id="score"><div class="wrap"><h2>대결 결산</h2>
  <section class="kpis"><div class="kpi" style="border-top-color:var(--c-fly)"><b>{tally['F']}승</b><span>초파리 연구원</span></div><div class="kpi" style="border-top-color:var(--c-robo)"><b>{tally['R']}승</b><span>Money-Robo</span></div><div class="kpi a"><b>{tally['D']}번</b><span>무승부</span></div></section>
  {say('doc','judge','doc_e10','3장은 3 대 3, 무승부 1. 에너지·단가·서류 수는 Money-Robo가, 주소 습관·가격표·추적은 초파리가 가져갔다. 블록체인 편 전체로는 초파리 10승, Money-Robo 9승, 무승부 2.')}
</div></section>
<section class="level" id="about"><div class="wrap"><h2>이 저장소</h2>
  <p class="sub">각 HTML은 assets/ 폴더의 공용 파일(lab.css, lab.js, sprites.js)을 불러옵니다. 저장소를 통째로 올리거나 내려받아 index.html을 열면 됩니다. 편마다 맨 끝의 "온톨로지·서지 꾸러미"에서 지식 그래프와 참고문헌을 ZIP으로 가져갈 수 있습니다.</p>
  <p class="sub">자료: 강의 교안 「4차산업시대의 금융」 블록체인 단원 p.31–44, Nakamoto (2008), Blockstream Help Center (반감기). 캐릭터 그림: adminmrobo/fruitfly-lab-expressions (ea5da3f). 저자: 안상선.</p>
  <p class="pn">이전: {CHAPTER['prev_chapter']} · 다음: {CHAPTER['next_chapter']}</p>
</div></section>
<footer><div class="wrap"><p>연구실 해설 대시보드 · 블록체인 편 3장 · v1.0 · 2026-10-29</p></div></footer>
<div id="tip"></div><div id="study"><span id="stTxt">읽은 곳 0%</span><button id="stBtn" hidden>밑줄</button></div>
<script src="assets/sprites.js"></script><script src="assets/lab.js"></script>
<script>Cast.fill();heroArt('C');requestAnimationFrame(loop);addEventListener('scroll',function(){{var h=document.documentElement,p=Math.round(100*h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight));$('#prog').style.width=p+'%';$('#stTxt').textContent='읽은 곳 '+p+'%';}},{{passive:true}});</script>
</body></html>'''
open(os.path.join(ROOT, 'index.html'), 'w').write(html)
print('index ok')

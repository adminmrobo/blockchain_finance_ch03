LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '3-01', 'slug': 'pow-vs-pos', 'key': '3_01', 'anchor': 'C',
 'tab_title': '작업증명과 지분증명', 'meta_title': '작업증명과 지분증명 — 한 표를 계산력으로 줄까, 지분으로 줄까',
 'description': '블록을 쓸 사람을 계산 경쟁으로 뽑는 작업증명과 보유 지분으로 뽑는 지분증명을 같은 참여자들로 돌려 보고, 교안의 비교표를 가중치로 다시 읽는 해설 페이지',
 'dc_source': '강의 교안 「블록체인과 비트코인」 p.31; Nakamoto (2008) 4절',
 'h1': '작업증명과 지분증명<br>— 한 표를 무엇으로 줄까', 'hero_alt': '금화와 장부가 쌓인 회계실을 픽셀로 그린 배경',
 'question': '블록을 쓸 사람을 계산 경쟁으로 뽑으면 무엇을 얻고 무엇을 잃을까? 가진 코인으로 뽑으면?',
 'lead': '2-06에서 비트코인은 "계산력 하나당 한 표"로 블록을 쓸 사람을 정했습니다. 그런데 이 경쟁에는 전기가 듭니다. 교안은 작업증명과 지분증명을 블록체인의 주요 합의 메커니즘으로 소개하고, 둘을 아홉 가지 기준으로 비교합니다. 같은 참여자 다섯 명을 두 방식으로 돌려 보고, 비교표를 내 기준으로 다시 읽어 봅니다.',
 'kpis': [('컴퓨팅 파워', '작업증명의 합의 기반', 'a', [1]), ('보유량과 기간', '지분증명의 합의 기반', 'g', [1]), ('에너지 소비', '작업증명의 대가 (교안)', 'r', [1]), ('9가지', '교안 비교표의 기준 수', 'm', [1])],
 'hero': [('doc', 'think', 'doc_e09', '한 표를 복제하기 어려운 것에 매겨야 해요(1-07). 계산력도 그렇고, 돈을 들여 사야 하는 지분도 그래요. 문제는 각각의 대가예요.'),
          ('asst', 'smile', 'asst_e13', '같은 다섯 명이 두 방식으로 블록 1,000개를 나눠 갖는 실험을 준비했어요. 에너지 계량기도 달았어요.'),
          ('fly', 'point', 'fly_e08', '보안은 작업증명이 "매우 높음"이라며. 그럼 고민할 게 뭐가 있어?'),
          ('robo', 'coin', 'robo_e16', '계산 경쟁은 전기 낭비지. 지분으로 뽑으면 훨씬 가볍다고요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '블록과 에너지를 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 작업증명 편.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 지분증명 편.')],
 'why_title': '왜 합의 방식을 비교하나',
 'why_lead': '2장까지는 비트코인의 작업증명 하나만 봤어요. 3장은 비트코인을 다른 선택지와 나란히 놓고 보는 데서 시작합니다.',
 'why': [('작업증명', '컴퓨팅 파워를 사용해 복잡한 수학 문제를 해결하는 방식으로, 높은 보안성을 제공하지만 에너지 소비가 크다. <sup>[1]</sup>'),
         ('지분증명', '보유한 암호화폐의 양과 기간에 따라 검증자를 선정하는 방식으로, 에너지 효율이 높고 더 빠른 거래 처리가 가능하다. <sup>[1]</sup>'),
         ('전환 흐름', '교안은 최근 환경 문제로 작업증명에서 지분증명으로 전환하는 블록체인이 늘고 있다고 쓴다. <sup>[1]</sup> 비트코인은 백서대로 작업증명을 쓴다. <sup>[2]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 두 방식 모두 "한 표를 비싸게" 만들어요. 비싼 값을 전기로 치르느냐, 묶어 둔 코인으로 치르느냐가 달라요.'),
 'big_lead': '2장의 채굴(2-06)과 확정(2-07)을 다른 합의 방식과 비교하는 칸입니다. 다음 편(3-02)은 작업증명의 그늘인 채굴장과 중앙화를 봅니다.',
 'ladder': [('①', '두 가지 추첨', '같은 참여자, 계산력 추첨 vs 지분 추첨', '블록 몫은 비슷하게 나와도 드는 에너지가 다르다'),
            ('②', '비교표를 내 기준으로', '교안의 9가지 기준에 가중치를 매겨 다시 읽기', '표는 정성 평가다 → 3-02에서 중앙화를 숫자로')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '두 가지 추첨', 'title': '계산으로 뽑기와 지분으로 뽑기',
   'tags': [('방식: 블록마다 한 명을 뽑아 블록을 쓰게 함', 'g'), ('장부: 쪽을 쓸 사람을 정하는 두 규칙', '')],
   'left': '<p>장부 한 쪽을 누가 쓸지 정해야 한다. 첫째 규칙: 모두 자물쇠를 돌려 먼저 연 사람이 쓴다(모두가 손을 움직인다). 둘째 규칙: 금고에 맡겨 둔 금화가 많은 사람일수록 제비를 많이 넣고, 한 장을 뽑는다(손은 한 번만 움직인다).</p>',
   'right': '<p>작업증명은 컴퓨팅 파워로 문제를 푸는 경쟁이고, 지분증명은 보유한 암호화폐의 양과 기간에 따라 검증자를 선정한다. <sup>[1]</sup> 작업증명에서 블록을 쓸 확률은 계산력 몫에 비례한다(2-06). <sup>[2]</sup> 지분증명에서는 맡긴 지분의 몫이 그 역할을 한다.</p>',
   'panel': '''<h3>직접 해 보기 — 다섯 참여자, 블록 1,000개</h3>
    <div class="cwrap"><canvas id="c1" aria-label="다섯 참여자가 작업증명과 지분증명에서 각각 만든 블록 수와 쓴 에너지를 비교하는 막대그래프"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">방식</span><button class="bt" data-mode="pow" aria-pressed="true">작업증명</button><button class="bt" data-mode="pos" aria-pressed="false">지분증명</button></div>
      <div class="group"><span class="glabel">참여자 E의 몫 (계산력=지분)</span><input type="range" id="r1e" min="5" max="60" step="5" value="20" aria-label="참여자 E의 몫 퍼센트"><span class="val" id="v1e">20</span>%</div>
      <div class="group"><button class="bt primary" id="b1Run">▶ 다시 뽑기</button></div></div>
    <h3>행동으로 보기 — 블록 하나를 정할 때 움직이는 기계</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="작업증명에서는 모든 채굴기가 돌아가고 지분증명에서는 추첨 한 번만 일어나는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 몫은 같고 비용이 다르다</h4>
    <ol><li>두 방식 모두 오래 보면 각자 만든 블록 수가 몫에 가까워진다. 이 실험에서는 계산력 몫과 지분 몫을 같게 두었다.</li>
      <li>작업증명은 블록마다 모든 채굴기가 해시를 계산한다. 블록 하나를 쓰는 사람은 한 명이지만 에너지는 모두가 쓴다.</li>
      <li>지분증명은 추첨과 검증만 하면 된다. 교안이 에너지 효율을 "높음", 작업증명을 "낮음"으로 적은 이유다. <sup>[1]</sup></li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 에너지만 보면 답이 쉽다. 하지만 교안 비교표에는 보안성, 탈중앙화, 진입 장벽 같은 다른 기준도 있다. → 비교표를 내 기준으로.</p>''',
   'extra': '<details class="math"><summary>수식으로 보기</summary><p>블록마다 참여자 i가 뽑힐 확률 = 몫<sub>i</sub>. 에너지(예시 단위): 작업증명은 블록마다 채굴기 n대 × 10분 × 1단위/분, 지분증명은 블록마다 검증자 n명 × 0.01단위. 시드 31(작업증명)·32(지분증명)로 블록 1,000개를 뽑는다.</p><p class="lim">에너지 단위는 비교를 위한 예시값이다. 실제 소비량은 장비, 네트워크 규모, 지분증명의 구체적 설계에 따라 크게 다르다.</p></details>',
   'say': ('fly', 'type', 'fly_e09', '블록 몫은 두 방식이 거의 같네. 에너지 계량기만 다섯 자리 대 두 자리로 다르고.')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '비교표 다시 읽기', 'title': '교안의 비교표를 내 기준으로 다시 읽기',
   'tags': [('방식: 9가지 기준에 가중치를 주고 합산', 'g'), ('장부: 쪽 쓸 사람을 정하는 규칙의 득실표', '')],
   'left': '<p>규칙을 고를 때 무엇을 중히 여기는지는 사람마다 다르다. 어떤 사람은 장부를 함부로 못 고치게 하는 것을, 어떤 사람은 금화 없는 사람도 참여할 수 있는 것을, 어떤 사람은 등불 기름값을 가장 먼저 본다.</p>',
   'right': '<p>교안은 두 방식을 합의 기반, 보안성, 에너지 효율성, 탈중앙화 정도, 확장성, 진입 장벽, 처리 속도, 51% 공격 비용, 환경 영향으로 비교한다. <sup>[1]</sup> 51% 공격 비용은 작업증명이 "매우 높음(하드웨어 비용)", 지분증명이 "매우 높음(코인 가치의 51% 이상)"으로 둘 다 높다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 기준마다 가중치 (0~3)</h3>
    <div class="cwrap"><canvas id="c2" aria-label="교안 비교표의 기준별 평가를 가중치로 곱해 작업증명과 지분증명의 점수를 비교한 막대그래프"></canvas></div>
    <div class="ctrl" id="w2"></div>
    <div class="ctrl"><div class="group"><span class="glabel">미리 정한 관점</span><button class="bt" data-pre="sec">보안·탈중앙화 중시</button><button class="bt" data-pre="eco">에너지·환경 중시</button><button class="bt" data-pre="even">모두 같게</button></div></div>
    <h3>행동으로 보기 — 저울에 올린 두 방식</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="가중치를 반영한 점수에 따라 저울이 기우는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — "어느 쪽이 낫다"는 기준이 정한다</h4>
    <ol><li>교안의 평가를 점수로 옮겼다: 매우 높음 3, 높음·빠름 2, 중간 1.5, 낮음·제한적·느림 1. 진입 장벽과 환경 영향은 낮을수록 좋으므로 진입 장벽 높음 1·중간 1.5, 환경 영향 큼 1·작음 2로 매겼다.</li>
      <li>보안성과 탈중앙화를 무겁게 보면 작업증명이, 에너지와 환경과 속도를 무겁게 보면 지분증명이 앞선다.</li>
      <li>51% 공격 비용은 둘 다 "매우 높음"이라 이 기준만으로는 갈리지 않는다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 표의 평가는 정성적이다. 특히 "탈중앙화 높음"은 채굴이 실제로 여러 사람에게 퍼져 있을 때의 이야기다. → 3-02 채굴장과 중앙화.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면 — 표를 읽는 법</h4><p>비교표는 결론이 아니라 질문 목록이다. "보안성 매우 높음"은 공격에 큰 비용이 든다는 뜻이고, 그 비용을 누가 어떤 형태로 치르는지(전기와 장비, 또는 묶어 둔 코인)는 따로 따져야 한다. 교안은 환경 문제로 지분증명으로 옮겨 가는 블록체인이 늘고 있다고 쓴다. <sup>[1]</sup></p></div>',
   'say': ('asst', 'e10', 'asst_e10', '가중치를 모두 같게 두면 지분증명이 16점 대 13점으로 앞서요. "보안·탈중앙화 중시"를 누르면 순서가 바뀌어요.')},
 ],
 'duel': {'title': '블록 100개를 정하는 데 드는 에너지',
  'intro': '같은 참여자 10명이 블록 100개를 정한다. 초파리는 작업증명(채굴기 10대가 블록마다 10분씩 계산), 주판봇은 지분증명(검증자 10명이 블록마다 추첨·검증). 판정 기준은 <b>쓴 에너지</b>(예시 단위, 낮을수록 좋음). 위 실험과 같은 에너지 함수로 계산한다.',
  'fly': ('작업증명', '보안이 매우 높은 쪽은 이쪽이야. 전기값은 보안의 값이고.', '채굴기 10대'),
  'robo': ('지분증명', '추첨 한 번이면 끝! 계량기가 거의 안 돌아요.', '검증자 10명'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>작업증명: 10대 × 10분 × 1단위/분 × 블록 100개. 지분증명: 10명 × 0.01단위 × 블록 100개. 막대는 로그 눈금(1에서 10<sup>5</sup>까지)이다.</p><p class="lim">에너지 단위는 예시값이다. 이 대결은 에너지만 잰다. 보안성·탈중앙화는 ②칸에서 따로 본다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>기준</th><th>작업증명 (PoW)</th><th>지분증명 (PoS)</th></tr></thead><tbody>
   <tr><td>합의 메커니즘 기반</td><td>컴퓨팅 파워</td><td>보유 암호화폐 양과 기간</td></tr>
   <tr><td>보안성</td><td>매우 높음</td><td>높음</td></tr>
   <tr><td>에너지 효율성</td><td>낮음</td><td>높음</td></tr>
   <tr><td>탈중앙화 정도</td><td>높음</td><td>중간</td></tr>
   <tr><td>확장성</td><td>제한적</td><td>높음</td></tr>
   <tr><td>진입 장벽</td><td>높음 (고성능 채굴 장비 필요)</td><td>중간 (일정량의 암호화폐 보유 필요)</td></tr>
   <tr><td>트랜잭션 처리 속도</td><td>상대적으로 느림</td><td>빠름</td></tr>
   <tr><td>51% 공격 비용</td><td>매우 높음 (하드웨어 비용)</td><td>매우 높음 (코인 가치의 51% 이상)</td></tr>
   <tr><td>환경 영향</td><td>큼</td><td>작음</td></tr></tbody></table></div>
   <p class="sub">출처: 교안 p.31의 「작업 증명과 지분 증명 비교」 표를 옮김. <sup>[1]</sup></p>''',
 'summary_say': ('doc', 'front', 'doc_e08', '두 방식 모두 한 표를 비싸게 만들어요. 작업증명은 전기와 장비로, 지분증명은 묶어 둔 코인으로. 다음 편은 작업증명의 비용이 낳은 채굴장 이야기예요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('robo', 'happy', 'robo_e12'), ('fly', 'cry', 'fly_e21'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 주판봇이 두 팔을 들고, 초파리 연구원이 폭포 눈물을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 작업증명은 계산력으로, 지분증명은 보유 지분으로 블록을 쓸 사람을 뽑는다.<br>· 에너지는 지분증명이 훨씬 적게 든다.<br>· 어느 쪽이 나은지는 보안·탈중앙화·에너지 중 무엇을 무겁게 보느냐에 달렸다.'),
           ('robo', 'happy', 'robo_e12', '계량기가 다섯 자리 대 두 자리! 가벼운 쪽이 이겼어요.'),
           ('fly', 'cry', 'fly_e21', '…에너지로는 못 이기지. 인정. 그래도 비트코인이 왜 이걸 쓰는지는 보안 쪽 칸에 있어.'),
           ('asst', 'e16', 'asst_e16', '다음은 3-02, 작업증명의 비용이 채굴을 어디로 모으는지 봐요.')],
 'kg_hint': '작업증명, 지분증명, 에너지, 51% 공격…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인과 비트코인」 p.31 (작업증명과 지분증명의 정의, 에너지 소비와 효율, 지분증명으로의 전환 흐름, 「작업 증명과 지분 증명 비교」 표). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 4절(작업증명, CPU 하나당 한 표). 대학 강의 자료실 사본으로 본문 확인.'],
 'examples': ['다섯 참여자의 몫과 에너지 단위 (예시값), 블록 추첨 시드 31·32', '비교표의 점수 환산(매우 높음 3 … 낮음 1)과 미리 정한 가중치 — 페이지에서 정한 환산 규칙', '대결: 참여자 10명, 블록 100개, 에너지 예시 단위'],
 'gloss_keys': [('작업증명', True), ('지분증명', True), ('51% 공격', True), ('계산력', False), ('비트코인', False)],
 'gloss_anchor': {'작업증명': '#why', '지분증명': '#why', '51% 공격': '#lv2', '계산력': '#lv1', '비트코인': '#why'},
 'quiz': {
  'lv1': [{'q': '교안에 따르면 지분증명은 무엇을 기준으로 검증자를 뽑나?', 'o': ['보유한 암호화폐의 양과 기간', '컴퓨팅 파워', '가입 순서', '거주 국가'], 'a': 0, 'why': '교안 p.31. 작업증명은 컴퓨팅 파워, 지분증명은 보유량과 기간이에요.', 'hint': '"왜" 카드 둘째.', 'c': 'lab:method/proof-of-stake'},
          {'q': '작업증명에서 블록 하나를 정할 때 에너지를 쓰는 쪽은?', 'o': ['경쟁에 참여한 모든 채굴기', '블록을 쓴 한 명', '거래를 보낸 사람', '아무도 쓰지 않는다'], 'a': 0, 'why': '블록은 한 명이 쓰지만 모든 채굴기가 해시를 계산해요.', 'hint': '"행동으로 보기" 장면.', 'c': 'lab:metric/energy-units'}],
  'lv2': [{'q': '교안 비교표에서 두 방식의 평가가 같은 기준은?', 'o': ['51% 공격 비용', '에너지 효율성', '확장성', '환경 영향'], 'a': 0, 'why': '둘 다 "매우 높음"이에요. 작업증명은 하드웨어 비용, 지분증명은 코인 가치의 51% 이상.', 'hint': '정리 표의 여덟째 줄.', 'c': 'lab:concept/majority-attack'},
          {'q': '보안성과 탈중앙화에 가중치를 크게 주면 이 페이지의 점수는?', 'o': ['작업증명이 앞선다', '지분증명이 앞선다', '항상 같다', '계산할 수 없다'], 'a': 0, 'why': '교안 표에서 보안성은 매우 높음 대 높음, 탈중앙화는 높음 대 중간이에요.', 'hint': '"보안·탈중앙화 중시" 버튼.', 'c': 'lab:method/weighted-comparison'}]},
 'kgspec': {
  'ladder': ['lab:method/proof-of-work', 'lab:method/weighted-comparison'],
  'about': ['lab:method/proof-of-work', 'lab:method/proof-of-stake', 'lab:concept/majority-attack', 'lab:metric/energy-units'],
  'nodes': [
   ('lab:method/weighted-comparison', 'Method', '가중치로 다시 읽은 비교표', 'weighted comparison table', '#lv2', '교안 비교표의 정성 평가를 점수로 옮기고 기준별 가중치를 곱해 합산하는 방법.', 3),
   ('lab:metric/energy-units', 'Metric', '쓴 에너지 (예시 단위)', 'energy used', '#lv1', '블록을 정하는 동안 참여자 전체가 쓴 에너지. 이 페이지의 예시 단위.', 3),
   ('lab:metric/security-rating', 'Metric', '보안성 평가', 'security rating', '#lv2', '교안 비교표의 보안성 항목. 작업증명 매우 높음, 지분증명 높음.', 3, [(LEC, '교안 p.31')]),
   ('lab:concept/decentralization', 'Concept', '탈중앙화 정도', 'degree of decentralization', '#lv2', '참여와 결정권이 얼마나 여러 참여자에게 퍼져 있는가.', 3, [(LEC, '교안 p.31')]),
   ('lab:concept/environmental-impact', 'Concept', '환경 영향', 'environmental impact', '#lv2', '합의 방식이 소비하는 에너지가 환경에 주는 영향.', 3, [(LEC, '교안 p.31')]),
   ('lab:limitation/energy-cost', 'Limitation', '작업증명의 에너지 소비', 'energy consumption of PoW', '#lv1', '블록마다 모든 채굴기가 계산하므로 에너지 소비가 크다.', 4, [(LEC, '교안 p.31')]),
   ('lab:limitation/qualitative-table', 'Limitation', '정성적 비교표', 'qualitative table', '#lv2', '비교표의 평가는 정성적이어서 실제 분산 정도는 따로 재야 한다.', 3),
   ('lab:analogy/lock-vs-lottery', 'Analogy', '자물쇠 경쟁 대 제비뽑기 ↔ 작업증명 대 지분증명', 'padlock race vs lottery', '#lv1', '모두가 손을 움직이는 경쟁과, 맡긴 금화만큼 제비를 넣는 추첨.', 3),
   ('lab:question/core', 'Question', '한 표를 계산력으로 줄까, 지분으로 줄까?', 'Compute or stake for a vote?', '#top', None, 3),
   ('lab:question/duel', 'Question', '블록 100개를 정하는 데 두 방식은 에너지를 얼마나 쓰나?', 'Energy for 100 blocks', '#duel', None, 3),
  ],
  'edges': [
   ('lab:method/proof-of-work', 'lab:contrastsWith', 'lab:method/proof-of-stake', '#lv1'),
   ('lab:method/proof-of-work', 'lab:hasLimitation', 'lab:limitation/energy-cost', '#lv1'),
   ('lab:limitation/energy-cost', 'lab:addressedBy', 'lab:method/proof-of-stake', '#lv1'),
   ('lab:method/proof-of-work', 'lab:evaluatedBy', 'lab:metric/energy-units', '#lv1'),
   ('lab:method/proof-of-stake', 'lab:evaluatedBy', 'lab:metric/energy-units', '#duel'),
   ('lab:metric/hash-rate', 'lab:partOf', 'lab:method/proof-of-work', '#lv1'),
   ('lab:concept/bitcoin', 'lab:prerequisiteOf', 'lab:method/proof-of-work', '#why'),
   ('lab:method/weighted-comparison', 'lab:evaluatedBy', 'lab:metric/security-rating', '#lv2'),
   ('lab:concept/decentralization', 'lab:partOf', 'lab:method/weighted-comparison', '#lv2'),
   ('lab:concept/environmental-impact', 'lab:partOf', 'lab:method/weighted-comparison', '#lv2'),
   ('lab:concept/majority-attack', 'lab:partOf', 'lab:method/weighted-comparison', '#lv2'),
   ('lab:limitation/energy-cost', 'lab:prerequisiteOf', 'lab:method/weighted-comparison', '#lv2'),
   ('lab:method/weighted-comparison', 'lab:hasLimitation', 'lab:limitation/qualitative-table', '#lv2'),
   ('lab:limitation/qualitative-table', 'lab:raises', 'lab:question/core', '#lv2'),
   ('lab:metric/energy-units', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/energy-cost', 'lab:raises', 'lab:question/core', '#lv1'),
   ('lab:analogy/lock-vs-lottery', 'lab:analogyOf', 'lab:method/proof-of-stake', '#lv1'),
  ],
  'claims': [
   ('lab:claim/pow-def', '작업증명은 컴퓨팅 파워를 사용해 복잡한 수학 문제를 해결하는 방식으로, 높은 보안성을 제공하지만 에너지 소비가 크다', '#why', ['lab:method/proof-of-work', 'lab:limitation/energy-cost'], [(LEC, '교안 p.31')], 'F01'),
   ('lab:claim/pos-def', '지분증명은 보유한 암호화폐의 양과 기간에 따라 검증자를 선정하는 방식으로, 에너지 효율이 높고 더 빠른 거래 처리가 가능하다', '#why', ['lab:method/proof-of-stake'], [(LEC, '교안 p.31')], 'F02'),
   ('lab:claim/shift-to-pos', '최근 환경 문제로 작업증명에서 지분증명으로 전환하는 블록체인들이 증가하고 있다', '#why', ['lab:method/proof-of-stake', 'lab:concept/environmental-impact'], [(LEC, '교안 p.31')], 'F03'),
   ('lab:claim/attack-cost-both', '51% 공격 비용은 작업증명(하드웨어 비용)과 지분증명(코인 가치의 51% 이상) 모두 매우 높다', '#lv2', ['lab:concept/majority-attack'], [(LEC, '교안 p.31 표')], 'F04'),
   ('lab:claim/one-cpu-vote-3', '작업증명은 본질적으로 CPU 하나당 한 표다', '#lv1', ['lab:method/proof-of-work'], [(WP, '4절')], 'F05'),
  ],
  'sims': [('lab:simulation/two-lotteries', '다섯 참여자 두 방식 실험', '#lv1', ['lab:method/proof-of-work', 'lab:method/proof-of-stake']),
           ('lab:simulation/weighted-table', '가중치 비교표', '#lv2', ['lab:method/weighted-comparison']),
           ('lab:simulation/duel-energy', '블록 100개 에너지 대결', '#duel', ['lab:metric/energy-units'])],
 },
}

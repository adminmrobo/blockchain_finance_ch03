LEC, WP, BS = "lecture2024blockchain", "nakamoto2008bitcoin", "blockstream2024halving"
PAGE = {
 'num': '3-03', 'slug': 'halving-and-cap', 'key': '3_03', 'anchor': 'C',
 'tab_title': '반감기와 발행 한도', 'meta_title': '반감기와 발행 한도 — 2,100만 개는 어떻게 정해지나',
 'description': '블록 보상이 21만 블록마다 절반으로 줄어드는 규칙을 사토시 단위까지 직접 더해 총 발행량을 계산하고, 보상이 줄어든 뒤 채굴자의 수입이 거래 수수료로 옮겨 가는 과정을 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인과 비트코인」 p.33; Nakamoto (2008) 6절; Blockstream Help Center',
 'h1': '반감기와 발행 한도<br>— 2,100만 개는 어떻게 정해지나', 'hero_alt': '금화와 장부가 쌓인 회계실을 픽셀로 그린 배경',
 'question': '아무도 발행을 결정하지 않는데, 비트코인은 어떻게 총량이 정해져 있을까? 보상이 0이 되면 채굴자는 왜 계속 채굴할까?',
 'lead': '2-06에서 채굴자는 블록의 첫 거래로 새 코인을 받았습니다. 그 양은 정해진 규칙으로 줄어듭니다. 교안은 묶음당 생성량이 50 BTC를 넘지 않고, 총 발행량이 2,100만 개로 제한되며, 보통 4년 주기로 보상이 줄어든다고 설명합니다. 이 규칙을 사토시 단위까지 직접 더해 보고, 보상이 줄어든 뒤 채굴자의 수입이 어디서 오는지 봅니다.',
 'kpis': [('50 BTC', '처음 블록 보상 (묶음당 상한)', 'a', [1]), ('21만 블록', '보상이 절반으로 줄어드는 간격 (약 4년)', 'g', [3]), ('3.125 BTC', '2024년 4월 반감기 뒤 블록 보상', 'm', [3]), ('2,100만', '총 발행량 상한 (교안)', 'r', [1])],
 'hero': [('doc', 'think', 'doc_e09', '발행량을 정하는 중앙은행이 없으니, 규칙을 처음부터 코드에 넣었어요. 그 규칙을 그대로 더해 보면 총량이 나와요.'),
          ('asst', 'smile', 'asst_e13', '블록 보상을 사토시 단위로 서른세 번 반으로 나누며 더해 볼게요. 정수로 나누니까 끝자리가 잘려요.'),
          ('fly', 'point', 'fly_e08', '2,100만이라고 다들 말하는데, 정말 딱 2,100만이야? 직접 더해 봐야지.'),
          ('robo', 'coin', 'robo_e16', '2,100만이면 2,100만이지. 어림값이면 충분해요!')],
 'cast': [('doc', 'scale', 'doc_e13', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '보상을 더하고 수수료를 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 사토시까지 더한다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 2,100만으로 어림한다.')],
 'why_title': '왜 발행 규칙을 보나',
 'why_lead': '은행 장부(1-06)에서는 기관이 돈의 양을 정했어요. 비트코인에서는 누가 정할까요? 답은 "규칙"이에요.',
 'why': [('발행 한도', '비트코인이 묶음당 생성되는 양은 50 BTC를 넘지 않으며, 총 발행량은 일정 규모(2,100만)로 제한돼 무분별한 채굴로 가치가 폭락하는 현상은 나타나지 않는다고 교안은 설명한다. <sup>[1]</sup>'),
         ('반감기', '블록 보상은 21만 블록마다(약 4년) 절반으로 줄어든다. 2024년 4월 19일 840,000번째 블록에서 보상이 6.25에서 3.125 BTC로 줄었다. <sup>[3]</sup>'),
         ('보상에서 수수료로', '백서는 정해진 양의 코인이 유통된 뒤에는 채굴 보상이 전부 거래 수수료로 옮겨 가 인플레이션이 없어질 수 있다고 쓴다. <sup>[2]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 금광에 비유하면, 매장량이 정해져 있고 캘수록 덜 나오는 광산이에요. 백서도 채굴을 금 캐기에 견줘요.'),
 'big_lead': '2-06의 채굴 보상이 시간에 따라 어떻게 바뀌는지 계산하는 칸입니다. 다음 편(3-04)은 그렇게 만들어진 코인이 거래에서 어떤 모양으로 존재하는지 봅니다.',
 'ladder': [('①', '반감기를 더하면 한도', '21만 블록마다 보상 절반 → 총 발행량', '보상은 결국 0이 된다'),
            ('②', '보상에서 수수료로', '블록 수입 = 보상 + 수수료, 보상이 줄면 수수료 몫이 커진다', '수수료만으로 보안 비용을 댈 수 있나는 열린 질문')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '반감기와 한도', 'title': '21만 블록마다 절반 — 더하면 한도가 된다',
   'tags': [('방식: 보상을 사토시 단위로 반씩 나누며 누적', 'g'), ('장부: 쪽마다 붙는 금화가 반씩 줄어드는 규칙', '')],
   'left': '<p>장부 쪽을 붙일 때마다 금화를 준다. 처음 21만 쪽까지는 쪽당 50닢, 다음 21만 쪽은 25닢, 그다음은 12닢 반… 금화는 쪼갤 수 있는 가장 작은 조각까지만 나눈다. 조각보다 작아지면 더는 주지 않는다.</p>',
   'right': '<p>블록 보상은 처음 50 BTC에서 21만 블록마다 절반으로 줄고, 이 일정이 총 발행량을 2,100만 개로 묶는다. <sup>[3]</sup> 나눗셈이 정수로 이뤄져 끝자리가 잘리므로 최종 총량은 2,100만보다 조금 적고, 마지막 조각은 2140년 무렵 채굴될 것으로 본다. <sup>[3]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 반감기 0번부터 33번까지</h3>
    <div class="cwrap"><canvas id="c1" aria-label="반감기 시기별 블록 보상 계단과 누적 발행량 곡선, 2,100만 선을 함께 그린 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">반감기 시기 (0 = 처음)</span><input type="range" id="r1e" min="0" max="33" step="1" value="4" aria-label="반감기 시기"><span class="val" id="v1e">4</span></div>
      <div class="group"><span class="glabel">단위</span><button class="bt" data-u="btc" aria-pressed="true">BTC</button><button class="bt" data-u="sat" aria-pressed="false">사토시</button></div></div>
    <h3>행동으로 보기 — 블록마다 떨어지는 금화</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="블록이 쌓일 때마다 보상 금화가 떨어지고, 반감기마다 금화 크기가 절반으로 줄어드는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 등비급수와 잘린 끝자리</h4>
    <ol><li>보상이 절반씩 줄면 합은 50 × 21만 × (1 + 1/2 + 1/4 + …) → 50 × 21만 × 2 = 2,100만에 다가간다.</li>
      <li>실제로는 사토시(1억분의 1 BTC) 단위 정수로 나누므로 끝자리가 잘린다. 33번째 반감기에 보상이 0사토시가 되고, 합계는 20,999,999.9769 BTC다.</li>
      <li>4번째 반감기(2024년)에 보상은 3.125 BTC가 되었다. <sup>[3]</sup> 이 시점까지 총량의 약 94%가 이미 발행되었다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 보상이 0으로 가면 채굴자는 무엇을 받고 채굴하나? → 보상에서 수수료로.</p>''',
   'extra': '<details class="math"><summary>수식으로 보기</summary><p>보상(i) = ⌊5,000,000,000 ÷ 2<sup>i</sup>⌋ 사토시, i = 반감기 횟수. 총량 = Σ<sub>i=0..32</sub> 210,000 × 보상(i) = 2,099,999,997,690,000 사토시 = 20,999,999.9769 BTC. 시기별 연도는 블록 10분 가정으로 어림한 값이다.</p><p class="lim">실제 반감기 날짜는 블록 생성 속도에 따라 앞당겨지거나 늦춰진다. 이 페이지는 2024년 4월 반감기만 실제 날짜로 표시한다.</p></details>',
   'say': ('fly', 'type', 'fly_e09', '서른세 번 더해 보니 20,999,999.9769. 딱 2,100만은 아니네. 0.0231 BTC가 모자라.')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '보상에서 수수료로', 'title': '보상이 줄면 무엇이 채굴을 받치나 — 수수료',
   'tags': [('방식: 블록 수입 = 새 코인 + 거래 수수료', 'g'), ('장부: 금화 대신 쪽마다 받는 기록료', '')],
   'left': '<p>쪽당 금화가 줄어도 장부 쓰는 사람이 남으려면 다른 벌이가 있어야 한다. 장부에 거래를 적어 달라는 사람들이 내는 기록료다. 금화가 줄수록 기록료가 벌이의 대부분이 된다.</p>',
   'right': '<p>백서는 블록의 첫 거래가 블록을 만든 사람에게 새 코인을 주어 노드가 네트워크를 지지하게 하고, 이를 금 캐는 사람이 자원을 들여 금을 유통시키는 일에 견준다. <sup>[2]</sup> 보상은 거래 수수료로도 줄 수 있으며, 정해진 양이 유통된 뒤에는 전부 수수료로 옮겨 갈 수 있다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 블록 하나의 수입 구성</h3>
    <div class="cwrap"><canvas id="c2" aria-label="반감기 시기별로 블록 하나의 수입을 새 코인과 수수료로 나눠 쌓은 막대그래프"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">블록당 수수료 (BTC)</span><input type="range" id="r2f" min="0" max="20" step="1" value="5" aria-label="블록당 수수료"><span class="val" id="v2f">0.5</span></div></div>
    <h3>행동으로 보기 — 블록마다 채굴자에게 가는 두 주머니</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="반감기가 지날수록 새 코인 주머니는 작아지고 수수료 주머니의 비중이 커지는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 주머니가 바뀐다</h4>
    <ol><li>수수료는 거래의 입력 합계와 출력 합계의 차이다. <sup>[2]</sup> 이 페이지는 블록당 수수료를 시기와 관계없이 같다고 두었다(예시값).</li>
      <li>블록당 수수료가 0.5 BTC라면 7번째 반감기(보상 0.390625 BTC)부터 수수료가 보상보다 커진다.</li>
      <li>백서는 탐욕스러운 공격자라도 규칙을 지켜 새 코인을 버는 편이 자기 재산의 가치를 지탱하는 시스템을 무너뜨리는 것보다 이득이라고 본다. <sup>[2]</sup></li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 수수료만으로 2-07의 보안 비용을 계속 댈 수 있을지는 이 모형이 답하지 못한다. 수수료 수준은 거래 수요에 달려 있다.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면 — 교안의 "공급 50% 감소"</h4><p>교안은 반감기를 "수요는 늘어나는데 일정 시점을 기준으로 공급이 매번 50% 감소한다"고 쉽게 풀어 설명한다. <sup>[1]</sup> 여기서 줄어드는 것은 새로 나오는 양(흐름)이지 이미 있는 양(총량)이 아니다. 4번째 반감기 뒤 새로 나오는 양은 블록당 3.125 BTC다. <sup>[3]</sup> 이 페이지는 가격을 다루지 않는다.</p></div>',
   'say': ('asst', 'e10', 'asst_e10', '블록당 수수료 0.5 BTC로 두면 7번째 반감기부터 수수료 주머니가 새 코인 주머니보다 커져요.')},
 ],
 'duel': {'title': '총 발행량: 사토시까지 더하기 vs 2,100만 어림',
  'intro': '초파리는 보상을 사토시 단위 정수로 반씩 나누며 서른세 번 더하고, 주판봇은 "2,100만"으로 어림한다. 판정 기준은 <b>규칙대로 계산한 실제 합계와의 차이</b>(BTC, 작을수록 좋음). 차이가 0.1 BTC 이하면 무승부로 본다.',
  'fly': ('사토시까지 더하기', '정수로 나누면 끝자리가 잘리잖아. 그걸 다 더해야 정확하지.', '반감기 33번 누적'),
  'robo': ('2,100만 어림', '교안에도 2,100만이라고 써 있어요. 그걸로 충분!', '어림값 21,000,000'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>실제 합계 = Σ 210,000 × ⌊5×10<sup>9</sup> ÷ 2<sup>i</sup>⌋ 사토시를 BTC로 바꾼 값(위 ①과 같은 함수). 각자 답과 이 값의 차이를 잰다. 무승부 기준 0.1 BTC는 이 페이지가 정한 값이다.</p><p class="lim">0.0231 BTC는 총량의 10억분의 1 수준이다. 교안의 "2,100만"은 이 규칙의 어림값이다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>반감기</th><th>대략의 시기</th><th>블록 보상 (BTC)</th><th>그때까지 누적 발행 비율</th></tr></thead><tbody>
   <tr><td>0 (처음)</td><td>2009</td><td>50</td><td>0%</td></tr>
   <tr><td>1</td><td>약 2012</td><td>25</td><td>50%</td></tr>
   <tr><td>2</td><td>약 2016</td><td>12.5</td><td>75%</td></tr>
   <tr><td>3</td><td>약 2020</td><td>6.25</td><td>87.5%</td></tr>
   <tr><td>4</td><td>2024년 4월 (블록 840,000)</td><td>3.125</td><td>93.75%</td></tr>
   <tr><td>33</td><td>2140년 무렵</td><td>0</td><td>100% (20,999,999.9769 BTC)</td></tr></tbody></table></div>
   <p class="sub">2024년 반감기와 2140년 무렵은 Blockstream 자료, 나머지 연도는 블록 10분 가정으로 어림. <sup>[3]</sup></p>''',
 'summary_say': ('doc', 'scale', 'doc_e13', '발행 한도는 누가 지키는 약속이 아니라 규칙을 더한 결과예요. 2,100만은 그 결과의 어림값이고요. 다음 편은 이 코인이 거래 안에서 어떤 모양인지 봐요.'),
 'stage': [('doc', 'scale', 'doc_e13'), ('asst', 'smile', 'asst_e13'), ('fly', 'coffee', 'fly_e13'), ('robo', 'meh', 'robo_e18')],
 'outro_alt': '무대 위에 네 캐릭터가 같은 높이로 서 있고, 초파리는 커피잔을, 주판봇은 일자 눈을 한 장면',
 'outro': [('doc', 'scale', 'doc_e13', '오늘의 세 줄.<br>· 블록 보상은 50 BTC에서 21만 블록마다 절반으로 준다.<br>· 사토시 단위로 더하면 총량은 20,999,999.9769 BTC, 어림해서 2,100만이다.<br>· 보상이 줄수록 채굴자의 수입은 거래 수수료로 옮겨 간다.'),
           ('asst', 'smile', 'asst_e13', '대결은 차이 0 대 0.0231 BTC. 0.1 BTC 기준 안이라 이번 판은 무승부예요. 정확한 값과 어림값이 같은 이야기를 하고 있었어요.'),
           ('fly', 'coffee', 'fly_e13', '끝자리까지 맞혔는데 무승부라니. 뭐, 10억분의 1이면 인정.'),
           ('robo', 'meh', 'robo_e18', '어림이 틀린 건 아니었네… 이겼다고도 졌다고도 못 하겠어요.')],
 'kg_hint': '반감기, 발행 한도, 사토시, 수수료…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인과 비트코인」 p.33 (묶음당 생성량 50 BTC 이하, 총 발행량 2,100만 제한, 4년 주기 보상 감소와 반감기, "공급이 매번 50% 감소"; 교안이 인용한 보도: 조선일보 2024.02.23). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 6절(블록의 첫 거래로 새 코인, 금 캐기 비유, 거래 수수료, 정해진 양 유통 뒤 수수료로 전환·인플레이션 없음, 탐욕스러운 공격자도 규칙을 지키는 편이 이득). 6절 내용은 HackerNoon 재수록본으로 재확인.',
                 'Blockstream Help Center. "What is the Bitcoin halving?" (21만 블록마다 보상 절반, 2009년 50 BTC, 2024년 4월 19일 블록 840,000에서 6.25 → 3.125 BTC, 총량 2,100만 상한과 정수 나눗셈으로 조금 적어짐, 2140년 무렵 마지막 조각). 2026-10-29 확인.'],
 'examples': ['반감기 시기별 연도(2024년 제외)는 블록 10분 가정의 어림값', '블록당 수수료 0.5 BTC — 예시값, 시기와 관계없이 같다고 둠', '대결의 무승부 기준 0.1 BTC — 페이지가 정한 값'],
 'gloss_keys': [('반감기', True), ('발행 한도', True), ('사토시', True), ('거래 수수료', True), ('채굴 보상', False), ('비트코인', False)],
 'gloss_anchor': {'반감기': '#why', '발행 한도': '#why', '사토시': '#lv1', '거래 수수료': '#lv2', '채굴 보상': '#lv1', '비트코인': '#why'},
 'quiz': {
  'lv1': [{'q': '블록 보상이 절반으로 줄어드는 간격은?', 'o': ['21만 블록 (약 4년)', '2,016블록 (약 2주)', '매년', '100만 블록'], 'a': 0, 'why': 'Blockstream 자료: 21만 블록마다, 대략 4년.', 'hint': 'KPI 둘째.', 'c': 'lab:concept/halving'},
          {'q': '사토시 단위로 정확히 더한 비트코인 총 발행량에 가장 가까운 것은?', 'o': ['20,999,999.9769 BTC', '21,000,000.0000 BTC', '21,000,000.0231 BTC', '무한대'], 'a': 0, 'why': '정수 나눗셈으로 끝자리가 잘려 2,100만보다 0.0231 BTC 적어요.', 'hint': '대결의 초파리 쪽 답.', 'c': 'lab:concept/supply-cap'}],
  'lv2': [{'q': '백서가 말한, 새 코인을 다 발행한 뒤 채굴 보상의 원천은?', 'o': ['거래 수수료', '중앙은행 지원금', '새 반감기', '광고 수입'], 'a': 0, 'why': '백서 6절: 정해진 양이 유통된 뒤 보상은 전부 거래 수수료로 옮겨 갈 수 있어요.', 'hint': '"왜" 카드 셋째.', 'c': 'lab:concept/transaction-fee'},
          {'q': '블록당 수수료가 0.5 BTC라면 수수료가 새 코인 보상보다 처음 커지는 반감기는? (보상: 6번째 0.78125, 7번째 0.390625 BTC)', 'o': ['7번째', '4번째', '6번째', '33번째'], 'a': 0, 'why': '0.5 > 0.390625가 되는 첫 시기가 7번째예요.', 'hint': '②의 막대.', 'c': 'lab:method/fee-transition'}]},
 'kgspec': {
  'ladder': ['lab:method/halving-schedule', 'lab:method/fee-transition'],
  'about': ['lab:concept/halving', 'lab:concept/supply-cap', 'lab:concept/transaction-fee', 'lab:concept/block-reward'],
  'nodes': [
   ('lab:method/halving-schedule', 'Method', '반감기 발행 일정', 'halving issuance schedule', '#lv1', '블록 보상을 21만 블록마다 사토시 단위 정수로 절반씩 줄이는 발행 규칙.', 4, [(BS, 'halving 설명')]),
   ('lab:method/fee-transition', 'Method', '보상에서 수수료로의 전환', 'transition to fees', '#lv2', '새 코인 보상이 줄면서 채굴자의 블록 수입이 거래 수수료로 옮겨 가는 과정.', 4, [(WP, '6절')]),
   ('lab:metric/total-supply', 'Metric', '총 발행량 (사토시 합계)', 'total supply', '#lv1', '반감기 규칙대로 모든 보상을 더한 값. 20,999,999.9769 BTC.', 4),
   ('lab:metric/fee-share', 'Metric', '블록 수입 중 수수료 몫', 'fee share of block revenue', '#lv2', '블록 하나의 수입(보상 + 수수료) 가운데 수수료가 차지하는 비율.', 3),
   ('lab:metric/supply-error', 'Metric', '실제 합계와의 차이', 'error from exact total', '#duel', '각 답과 규칙대로 계산한 총 발행량의 차이(BTC).', 3),
   ('lab:concept/integer-truncation', 'Concept', '정수 나눗셈으로 잘린 끝자리', 'integer truncation', '#lv1', '사토시 단위 정수로 나누며 버려지는 끝자리. 총량이 2,100만보다 조금 적어지는 이유.', 3, [(BS, 'halving 설명')]),
   ('lab:concept/honest-incentive', 'Concept', '규칙을 지키는 편이 이득', 'incentive to stay honest', '#lv2', '과반 계산력을 가진 공격자도 규칙대로 새 코인을 버는 편이 이득이라는 백서의 논리.', 3, [(WP, '6절')]),
   ('lab:limitation/reward-to-zero', 'Limitation', '보상은 결국 0이 된다', 'subsidy goes to zero', '#lv1', '33번째 반감기에 보상이 0사토시가 되어 새 코인 발행이 끝난다.', 3),
   ('lab:limitation/fee-security-open', 'Limitation', '수수료만으로 보안 비용을 댈 수 있나', 'can fees fund security', '#lv2', '수수료 수준은 거래 수요에 달려 있어 이 모형으로는 답할 수 없다.', 3),
   ('lab:analogy/gold-mine', 'Analogy', '매장량이 정해진 금광 ↔ 반감기', 'finite gold mine ~ halving', '#why', '캘수록 덜 나오고 총량이 정해진 광산.', 3, [(WP, '6절')]),
   ('lab:question/core', 'Question', '아무도 정하지 않는데 총량은 어떻게 정해질까?', 'How is the supply fixed?', '#top', None, 3),
   ('lab:question/duel', 'Question', '사토시까지 더한 값과 2,100만 어림은 얼마나 다를까?', 'Exact total vs 21M', '#duel', None, 3),
  ],
  'edges': [
   ('lab:concept/halving', 'lab:partOf', 'lab:method/halving-schedule', '#lv1'),
   ('lab:term/satoshi', 'lab:partOf', 'lab:method/halving-schedule', '#lv1'),
   ('lab:concept/integer-truncation', 'lab:partOf', 'lab:method/halving-schedule', '#lv1'),
   ('lab:concept/block-reward', 'lab:prerequisiteOf', 'lab:method/halving-schedule', '#lv1'),
   ('lab:method/halving-schedule', 'lab:evaluatedBy', 'lab:metric/total-supply', '#lv1'),
   ('lab:metric/total-supply', 'lab:partOf', 'lab:concept/supply-cap', '#lv1'),
   ('lab:method/halving-schedule', 'lab:hasLimitation', 'lab:limitation/reward-to-zero', '#lv1'),
   ('lab:limitation/reward-to-zero', 'lab:addressedBy', 'lab:method/fee-transition', '#lv2'),
   ('lab:concept/transaction-fee', 'lab:partOf', 'lab:method/fee-transition', '#lv2'),
   ('lab:method/fee-transition', 'lab:evaluatedBy', 'lab:metric/fee-share', '#lv2'),
   ('lab:concept/honest-incentive', 'lab:partOf', 'lab:method/fee-transition', '#lv2'),
   ('lab:method/fee-transition', 'lab:hasLimitation', 'lab:limitation/fee-security-open', '#lv2'),
   ('lab:concept/bitcoin', 'lab:prerequisiteOf', 'lab:concept/supply-cap', '#why'),
   ('lab:metric/total-supply', 'lab:evaluatedBy', 'lab:metric/supply-error', '#duel'),
   ('lab:metric/supply-error', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/reward-to-zero', 'lab:raises', 'lab:question/core', '#lv1'),
   ('lab:analogy/gold-mine', 'lab:analogyOf', 'lab:concept/halving', '#why'),
  ],
  'claims': [
   ('lab:claim/cap-21m', '비트코인이 묶음당 생성되는 양은 50 BTC를 넘지 않으며 총 발행량은 2,100만으로 제한돼 있다', '#why', ['lab:concept/supply-cap'], [(LEC, '교안 p.33')], 'F01'),
   ('lab:claim/four-year', '보통 4년 주기로 보상 감소가 나타나며, 공급이 일정 시점마다 50% 감소한다고 설명할 수 있다', '#lv2', ['lab:concept/halving'], [(LEC, '교안 p.33')], 'F02'),
   ('lab:claim/halving-210k', '블록 보상은 21만 블록마다(약 4년) 절반으로 줄며, 2009년 처음 보상은 50 BTC였다', '#lv1', ['lab:concept/halving', 'lab:method/halving-schedule'], [(BS, 'halving 설명')], 'F03'),
   ('lab:claim/halving-2024', '2024년 4월 19일 840,000번째 블록에서 보상이 6.25에서 3.125 BTC로 줄었다', '#why', ['lab:concept/halving'], [(BS, 'halving 설명')], 'F04'),
   ('lab:claim/truncation', '정수 나눗셈으로 보상이 잘려 최종 총량은 2,100만보다 조금 적고, 마지막 조각은 2140년 무렵 채굴된다', '#lv1', ['lab:concept/integer-truncation', 'lab:metric/total-supply'], [(BS, 'halving 설명')], 'F05'),
   ('lab:claim/fee-transition', '정해진 양의 코인이 유통된 뒤에는 보상이 전부 거래 수수료로 옮겨 가 인플레이션이 없어질 수 있다', '#why', ['lab:method/fee-transition'], [(WP, '6절')], 'F06'),
   ('lab:claim/gold-miners', '새 코인의 꾸준한 추가는 금 캐는 사람이 자원을 들여 금을 유통시키는 것과 비슷하다', '#lv2', ['lab:analogy/gold-mine'], [(WP, '6절')], 'F07'),
   ('lab:claim/greedy-attacker', '탐욕스러운 공격자도 시스템을 무너뜨리기보다 규칙을 지켜 새 코인을 버는 편이 더 이득이라고 본다', '#lv2', ['lab:concept/honest-incentive'], [(WP, '6절')], 'F08'),
  ],
  'sims': [('lab:simulation/halving-sum', '반감기 33번 누적 실험', '#lv1', ['lab:method/halving-schedule']),
           ('lab:simulation/block-revenue', '블록 수입 구성 실험', '#lv2', ['lab:method/fee-transition']),
           ('lab:simulation/duel-total-supply', '총 발행량 대결', '#duel', ['lab:metric/supply-error'])],
 },
}

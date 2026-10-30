LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '3-02', 'slug': 'mining-farms', 'key': '3_02', 'anchor': 'D',
 'tab_title': '채굴장과 중앙화', 'meta_title': '채굴장과 중앙화 — 한 표가 한곳에 모일 때',
 'description': '전기료와 장비 단가의 차이가 채굴을 어떻게 대규모 채굴장으로 모으는지 10년 모형으로 돌려 보고, 상위 채굴자 몇이 손잡으면 과반이 되는지와 그때의 공격 확률을 계산하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인과 비트코인」 p.32; Nakamoto (2008) 4·11절',
 'h1': '채굴장과 중앙화<br>— 한 표가 한곳에 모일 때', 'hero_alt': '책상과 서류가 놓인 사무실을 픽셀로 그린 배경',
 'question': '누구나 채굴할 수 있다면, 왜 채굴은 몇몇 거대한 채굴장으로 모일까? 모이면 무엇이 위험해질까?',
 'lead': '3-01의 비교표는 작업증명의 탈중앙화를 "높음"으로 적었습니다. 그런데 같은 교안의 다음 쪽은 대규모 채굴장과 채굴의 중앙화를 문제로 꼽습니다. 집에서 채굴기 한 대를 돌리는 사람과 수천 대를 한곳에서 돌리는 채굴장의 단가를 비교하고, 10년 동안 계산력이 어디로 모이는지, 그리고 상위 몇 곳이 손잡으면 2-07의 공격 확률이 어떻게 되는지 계산합니다.',
 'kpis': [('고성능 GPU·전용 장비', '경쟁이 치열해지며 채굴자들이 쓰게 된 장비', 'a', [1]), ('수천 대', '한 곳에서 운영하는 채굴장 규모', 'r', [1]), ('분산화 원칙 훼손', '채굴 중앙화의 위험 (교안)', 'r', [1]), ('q ≥ 0.5', '기다려도 막을 수 없는 공격자 몫 (백서 식)', 'm', [2])],
 'hero': [('doc', 'think', 'doc_e09', '"누구나 참여할 수 있다"와 "누구나 이익을 낼 수 있다"는 다른 말이에요. 단가가 다르면 계산력은 싼 쪽으로 흘러가요.'),
          ('asst', 'smile', 'asst_e13', '집 채굴자 마흔 명과 채굴장 세 곳으로 10년 모형을 돌려요. 해마다 누가 남는지 제가 셀게요.'),
          ('fly', 'point', 'fly_e08', '집에서 한 대 돌리는 게 진짜 탈중앙화지. 작은 채굴자가 많을수록 안전하잖아.'),
          ('robo', 'coin', 'robo_e16', '규모의 경제! 크게 돌리면 싸게 먹히는 건 데이터가 말해 줘요.')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '해마다 남은 채굴자를 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 집에서 한 대.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 채굴장 천 대.')],
 'why_title': '왜 채굴장을 보나',
 'why_lead': '2-06은 "계산력 몫 = 표"였어요. 그렇다면 계산력이 어디에 모여 있는지가 곧 표가 어디에 모여 있는지예요.',
 'why': [('장비 경쟁', '작업증명 기반 채굴이 점점 복잡해지고 경쟁이 치열해져 채굴자들은 고성능 GPU나 전용 채굴장비를 사용하게 되었고, 수천 대의 채굴기를 한 곳에서 운영하는 시설이 생겨났다. <sup>[1]</sup>'),
         ('세 가지 문제', '교안은 이 현상이 채굴의 중앙화, 막대한 전력 소비로 인한 환경 문제, 개인 채굴자들의 진입장벽 상승을 낳는다고 정리한다. <sup>[1]</sup>'),
         ('분산화 원칙', '채굴의 중앙화는 블록체인의 분산화 원칙을 훼손할 수 있고, 많은 국가가 채굴장의 전력 소비에 우려를 표명하고 있다. <sup>[1]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 백서의 안전 조건은 "정직한 노드가 계산력 과반"이에요. 과반이 몇 곳에 모이면, 그 몇 곳의 정직함에 기대게 돼요.'),
 'big_lead': '3-01의 "탈중앙화 높음"을 숫자로 다시 재는 칸입니다. 다음 편(3-03)은 채굴자가 이 비용을 내는 이유인 보상과 반감기를 봅니다.',
 'ladder': [('①', '단가가 계산력을 모은다', '전기료·장비 단가 차이 → 10년 뒤 계산력 분포', '분포가 한쪽으로 쏠린다'),
            ('②', '몇 곳이 손잡으면 과반인가', '상위 k곳의 몫 q와 2-07의 공격 확률 P(q, 6)', 'q ≥ 0.5이면 기다려도 소용없다')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '단가와 쏠림', 'title': '싼 쪽으로 흐르는 계산력 — 10년 모형',
   'tags': [('방식: 해마다 수익과 비용을 비교해 남거나 떠나거나 늘림', 'g'), ('현장: 집 채굴기 대 채굴장', '')],
   'left': '<p>동네 빵집 마흔 곳과 큰 공장 세 곳이 같은 빵값을 받는다. 공장은 밀가루를 싸게 사고 전기도 싸다. 빵값이 조금씩 내려가면, 원가가 비싼 빵집부터 문을 닫고 공장은 번 돈으로 기계를 더 들인다.</p>',
   'right': '<p>채굴 경쟁이 치열해지며 전용 장비와 대규모 채굴장이 등장했다. <sup>[1]</sup> 블록 보상은 계산력 몫대로 나뉘므로(2-06), 전체 계산력이 늘면 같은 장비 한 대가 버는 몫은 줄어든다. 단가가 높은 채굴자부터 수익이 비용을 밑돈다.</p>',
   'panel': '''<h3>직접 해 보기 — 집 채굴자 40명, 채굴장 3곳, 10년</h3>
    <div class="cwrap"><canvas id="c1" aria-label="해마다 집 채굴자와 채굴장이 차지한 계산력 몫을 쌓은 막대그래프"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">채굴장 전기료 (집 = 1.0)</span><input type="range" id="r1p" min="40" max="100" step="10" value="50" aria-label="채굴장 전기료 비율"><span class="val" id="v1p">0.5</span></div>
      <div class="group"><span class="glabel">해마다 전체 보상 변화</span><input type="range" id="r1r" min="-20" max="20" step="5" value="-5" aria-label="해마다 전체 보상 변화 퍼센트"><span class="val" id="v1r">−5</span>%</div></div>
    <h3>행동으로 보기 — 해마다 불이 꺼지는 집 채굴기</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="해가 지날수록 집 채굴기의 불이 하나씩 꺼지고 채굴장의 기계가 늘어나는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 단가 차이는 해마다 쌓인다</h4>
    <ol><li>장비 한 대당 수익 = 전체 보상 ÷ 전체 계산력. 모두에게 같다.</li>
      <li>비용은 다르다. 집 채굴자는 사람마다 1.6~2.4(전기료가 다르다), 채굴장은 전기료(기본 0.5) + 장비 0.8(대량 구매). 수익이 비용 아래로 내려가면 단가가 높은 쪽부터 그만둔다.</li>
      <li>채굴장은 남은 이익으로 장비를 더 들여 몫을 키운다. 10년 뒤 계산력은 몇 곳에 몰린다. 교안이 말한 "개인 채굴자들의 진입장벽 상승"이다. <sup>[1]</sup></li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 몫이 몰리면 얼마나 위험한가? 2-07의 공격 확률 식에 넣어 본다. → 몇 곳이 손잡으면 과반인가.</p>''',
   'extra': '<details class="math"><summary>수식으로 보기</summary><p>해마다: 대당 수익 r = R ÷ ΣH. 채굴자 i의 이익 = H<sub>i</sub>(r − c<sub>i</sub>). 집 채굴자는 이익이 0보다 작으면 그만둔다(H = 0). 채굴장은 이익의 절반을 장비 단가 0.8로 나눈 만큼 장비를 늘린다. 첫해 R = 150, 집 40명 각 1대(단가 1.60, 1.62, …, 2.38), 채굴장 8·6·4대. R은 해마다 슬라이더 비율만큼 바뀐다.</p><p class="lim">모든 수치는 예시값이다. 실제 채굴 산업에는 장비 세대 교체, 지역별 전기료, 채굴 풀, 규제 같은 요인이 더 있다.</p></details>',
   'say': ('fly', 'type', 'fly_e09', '첫해엔 집 채굴자가 절반이 넘었는데… 해마다 불이 꺼지네. 남은 건 채굴장 세 곳이야.')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '몇 곳이면 과반', 'title': '상위 몇 곳이 손잡으면 과반인가',
   'tags': [('방식: 몫이 큰 순서로 더해 50%를 넘는 최소 수', 'g'), ('현장: 채굴장 몇 곳의 담합', '')],
   'left': '<p>마을 장부를 아홉 사람이 나눠 들었는데, 알고 보니 그중 일곱 권을 한 집안 세 사람이 들고 있다. 이 세 사람이 입을 맞추면 마을 다수결은 그들의 뜻대로 된다.</p>',
   'right': '<p>백서는 정직한 노드가 계산력 과반을 쥐어야 정직한 사슬이 가장 빨리 자란다고 쓰고, 공격자 몫 q가 정직한 쪽 이상이면 따라잡을 확률이 1이라고 계산한다(2-07). <sup>[2]</sup> 교안은 채굴의 중앙화가 블록체인의 분산화 원칙을 훼손할 수 있다고 쓴다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 상위 k곳이 손잡으면</h3>
    <div class="cwrap"><canvas id="c2" aria-label="채굴자를 몫이 큰 순서로 늘어놓고, 상위 k곳을 묶은 몫과 50% 선을 표시한 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">분포</span><button class="bt" data-dist="y1" aria-pressed="false">①의 첫해</button><button class="bt" data-dist="y10" aria-pressed="true">①의 10년째</button></div>
      <div class="group"><span class="glabel">손잡는 상위 채굴자 수 k</span><input type="range" id="r2k" min="1" max="10" step="1" value="2" aria-label="손잡는 상위 채굴자 수"><span class="val" id="v2k">2</span>곳</div></div>
    <h3>행동으로 보기 — 손잡은 쪽의 사슬과 정직한 사슬</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="손잡은 채굴자들의 사슬과 나머지 정직한 사슬이 각자 몫에 따라 자라는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 과반까지 필요한 수</h4>
    <ol><li>몫이 큰 순서로 더해 처음 50%를 넘는 수가 "과반에 필요한 최소 채굴자 수"다. 이 수가 작을수록 몇 곳의 담합으로 사슬을 좌우할 수 있다.</li>
      <li>①의 첫해 분포에서는 이 수가 크지만, 10년째에는 채굴장 두 곳이면 된다.</li>
      <li>손잡은 몫 q를 2-07의 식에 넣으면 6블록을 기다렸을 때의 공격 성공 확률이 나온다. q가 0.5를 넘는 순간 확률은 1이다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 담합은 할 수 있느냐와 할 이유가 있느냐가 다르다. 채굴자가 왜 정직하게 채굴하는 쪽을 택하는지는 보상 구조에 있다. → 3-03 반감기와 보상.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면 — 분산을 재는 숫자 하나</h4><p>"참여자가 몇 명인가"보다 "몇 명이 손잡으면 과반인가"가 분산의 실제 정도를 더 잘 보여 준다. 수천 명이 참여해도 계산력 대부분이 소수에게 있으면 이 수는 작다. 교안이 대규모 채굴장을 분산화 원칙의 문제로 꼽은 이유다. <sup>[1]</sup></p></div>',
   'say': ('asst', 'e10', 'asst_e10', '10년째 분포에서는 상위 두 곳만 손잡아도 50%를 넘어요. 그러면 6블록을 기다려도 공격 성공 확률은 1이에요.')},
 ],
 'duel': {'title': '집 채굴기 한 대 vs 채굴장, 계산 단가',
  'intro': '초파리는 집에서 채굴기를 돌리고(전기료 1.0, 장비 1.0), Money-Robo는 채굴장에서 같은 기계를 대량으로 돌린다(전기료 0.5, 장비 0.8). 판정 기준은 <b>계산력 한 단위의 연간 비용</b>(예시 단위, 낮을수록 좋음). 위 실험과 같은 비용 함수로 계산한다.',
  'fly': ('집에서 한 대', '작게 여럿이 돌려야 분산이지. 비용도 크게 차이 안 날걸.', '전기료 1.0'),
  'robo': ('채굴장 천 대', '전기는 싸게, 장비는 묶음으로! 단가가 다르죠.', '전기료 0.5'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>단가 = 전기료 × 대당 전력(1) + 장비 단가. 집: 1.0 + 1.0 = 2.0, 채굴장: 0.5 + 0.8 = 1.3. 막대는 2.5를 끝으로 한 선형 눈금이다.</p><p class="lim">예시값이다. 이 대결은 단가만 잰다. 단가가 낮은 쪽이 이긴다는 사실이 바로 ②칸의 쏠림 문제를 낳는다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>교안이 꼽은 문제</th><th>이 페이지에서 본 모습</th></tr></thead><tbody>
   <tr><td>채굴의 중앙화</td><td>10년 모형에서 계산력이 채굴장 세 곳에 몰리고, 과반에 필요한 수가 두 곳으로 줄었다</td></tr>
   <tr><td>막대한 전력 소비와 환경 문제</td><td>3-01: 작업증명은 블록마다 모든 채굴기가 전기를 쓴다</td></tr>
   <tr><td>개인 채굴자의 진입장벽 상승</td><td>단가가 높은 집 채굴자부터 수익이 비용 아래로 내려가 그만둔다</td></tr></tbody></table></div>
   <p class="sub">교안 p.32의 정리를 이 페이지의 실험과 짝지음. <sup>[1]</sup></p>''',
 'summary_say': ('doc', 'front', 'doc_e08', '단가가 계산력을 모으고, 모인 계산력은 과반 문제로 이어져요. 다음 편은 채굴자가 애초에 이 비용을 내는 이유, 보상과 반감기예요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('robo', 'happy', 'robo_e12'), ('fly', 'cry', 'fly_e21'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 Money-Robo가 두 팔을 들고, 초파리 연구원이 폭포 눈물을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 전용 장비와 대규모 채굴장이 등장하며 계산력이 몇 곳으로 모였다.<br>· 단가 차이는 해마다 쌓여 작은 채굴자를 밀어낸다.<br>· "몇 곳이 손잡으면 과반인가"가 작아질수록 분산화 원칙이 약해진다.'),
           ('robo', 'happy', 'robo_e12', '단가 1.3 대 2.0! 규모가 이겼어요.'),
           ('fly', 'cry', 'fly_e21', '…단가로는 못 이겨. 인정. 근데 그게 바로 문제라는 거잖아. 이긴 쪽이 계속 커지니까.'),
           ('asst', 'e16', 'asst_e16', '다음은 3-03, 채굴 보상이 4년마다 반으로 줄어드는 반감기와 2,100만 개 한도를 계산해요.')],
 'kg_hint': '채굴장, 중앙화, 과반, 단가…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인과 비트코인」 p.32 (고성능 GPU·전용 채굴장비, 수천 대 규모의 채굴장, 채굴의 중앙화·환경 문제·진입장벽 상승, 분산화 원칙 훼손, 각국의 우려; 교안이 인용한 보도: 「채굴업자의 경고」 서울경제 2021.04.19). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 4절(정직한 노드의 계산력 과반), 11절(공격자 성공 확률, p ≤ q이면 1). 대학 강의 자료실 사본으로 본문 확인.'],
 'examples': ['10년 모형의 채굴자 수, 장비 수, 전기료·장비 단가, 전체 보상과 변화율 — 모두 예시값', '공격 확률은 2-07과 같은 백서 11절 식으로 계산', '대결: 단가 2.0 대 1.3 (예시 단위)'],
 'gloss_keys': [('채굴장', True), ('채굴 중앙화', True), ('51% 공격', True), ('계산력', False), ('작업증명', False)],
 'gloss_anchor': {'채굴장': '#why', '채굴 중앙화': '#why', '51% 공격': '#lv2', '계산력': '#lv1', '작업증명': '#why'},
 'quiz': {
  'lv1': [{'q': '교안이 대규모 채굴장의 등장으로 생긴 문제로 꼽지 않은 것은?', 'o': ['블록 크기 축소', '채굴의 중앙화', '전력 소비로 인한 환경 문제', '개인 채굴자의 진입장벽 상승'], 'a': 0, 'why': '교안 p.32는 중앙화, 환경 문제, 진입장벽 상승을 꼽아요.', 'hint': '"왜" 카드 둘째.', 'c': 'lab:limitation/mining-centralization'},
          {'q': '이 페이지의 모형에서 전체 계산력이 늘면 장비 한 대가 버는 수익은?', 'o': ['줄어든다', '늘어난다', '그대로다', '0이 된다'], 'a': 0, 'why': '대당 수익 = 전체 보상 ÷ 전체 계산력이라 분모가 커지면 줄어요.', 'hint': '"풀이" 1번.', 'c': 'lab:metric/unit-cost'}],
  'lv2': [{'q': '채굴자 몫이 40%, 15%, 10%, 그리고 나머지가 1%씩이라면 과반에 필요한 최소 채굴자 수는?', 'o': ['2곳', '1곳', '3곳', '35곳'], 'a': 0, 'why': '40% + 15% = 55%로 두 곳이면 50%를 넘어요.', 'hint': '큰 순서로 더해 보세요.', 'c': 'lab:metric/min-colluders'},
          {'q': '손잡은 채굴자 몫 q가 0.55일 때, 6블록을 기다리면 2-07 식의 공격 성공 확률은?', 'o': ['1', '0.0002428', '0.5', '0'], 'a': 0, 'why': 'p ≤ q이면 기다린 블록 수와 관계없이 1이에요.', 'hint': '2-07의 한계.', 'c': 'lab:concept/majority-attack'}]},
 'kgspec': {
  'ladder': ['lab:method/cost-driven-concentration', 'lab:method/collusion-count'],
  'about': ['lab:concept/mining-farm', 'lab:limitation/mining-centralization', 'lab:metric/min-colluders', 'lab:concept/majority-attack'],
  'nodes': [
   ('lab:method/cost-driven-concentration', 'Method', '단가 차이에 따른 계산력 쏠림 모형', 'cost-driven concentration model', '#lv1', '해마다 수익과 단가를 비교해 채굴자가 남거나 떠나거나 장비를 늘리는 모형.', 3),
   ('lab:method/collusion-count', 'Method', '과반 담합 수 세기', 'counting colluders for majority', '#lv2', '몫이 큰 순서로 더해 50%를 넘는 최소 채굴자 수를 구하는 방법.', 3),
   ('lab:metric/unit-cost', 'Metric', '계산력 단가', 'cost per hash unit', '#lv1', '계산력 한 단위를 1년 돌리는 데 드는 비용(전기료 + 장비).', 3),
   ('lab:metric/min-colluders', 'Metric', '과반에 필요한 최소 채굴자 수', 'minimum colluders for majority', '#lv2', '상위 채굴자 몇 곳이 손잡으면 계산력 과반이 되는가.', 4),
   ('lab:concept/economies-of-scale', 'Concept', '규모의 경제', 'economies of scale', '#lv1', '규모가 커질수록 단위당 비용이 낮아지는 현상. 싼 전기와 대량 구매.', 3),
   ('lab:limitation/entry-barrier', 'Limitation', '개인 채굴자의 진입장벽 상승', 'rising entry barrier', '#lv1', '단가가 높은 개인 채굴자는 수익을 내기 어려워진다.', 3, [(LEC, '교안 p.32')]),
   ('lab:metric/attacker-success', 'Metric', '공격 성공 확률 P(q, z)', 'attacker success probability', '#lv2', 'z블록 뒤처진 공격자가 계산력 몫 q로 정직한 사슬을 따라잡을 확률.', 4, [(WP, '11절')]),
   ('lab:analogy/bakery-factory', 'Analogy', '동네 빵집과 공장 ↔ 집 채굴기와 채굴장', 'bakeries vs factory', '#lv1', '같은 값을 받으면 원가가 싼 공장이 남고 커진다.', 3),
   ('lab:analogy/family-ledgers', 'Analogy', '한 집안이 든 장부 일곱 권 ↔ 계산력 쏠림', 'one family holds seven ledgers', '#lv2', '참여자가 많아도 몫이 몇 사람에게 몰리면 다수결은 그들 뜻대로 된다.', 3),
   ('lab:question/core', 'Question', '누구나 채굴할 수 있는데 왜 채굴은 몇 곳에 모일까?', 'Why does mining concentrate?', '#top', None, 3),
   ('lab:question/duel', 'Question', '집 채굴기와 채굴장의 계산 단가는?', 'Home vs farm unit cost', '#duel', None, 3),
  ],
  'edges': [
   ('lab:concept/economies-of-scale', 'lab:partOf', 'lab:method/cost-driven-concentration', '#lv1'),
   ('lab:method/cost-driven-concentration', 'lab:evaluatedBy', 'lab:metric/unit-cost', '#lv1'),
   ('lab:concept/mining-farm', 'lab:partOf', 'lab:method/cost-driven-concentration', '#lv1'),
   ('lab:method/cost-driven-concentration', 'lab:hasLimitation', 'lab:limitation/entry-barrier', '#lv1'),
   ('lab:method/cost-driven-concentration', 'lab:hasLimitation', 'lab:limitation/mining-centralization', '#lv1'),
   ('lab:limitation/mining-centralization', 'lab:addressedBy', 'lab:method/collusion-count', '#lv2', 'mid'),
   ('lab:method/cost-driven-concentration', 'lab:prerequisiteOf', 'lab:method/collusion-count', '#lv2'),
   ('lab:method/collusion-count', 'lab:evaluatedBy', 'lab:metric/min-colluders', '#lv2'),
   ('lab:method/collusion-count', 'lab:evaluatedBy', 'lab:metric/attacker-success', '#lv2'),
   ('lab:metric/hash-rate', 'lab:partOf', 'lab:method/collusion-count', '#lv2'),
   ('lab:concept/majority-attack', 'lab:broader', 'lab:metric/attacker-success', '#lv2'),
   ('lab:method/proof-of-work', 'lab:prerequisiteOf', 'lab:concept/mining-farm', '#why'),
   ('lab:metric/unit-cost', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/mining-centralization', 'lab:raises', 'lab:question/core', '#why'),
   ('lab:analogy/bakery-factory', 'lab:analogyOf', 'lab:concept/economies-of-scale', '#lv1'),
   ('lab:analogy/family-ledgers', 'lab:analogyOf', 'lab:limitation/mining-centralization', '#lv2'),
  ],
  'claims': [
   ('lab:claim/equipment-race', '작업증명 채굴이 복잡해지고 경쟁이 치열해져 채굴자들은 고성능 GPU나 전용 채굴장비를 쓰게 되었고, 수천 대의 채굴기를 한 곳에서 운영하는 시설이 생겨났다', '#why', ['lab:concept/mining-farm'], [(LEC, '교안 p.32')], 'F01'),
   ('lab:claim/three-problems', '대규모 채굴장은 채굴의 중앙화, 막대한 전력 소비로 인한 환경 문제, 개인 채굴자들의 진입장벽 상승을 야기한다', '#why', ['lab:limitation/mining-centralization', 'lab:limitation/entry-barrier'], [(LEC, '교안 p.32')], 'F02'),
   ('lab:claim/decentralization-harm', '채굴의 중앙화는 블록체인의 분산화 원칙을 훼손할 수 있으며, 많은 국가가 채굴장의 전력 소비에 우려를 표명하고 있다', '#why', ['lab:limitation/mining-centralization'], [(LEC, '교안 p.32')], 'F03'),
   ('lab:claim/honest-majority', '정직한 노드가 계산력 과반을 통제하면 정직한 사슬이 가장 빨리 자란다', '#lv2', ['lab:metric/min-colluders'], [(WP, '4절')], 'F04'),
   ('lab:claim/q-ge-p', '공격자 몫이 정직한 쪽 이상이면 따라잡을 확률은 1이다', '#lv2', ['lab:metric/attacker-success', 'lab:concept/majority-attack'], [(WP, '11절')], 'F05'),
  ],
  'sims': [('lab:simulation/ten-year-mining', '집 채굴자·채굴장 10년 모형', '#lv1', ['lab:method/cost-driven-concentration']),
           ('lab:simulation/top-k-collusion', '상위 k곳 담합 실험', '#lv2', ['lab:method/collusion-count']),
           ('lab:simulation/duel-unit-cost', '계산 단가 대결', '#duel', ['lab:metric/unit-cost'])],
 },
}

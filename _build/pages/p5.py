LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '3-05', 'slug': 'pseudonymous-wallet', 'key': '3_05', 'anchor': 'D',
 'tab_title': '익명성과 전자지갑', 'meta_title': '익명성과 전자지갑 — 모두가 보는 장부에서 이름을 숨기는 법',
 'description': '은행과 비트코인이 개인정보를 지키는 방식을 누가 무엇을 보는지로 비교하고, 주소를 다시 쓰거나 여러 조각을 함께 쓸 때 거래가 한 사람으로 묶이는 과정을 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인과 비트코인」 p.35; Nakamoto (2008) 10절',
 'h1': '익명성과 전자지갑<br>— 모두가 보는 장부에서 이름 숨기기', 'hero_alt': '책상과 서류가 놓인 사무실을 픽셀로 그린 배경',
 'question': '모든 거래가 공개되는데, 어떻게 익명일 수 있을까? 그 익명성은 언제 깨질까?',
 'lead': '3-04에서 모든 노드는 모든 거래를 봤습니다. 그런데 교안은 비트코인 거래의 가장 큰 특징 중 하나로 익명성을 꼽습니다. 거래 내역은 공개되지만 개인 신원은 숨겨진다는 것이죠. 은행과 비트코인이 각각 누구에게 무엇을 보여 주는지 비교하고, 그 익명성이 어떤 습관 때문에 깨지는지 직접 묶어 봅니다.',
 'kpis': [('실명 없이', '전자지갑 생성·사용 (교안)', 'a', [1]), ('내역 공개, 신원 숨김', '비트코인의 익명성 (교안)', 'g', [1]), ('거래마다 새 키', '백서가 권하는 습관', 'm', [2]), ('여러 입력', '같은 주인임이 드러나는 거래 (백서)', 'r', [2])],
 'hero': [('doc', 'think', 'doc_e09', '은행은 정보를 감춰서 사생활을 지켜요. 비트코인은 모든 걸 공개해야 하니, 대신 이름과 주소의 연결을 끊어요.'),
          ('asst', 'smile', 'asst_e13', '한 사람이 20번 돈을 받고 몇 번 쓰는 장면을 만들었어요. 주소 하나가 들통나면 몇 건이 묶이는지 제가 셀게요.'),
          ('fly', 'point', 'fly_e08', '주소에 이름이 없다고 끝이 아니야. 같은 주소를 계속 쓰면 다 이어지잖아.'),
          ('robo', 'coin', 'robo_e16', '주소 하나로 다 받으면 관리가 편하죠. 이름은 어차피 안 적히니까요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '묶인 거래를 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 거래마다 새 주소.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 주소 하나로 다 받기.')],
 'why_title': '왜 익명성을 보나',
 'why_lead': '1-06의 은행은 장부를 혼자 들고 있어서 남에게 보여 주지 않으면 그만이었어요. 모두가 장부를 나눠 든 비트코인은 사정이 다릅니다.',
 'why': [('익명성', '사용자들은 실명을 밝히지 않고도 거래할 수 있어 개인정보 보호 측면에서 장점이 있으며, 거래 내역은 공개되지만 개인 신원은 숨겨진다. <sup>[1]</sup>'),
         ('전자지갑', '비트코인 거래에는 전자지갑이 쓰이며, 일반 은행 계좌와 달리 실명 확인 절차 없이 생성하고 사용할 수 있다. 사용자는 고유한 주소를 가진 지갑을 만들어 보관하고 송금한다. <sup>[1]</sup>'),
         ('새 개인정보 모델', '백서는 모든 거래를 공개해야 하므로, 정보 접근을 막는 대신 공개키를 익명으로 유지해 개인정보를 지킨다고 쓴다. 사람들은 누군가가 누군가에게 얼마를 보냈는지는 보지만 그것을 사람과 연결하지는 못한다. <sup>[2]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 엄밀히는 익명보다 "가명"에 가까워요. 주소라는 가명이 사람과 이어지는 순간, 그 가명으로 한 일이 모두 드러나요.'),
 'big_lead': '3-04의 "모든 노드가 모든 거래를 본다"는 한계에서 시작하는 칸입니다. 다음 편(3-06)은 이렇게 거래되는 비트코인이 화폐인지를 따집니다.',
 'ladder': [('①', '누가 무엇을 보나', '은행 모델과 비트코인 모델의 정보 흐름 비교', '주소와 사람의 연결이 끊겨 있어야만 성립'),
            ('②', '묶이는 거래', '주소 재사용과 여러 입력 거래가 거래를 한 사람으로 묶는다', '한 번 드러나면 묶인 거래가 함께 드러난다 → 3-07 추적')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '누가 무엇을 보나', 'title': '감추는 모델과 끊는 모델',
   'tags': [('방식: 보는 사람마다 볼 수 있는 항목을 비교', 'g'), ('현장: 은행 창구 대 공개 게시판', '')],
   'left': '<p>은행 창구에서는 내 이름과 금액을 은행과 상대방만 안다. 옆 사람은 모른다. 반면 공개 게시판에는 모든 송금이 붙는다. 대신 이름 대신 별명만 적힌다. 게시판을 보는 사람은 "별명 7번이 별명 12번에게 3만 원"까지만 안다.</p>',
   'right': '<p>백서는 전통적인 은행 모델이 정보 접근을 당사자와 신뢰받는 제3자로 제한해 개인정보를 지킨다고 쓴다. 비트코인은 모든 거래를 공개해야 하므로 이 방법을 쓸 수 없고, 대신 공개키를 익명으로 유지해 신원과 거래 사이의 연결을 끊는다. 이는 증권거래소가 거래 시각과 규모는 공개하되 당사자는 밝히지 않는 것과 비슷하다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 보는 사람을 바꿔 보기</h3>
    <div class="cwrap"><canvas id="c1" aria-label="전통적 모델과 비트코인 모델에서 신원, 거래, 제3자, 상대방, 대중 사이의 정보 흐름과 끊긴 지점을 그린 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">보는 사람</span><button class="bt" data-who="public" aria-pressed="true">아무나 (대중)</button><button class="bt" data-who="party" aria-pressed="false">거래 상대</button><button class="bt" data-who="third" aria-pressed="false">은행·중개자</button></div></div>
    <h3>행동으로 보기 — 그 사람의 화면</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="선택한 사람이 은행 모델과 비트코인 모델에서 각각 볼 수 있는 항목을 화면처럼 보여 주는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 숨기는 곳이 다르다</h4>
    <ol><li>은행 모델은 거래 내역을 감춘다. 대중은 아무것도 못 보지만, 은행은 이름과 금액을 모두 안다.</li>
      <li>비트코인 모델은 내역을 공개하고 이름을 뺀다. 대중도 금액·시각·주소를 보지만, 주소가 누구인지는 모른다. 교안이 말한 "거래 내역은 공개되지만 개인 신원은 숨겨진다"다. <sup>[1]</sup></li>
      <li>그래서 비트코인의 익명성은 "주소와 사람의 연결이 끊겨 있다"는 한 가지 조건에 기대고 있다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 그 연결은 언제 이어지나? 같은 주소를 계속 쓰거나, 여러 주소의 조각을 한 거래에 함께 쓸 때. → 묶이는 거래.</p>''',
   'extra': '<details class="math"><summary>표로 보기</summary><p>은행 모델 — 대중: 없음 / 상대방: 이름·금액·시각 / 은행: 이름·금액·시각·계좌 전체. 비트코인 모델 — 대중: 금액·시각·주소 / 상대방: 금액·시각·주소(+ 상대가 알려 준 정보) / 중개자: 없음(거래소 등을 거치면 그 사업자가 아는 정보).</p><p class="lim">이 표는 백서 10절의 두 모델을 단순화했다. 실제로는 지갑·거래소·네트워크 정보 등으로 연결이 생길 수 있다.</p></details>',
   'say': ('fly', 'type', 'fly_e09', '대중 화면을 보면 은행 쪽은 텅 비었고, 비트코인 쪽은 금액이랑 주소까지 다 보여. 이름만 빠졌어.')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '묶이는 거래', 'title': '한 번 드러나면 줄줄이 — 주소 재사용과 여러 입력',
   'tags': [('방식: 같은 주인으로 보이는 주소를 묶어 덩어리로 만듦', 'g'), ('현장: 별명 하나가 들통난 게시판', '')],
   'left': '<p>게시판에 별명 하나로 스무 번 돈을 받았다. 택배를 받으려고 그 별명과 주소를 쇼핑몰에 한 번 알려 줬다. 이제 그 쇼핑몰은 스무 건을 모두 내 것으로 안다. 별명을 매번 바꿨다면? 대신 두 별명으로 받은 돈을 한 번에 모아 쓰면, 그 두 별명은 같은 사람으로 묶인다.</p>',
   'right': '<p>백서는 추가 방화벽으로 거래마다 새 키 쌍을 써서 공통의 주인과 연결되지 않게 하라고 권한다. 다만 여러 입력을 가진 거래는 그 입력들이 같은 주인의 것임을 드러낼 수밖에 없고, 키의 주인이 드러나면 연결된 다른 거래들까지 드러날 위험이 있다고 쓴다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 받은 돈 20건, 주소 하나가 드러나면</h3>
    <div class="cwrap"><canvas id="c2" aria-label="받은 거래 20건의 주소를 점으로 놓고, 여러 입력 거래로 묶인 주소를 선으로 잇고, 드러난 주소와 이어진 덩어리를 강조한 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">받는 방식</span><button class="bt" data-mode="fresh" aria-pressed="true">거래마다 새 주소</button><button class="bt" data-mode="reuse" aria-pressed="false">주소 하나 재사용</button></div>
      <div class="group"><span class="glabel">여러 조각을 모아 쓴 횟수</span><input type="range" id="r2m" min="0" max="10" step="1" value="4" aria-label="여러 입력 거래 횟수"><span class="val" id="v2m">4</span>번</div>
      <div class="group"><button class="bt" id="b2Leak">드러난 주소 바꾸기</button></div></div>
    <h3>행동으로 보기 — 들통난 하나에서 퍼지는 연결</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="드러난 주소 하나에서 같은 덩어리의 주소로 빨간 표시가 퍼져 나가는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 덩어리의 크기가 피해의 크기</h4>
    <ol><li>주소 하나를 재사용하면 20건이 처음부터 한 덩어리다. 그 주소가 드러나면 20건이 모두 드러난다.</li>
      <li>거래마다 새 주소를 쓰면 처음에는 20개의 작은 덩어리다. 하지만 여러 조각을 모아 한 번에 쓸 때마다(3-04의 입력 여럿) 그 주소들이 한 덩어리로 묶인다.</li>
      <li>드러난 주소가 속한 덩어리의 크기만큼 거래가 함께 드러난다. 모아 쓰기를 많이 할수록 새 주소의 효과는 줄어든다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 이 "묶기"는 거꾸로 수사에도 쓰인다. 범죄 자금이 공개 장부 위에서 어떻게 추적되는지는 → 3-07.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면 — 익명성의 두 얼굴</h4><p>교안은 익명성 덕분에 사용자들이 더 자유롭게 금융 활동을 하고 정부·은행 등의 통제에서 벗어날 수 있다고 쓰는 한편 <sup>[1]</sup>, 같은 성질이 범죄에 악용된다고도 쓴다(3-07). 공개 장부라는 점은 그대로이므로, 주소와 사람의 연결이 한 번 생기면 과거 거래까지 거슬러 볼 수 있다는 점도 함께 기억할 만하다.</p></div>',
   'say': ('asst', 'e10', 'asst_e10', '새 주소를 써도 모아 쓰기를 네 번 하니 드러난 주소와 같은 덩어리가 생겼어요. 재사용이면 처음부터 20건이 한 덩어리고요.')},
 ],
 'duel': {'title': '주소 하나가 드러났을 때, 함께 드러나는 거래',
  'intro': '같은 사람이 돈을 20번 받고, 그중 일부를 네 번에 걸쳐 모아 쓴다. 초파리는 거래마다 새 주소로, Money-Robo는 주소 하나로 받는다. 첫 모아 쓰기에 쓰인 주소 하나가 쇼핑몰에 알려졌다. 판정 기준은 <b>그 사람의 것으로 묶여 드러나는 받은 거래 수</b>(적을수록 좋음). 위 실험과 같은 묶기 함수, 시드 35.',
  'fly': ('거래마다 새 주소', '하나가 드러나도 나머지까지 엮이진 않게 해야지.', '주소 20개'),
  'robo': ('주소 하나 재사용', '주소 하나면 관리가 편해요. 이름도 안 적히고!', '주소 1개'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>새 주소 쪽: 주소 20개에서 시작해, 모아 쓰기 4번(각각 무작위 주소 2~3개를 함께 입력으로 씀, 시드 35)마다 그 주소들을 한 덩어리로 합친다. 드러난 주소가 속한 덩어리의 크기를 센다. 재사용 쪽: 처음부터 20건이 한 주소다. 막대는 20을 끝으로 한 선형 눈금이다.</p><p class="lim">모아 쓰기 외의 연결 단서(금액, 시각, 거스름돈 주소의 패턴 등)는 넣지 않았다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>보는 사람</th><th>은행 모델</th><th>비트코인 모델</th></tr></thead><tbody>
   <tr><td>아무나 (대중)</td><td>볼 수 없음</td><td>금액·시각·주소 (이름 없음)</td></tr>
   <tr><td>거래 상대</td><td>이름·금액·시각</td><td>금액·시각·주소, 그리고 상대가 따로 알려 준 정보</td></tr>
   <tr><td>은행·중개자</td><td>이름·금액·시각·계좌 전체</td><td>없음 (중개자를 거치면 그 사업자가 아는 정보)</td></tr>
   <tr><td>지키는 방법</td><td>정보 접근을 당사자와 제3자로 제한</td><td>공개키를 익명으로 유지, 거래마다 새 키</td></tr>
   <tr><td>깨지는 경우</td><td>제3자가 유출하거나 넘겨줄 때</td><td>주소와 사람이 한 번 연결될 때 (재사용, 여러 입력)</td></tr></tbody></table></div>
   <p class="sub">백서 10절의 두 모델과 권고를 표로 정리. <sup>[2]</sup></p>''',
 'summary_say': ('doc', 'front', 'doc_e08', '비트코인은 내역을 공개하고 이름을 빼요. 그 익명성은 주소와 사람이 이어지지 않을 때만 성립해요. 다음 편은 이런 비트코인이 과연 화폐인지 따져 봐요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('fly', 'arms', 'fly_e16'), ('robo', 'sigh', 'robo_e20'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 초파리 연구원이 팔짱을 끼고, Money-Robo가 식은땀을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 비트코인은 거래 내역을 공개하고, 이름 대신 주소를 적는다.<br>· 전자지갑은 실명 확인 없이 만들 수 있다.<br>· 주소를 다시 쓰거나 여러 조각을 모아 쓰면 거래가 한 사람으로 묶인다.'),
           ('fly', 'arms', 'fly_e16', '새 주소로 받았더니 20건 중 8건만 드러났어. 그 8건도 모아 쓰기로 묶인 거고.'),
           ('robo', 'sigh', 'robo_e20', '주소 하나 들통에 스무 건이 줄줄이… 편한 게 다가 아니었네요.'),
           ('asst', 'e16', 'asst_e16', '다음은 3-06, 비트코인이 화폐의 세 기능을 하는지, 가치는 어디서 오는지 따져 봐요.')],
 'kg_hint': '익명성, 전자지갑, 주소, 재사용…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인과 비트코인」 p.35 (비트코인 거래의 익명성, 거래 내역 공개와 신원 숨김, 통제에서 벗어난 금융 활동, 실명 확인 없는 전자지갑과 고유 주소). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 10절(전통 은행 모델과 새 개인정보 모델, 공개키의 익명 유지, 증권거래소 비유, 거래마다 새 키 쌍, 여러 입력 거래가 같은 주인을 드러냄, 주인이 드러나면 연결된 거래도 드러날 위험). HackerNoon 재수록본으로 확인.'],
 'examples': ['받은 거래 20건, 모아 쓰기 횟수와 묶이는 주소(시드 35) — 예시값', '보는 사람별 항목표 — 백서 10절을 단순화', '대결: 모아 쓰기 4번, 드러난 주소는 첫 모아 쓰기에 쓰인 주소로 고정'],
 'gloss_keys': [('익명성', True), ('전자지갑', True), ('주소', True), ('주소 재사용', True), ('중개자', False)],
 'gloss_anchor': {'익명성': '#why', '전자지갑': '#why', '주소': '#lv1', '주소 재사용': '#lv2', '중개자': '#lv1'},
 'quiz': {
  'lv1': [{'q': '교안이 설명한 비트코인 익명성의 내용은?', 'o': ['거래 내역은 공개되지만 개인 신원은 숨겨진다', '거래 내역도 신원도 모두 숨겨진다', '신원은 공개되고 거래 내역은 숨겨진다', '은행만 거래를 볼 수 있다'], 'a': 0, 'why': '교안 p.35.', 'hint': '"왜" 카드 첫째.', 'c': 'lab:concept/pseudonymity'},
          {'q': '백서가 비트코인 개인정보 모델을 비유한 대상은?', 'o': ['거래 시각과 규모는 공개하되 당사자는 밝히지 않는 증권거래소 정보', '은행 비밀번호', '봉인된 편지', '익명 투표함'], 'a': 0, 'why': '백서 10절의 비유예요.', 'hint': '①의 "방식" 설명.', 'c': 'lab:method/public-key-privacy'}],
  'lv2': [{'q': '백서가 개인정보를 위해 권한 습관은?', 'o': ['거래마다 새 키 쌍을 쓴다', '주소 하나를 오래 쓴다', '거래를 공개하지 않는다', '은행을 거친다'], 'a': 0, 'why': '공통의 주인과 연결되지 않게 하려는 추가 방화벽이에요.', 'hint': 'KPI 셋째.', 'c': 'lab:limitation/key-reuse'},
          {'q': '새 주소를 써도 여러 주소의 조각을 한 거래에 함께 쓰면?', 'o': ['그 주소들이 같은 주인으로 묶인다', '아무 일도 없다', '주소가 사라진다', '거래가 거부된다'], 'a': 0, 'why': '여러 입력 거래는 입력들이 같은 주인의 것임을 드러내요(백서 10절).', 'hint': '②의 선.', 'c': 'lab:method/address-clustering'}]},
 'kgspec': {
  'ladder': ['lab:method/public-key-privacy', 'lab:method/address-clustering'],
  'about': ['lab:concept/pseudonymity', 'lab:concept/wallet', 'lab:limitation/key-reuse', 'lab:method/address-clustering'],
  'nodes': [
   ('lab:method/public-key-privacy', 'Method', '공개키를 익명으로 유지하는 개인정보 모델', 'public-key privacy model', '#lv1', '거래는 공개하되 공개키(주소)와 신원의 연결을 끊어 개인정보를 지키는 방식.', 4, [(WP, '10절')]),
   ('lab:method/traditional-privacy', 'Method', '전통적 은행 개인정보 모델', 'traditional privacy model', '#lv1', '정보 접근을 당사자와 신뢰받는 제3자로 제한하는 방식.', 3, [(WP, '10절')]),
   ('lab:method/address-clustering', 'Method', '주소 묶기 (같은 주인 추정)', 'address clustering', '#lv2', '재사용된 주소나 여러 입력 거래를 근거로 주소들을 같은 주인의 덩어리로 묶는 방법.', 4),
   ('lab:method/fresh-keys', 'Method', '거래마다 새 키 쌍', 'fresh key per transaction', '#lv2', '거래마다 새 주소를 써서 공통의 주인과 연결되지 않게 하는 습관.', 3, [(WP, '10절')]),
   ('lab:limitation/multi-input-link', 'Limitation', '여러 입력 거래의 연결', 'multi-input linking', '#lv2', '여러 입력을 가진 거래는 그 입력들이 같은 주인의 것임을 드러낸다.', 4, [(WP, '10절')]),
   ('lab:metric/linked-transactions', 'Metric', '함께 드러나는 거래 수', 'linked transactions exposed', '#duel', '주소 하나가 드러났을 때 같은 주인으로 묶여 드러나는 받은 거래의 수.', 4),
   ('lab:metric/visible-fields', 'Metric', '보는 사람별 보이는 항목', 'visible fields per viewer', '#lv1', '대중·상대방·중개자가 각 모델에서 볼 수 있는 이름·금액·시각·주소.', 3),
   ('lab:analogy/nickname-board', 'Analogy', '별명이 적힌 공개 게시판 ↔ 비트코인 거래', 'nickname board ~ bitcoin ledger', '#lv1', '모든 송금이 붙지만 이름 대신 별명만 적힌다.', 3),
   ('lab:analogy/stock-tape', 'Analogy', '증권거래소 공개 정보 ↔ 새 개인정보 모델', 'stock exchange tape', '#lv1', '거래 시각과 규모는 공개하되 당사자는 밝히지 않는다.', 3, [(WP, '10절')]),
   ('lab:question/core', 'Question', '모든 거래가 공개되는데 어떻게 익명일 수 있을까?', 'How can a public ledger be anonymous?', '#top', None, 3),
   ('lab:question/duel', 'Question', '주소 하나가 드러나면 거래 몇 건이 함께 드러날까?', 'How many transactions are exposed?', '#duel', None, 3),
  ],
  'edges': [
   ('lab:method/public-key-privacy', 'lab:contrastsWith', 'lab:method/traditional-privacy', '#lv1'),
   ('lab:concept/trusted-third-party', 'lab:partOf', 'lab:method/traditional-privacy', '#lv1'),
   ('lab:term/address', 'lab:partOf', 'lab:method/public-key-privacy', '#lv1'),
   ('lab:concept/pseudonymity', 'lab:broader', 'lab:method/public-key-privacy', '#why'),
   ('lab:concept/wallet', 'lab:partOf', 'lab:method/public-key-privacy', '#why'),
   ('lab:method/public-key-privacy', 'lab:evaluatedBy', 'lab:metric/visible-fields', '#lv1'),
   ('lab:method/public-key-privacy', 'lab:hasLimitation', 'lab:limitation/key-reuse', '#lv2'),
   ('lab:method/public-key-privacy', 'lab:hasLimitation', 'lab:limitation/multi-input-link', '#lv2'),
   ('lab:limitation/key-reuse', 'lab:addressedBy', 'lab:method/fresh-keys', '#lv2'),
   ('lab:limitation/multi-input-link', 'lab:prerequisiteOf', 'lab:method/address-clustering', '#lv2'),
   ('lab:limitation/key-reuse', 'lab:prerequisiteOf', 'lab:method/address-clustering', '#lv2'),
   ('lab:method/address-clustering', 'lab:evaluatedBy', 'lab:metric/linked-transactions', '#lv2'),
   ('lab:method/fresh-keys', 'lab:evaluatedBy', 'lab:metric/linked-transactions', '#duel'),
   ('lab:metric/linked-transactions', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/key-reuse', 'lab:raises', 'lab:question/core', '#lv2'),
   ('lab:analogy/nickname-board', 'lab:analogyOf', 'lab:concept/pseudonymity', '#lv1'),
   ('lab:analogy/stock-tape', 'lab:analogyOf', 'lab:method/public-key-privacy', '#lv1'),
  ],
  'claims': [
   ('lab:claim/anonymity', '사용자들은 실명을 밝히지 않고도 거래할 수 있으며, 거래 내역은 공개되지만 개인 신원은 숨겨진다', '#why', ['lab:concept/pseudonymity'], [(LEC, '교안 p.35')], 'F01'),
   ('lab:claim/wallet-no-kyc', '전자지갑은 일반 은행 계좌와 달리 실명 확인 절차 없이 생성하고 사용할 수 있으며, 고유한 주소를 가진다', '#why', ['lab:concept/wallet', 'lab:term/address'], [(LEC, '교안 p.35')], 'F02'),
   ('lab:claim/freedom-from-control', '익명성으로 사용자들은 더 자유롭게 금융 활동을 할 수 있으며 정부·은행 등의 통제에서 벗어날 수 있다', '#lv2', ['lab:concept/pseudonymity'], [(LEC, '교안 p.35')], 'F03'),
   ('lab:claim/new-privacy-model', '모든 거래를 공개해야 하므로 공개키를 익명으로 유지해 개인정보를 지키며, 이는 증권거래소가 당사자를 밝히지 않고 거래 시각과 규모를 공개하는 것과 비슷하다', '#lv1', ['lab:method/public-key-privacy', 'lab:analogy/stock-tape'], [(WP, '10절')], 'F04'),
   ('lab:claim/fresh-key', '거래마다 새 키 쌍을 써서 공통의 주인과 연결되지 않게 해야 한다', '#lv2', ['lab:method/fresh-keys'], [(WP, '10절')], 'F05'),
   ('lab:claim/multi-input', '여러 입력 거래는 입력들이 같은 주인의 것임을 드러내며, 키의 주인이 드러나면 연결된 다른 거래도 드러날 수 있다', '#lv2', ['lab:limitation/multi-input-link', 'lab:metric/linked-transactions'], [(WP, '10절')], 'F06'),
  ],
  'sims': [('lab:simulation/viewer-screens', '보는 사람별 화면 비교', '#lv1', ['lab:method/public-key-privacy']),
           ('lab:simulation/cluster-20', '받은 거래 20건 묶기 실험', '#lv2', ['lab:method/address-clustering']),
           ('lab:simulation/duel-exposure', '드러나는 거래 수 대결', '#duel', ['lab:metric/linked-transactions'])],
 },
}

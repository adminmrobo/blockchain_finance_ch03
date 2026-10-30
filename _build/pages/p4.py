LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '3-04', 'slug': 'tx-is-the-note', 'key': '3_04', 'anchor': 'C',
 'tab_title': '거래가 곧 증서', 'meta_title': '거래가 곧 증서 — 지갑 속 비트코인은 어떤 모양일까',
 'description': '비트코인의 잔액이 "쓰지 않은 거래 결과" 조각들로 이루어져 있음을 직접 송금하며 보고, 거래가 네트워크에 퍼지고 이중 지불이 걸러지는 과정을 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인과 비트코인」 p.34; Nakamoto (2008) 5·9절',
 'h1': '거래가 곧 증서<br>— 지갑 속 비트코인은 어떤 모양일까', 'hero_alt': '금화와 장부가 쌓인 회계실을 픽셀로 그린 배경',
 'question': '비트코인 지갑에는 "잔액 0.7 BTC"가 적힌 칸이 있을까? 송금하면 장부에는 무엇이 남을까?',
 'lead': '2-04에서 블록체인은 잔액을 덮어쓰지 않고 이력을 쌓았습니다. 비트코인은 그 생각을 끝까지 밀고 갑니다. 교안은 일반 장부가 수표·영수증 같은 증서의 교환 내역을 적는 반면, 블록체인은 그 자체가 거래장부이자 거래증서라고 설명합니다. 지갑 속 비트코인이 어떤 조각으로 되어 있는지 직접 송금하며 보고, 그 거래가 네트워크에 어떻게 퍼지는지 봅니다.',
 'kpis': [('장부 = 증서', '블록체인은 거래장부이자 거래증서 (교안)', 'a', [1]), ('지불되지 않은 결과', '비트코인 거래가 존재하는 형태', 'g', [1]), ('입력 여럿, 출력 둘', '보통의 거래: 지불 + 거스름돈 (백서)', 'm', [2]), ('검증 → 추가 → 전파', '거래를 받은 노드가 하는 일', 'r', [1])],
 'hero': [('doc', 'think', 'doc_e09', '지갑에 "잔액" 칸은 없어요. 아직 쓰지 않은 거래 결과들이 있을 뿐이에요. 잔액은 그것들을 더한 값이에요.'),
          ('asst', 'smile', 'asst_e13', '조각 네 개가 든 지갑으로 직접 송금해 볼게요. 쓴 조각과 새로 생긴 조각을 제가 셀게요.'),
          ('fly', 'point', 'fly_e08', '은행처럼 원장에 적고 확인증도 따로 떼 주는 게 확실하지 않아?'),
          ('robo', 'coin', 'robo_e16', '거래 자체가 증서면 서류가 확 줄죠. 효율이 답이에요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '조각과 문서를 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 은행식 원장 + 확인증.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 거래가 곧 증서.')],
 'why_title': '왜 거래의 모양을 보나',
 'why_lead': '1장에서 돈은 "장부의 숫자"였어요(1-01). 비트코인에서 그 숫자는 어디에 어떤 모양으로 적혀 있을까요?',
 'why': [('장부이자 증서', '일반적인 장부에는 수표나 영수증, 약속어음의 교환 내역이 기록되는 반면, 블록체인은 그 자체가 거래장부인 동시에 거래증서다. <sup>[1]</sup>'),
         ('지불되지 않은 결과', '비트코인에서는 각 거래가 지불되지 않은 결과의 형태로 존재한다고 표현한다. <sup>[1]</sup> 백서는 값을 나누고 합칠 수 있도록 거래에 여러 입력과 출력을 둔다. <sup>[2]</sup>'),
         ('퍼지는 거래', '거래는 지갑 앱을 통해 네트워크에 뿌려지고, 네트워크의 컴퓨터들은 거래를 검증한 다음 자신의 장부에 추가하고, 다른 컴퓨터들에게도 뿌린다. <sup>[1]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 은행에서는 원장과 확인증이 따로 있어 서로 맞춰 봐야 해요. 비트코인에서는 거래 하나가 둘 다예요.'),
 'big_lead': '2장의 블록과 사슬 안에 실제로 무엇이 들어가는지 보는 칸입니다. 다음 편(3-05)은 이 거래에 이름 대신 무엇이 적히는지, 익명성을 봅니다.',
 'ladder': [('①', '조각으로 된 잔액', '입력 조각을 쓰고, 지불과 거스름돈 조각을 새로 만든다', '이 거래가 진짜인지 누가 확인하나'),
            ('②', '퍼지고 걸러지는 거래', '노드가 검증·추가·전파, 이중 지불은 먼저 본 것 + 블록으로 정리', '받는 사람은 블록에 담길 때까지 기다려야 한다(2-07)')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '조각으로 된 잔액', 'title': '잔액은 조각들의 합 — 쓰지 않은 거래 결과',
   'tags': [('방식: 입력 조각을 통째로 쓰고 출력 조각을 새로 만듦', 'g'), ('장부: 금화 대신 액면이 적힌 증서 묶음', '')],
   'left': '<p>지갑에 액면이 적힌 증서 네 장이 있다. 0.7을 내야 하는데 딱 맞는 증서가 없다. 0.5짜리와 0.3짜리를 함께 내면, 받는 쪽 이름으로 0.7짜리 새 증서가, 내 이름으로 거스름 증서가 새로 생긴다. 낸 증서는 찢어져 다시 못 쓴다.</p>',
   'right': '<p>값을 나누고 합칠 수 있도록 거래에는 여러 입력과 출력이 있다. 보통은 큰 이전 거래 하나나 작은 여러 개를 입력으로 쓰고, 출력은 많아야 둘이다. 하나는 지불, 하나는 거스름돈을 보낸 사람에게 되돌린다. <sup>[2]</sup> 아직 쓰지 않은 출력이 교안이 말한 "지불되지 않은 결과"다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 지갑의 조각으로 송금하기</h3>
    <div class="cwrap"><canvas id="c1" aria-label="송금에 쓰인 입력 조각과 새로 생긴 지불·거스름돈 출력 조각을 왼쪽에서 오른쪽으로 잇는 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">보낼 금액 (BTC)</span><input type="range" id="r1a" min="1" max="19" step="1" value="14" aria-label="보낼 금액"><span class="val" id="v1a">0.70</span></div>
      <div class="group"><span class="glabel">조각 고르기</span><button class="bt" data-pick="big" aria-pressed="true">큰 조각부터</button><button class="bt" data-pick="small" aria-pressed="false">작은 조각부터</button></div>
      <div class="group"><button class="bt primary" id="b1Send">▶ 보내기</button><button class="bt" id="b1Reset">지갑 처음으로</button></div></div>
    <h3>행동으로 보기 — 찢어지는 증서와 새로 생기는 증서</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="입력으로 쓴 증서가 찢어지고 지불·거스름 증서가 새로 생기는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 입력 = 출력 + 수수료</h4>
    <ol><li>입력 조각은 나눠 쓸 수 없고 통째로 쓴다. 보낼 금액보다 크면 남는 만큼 거스름돈 출력이 생긴다.</li>
      <li>입력 합계 − 출력 합계가 수수료다(3-03). 이 페이지는 수수료를 0.001 BTC로 두었다.</li>
      <li>보내고 나면 지갑의 조각 구성이 바뀐다. 잔액은 남은 조각과 거스름돈을 더한 값이다. "잔액" 칸을 고치는 것이 아니라 증서를 새로 쓰는 것이다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 같은 조각을 두 사람에게 동시에 보내면? 누가 그 거래를 확인하고 하나만 남기나? → 퍼지고 걸러지는 거래.</p>''',
   'extra': '<details class="math"><summary>수식으로 보기</summary><p>입력 집합 I를 "큰 조각부터"(또는 작은 조각부터) 골라 Σ<sub>I</sub> ≥ 금액 + 수수료가 될 때까지 더한다. 출력: 지불 = 금액, 거스름돈 = Σ<sub>I</sub> − 금액 − 수수료(0이면 생략). 처음 지갑 조각은 0.5, 0.3, 0.15, 0.05 BTC.</p><p class="lim">조각 구성과 수수료는 예시값이다. 실제 지갑은 수수료, 거래 크기, 개인정보를 함께 고려해 조각을 고른다.</p></details>',
   'say': ('fly', 'type', 'fly_e09', '0.7을 보내려고 0.5와 0.3을 통째로 냈어. 0.099 BTC는 거스름 조각으로 돌아왔고. 잔액 칸 같은 건 어디에도 없네.')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '퍼지는 거래', 'title': '퍼지고 걸러지는 거래 — 검증, 추가, 전파',
   'tags': [('방식: 받은 거래를 검증해 내 장부에 넣고 이웃에게 전달', 'g'), ('장부: 마을 장부 서른 권에 소문처럼 퍼지는 기록', '')],
   'left': '<p>마을 장부 서른 권이 있다. 누가 "갑이 을에게 보냈다"는 쪽지를 한 집에 건네면, 그 집은 쪽지가 맞는지 보고 자기 장부에 옮긴 뒤 이웃집에 쪽지를 전한다. 같은 증서로 두 사람에게 보낸 쪽지가 마을 양쪽 끝에서 동시에 돌면, 집마다 먼저 받은 쪽만 적는다.</p>',
   'right': '<p>지갑 앱이 거래를 네트워크에 뿌리면 컴퓨터들은 거래를 검증하고 장부에 추가한 뒤 다른 컴퓨터에도 뿌린다. <sup>[1]</sup> 백서의 순서: 새 거래를 모든 노드에 전파하고, 노드는 거래를 블록에 모아 작업증명을 하고, 블록을 찾으면 전파한다. 노드는 블록의 거래가 모두 유효하고 이미 쓰인 것이 아닐 때만 받아들인다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 노드 30개 망에 거래 뿌리기</h3>
    <div class="cwrap"><canvas id="c2" aria-label="노드 30개 망에서 거래가 홉마다 퍼지고, 이중 지불 시 노드마다 먼저 받은 거래가 색으로 표시되는 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">시나리오</span><button class="bt" data-sc="one" aria-pressed="true">정상 거래 하나</button><button class="bt" data-sc="double" aria-pressed="false">같은 조각으로 두 거래 (이중 지불)</button></div>
      <div class="group"><button class="bt primary" id="b2Go">▶ 뿌리기</button></div></div>
    <h3>행동으로 보기 — 다음 블록이 정리한다</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="다음 블록을 찾은 노드의 거래만 블록에 담기고 나머지는 무효가 되는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 소문은 갈라져도 블록은 하나</h4>
    <ol><li>거래는 홉마다 이웃으로 퍼져 몇 홉 안에 망 전체에 닿는다(1-02의 그물형).</li>
      <li>같은 조각을 쓰는 두 거래가 동시에 퍼지면 망이 갈라진다. 노드마다 먼저 받은 거래만 유효로 본다.</li>
      <li>다음 블록을 찾은 노드가 담은 거래가 사슬에 들어가고, 다른 쪽 거래는 이미 쓰인 조각을 쓴 것이 되어 거부된다. 그래서 받는 사람은 블록에 담기고 그 뒤에 블록이 쌓일 때까지 기다린다(2-07).</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 모든 노드가 모든 거래를 본다. 그렇다면 내 거래도 모두에게 보인다는 뜻이다. → 3-05 익명성과 전자지갑.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면 — 은행 이체와 비트코인 이체</h4><p>교안은 은행의 계좌 이체 프로세스를 "거래내역 및 거래증서", 비트코인의 이체 프로세스를 "거래내역만 존재"로 대비한다. <sup>[1]</sup> 은행은 보내는 은행과 받는 은행의 원장, 그리고 확인증을 서로 맞춰야 하지만, 비트코인 거래는 그 하나가 내역이자 증서다. 대신 그 하나를 망 전체가 검증한다.</p></div>',
   'say': ('asst', 'e10', 'asst_e10', '이중 지불 시나리오에서 망이 두 쪽으로 갈렸지만, 다음 블록이 담은 거래 하나만 남았어요.')},
 ],
 'duel': {'title': '거래 1,000건, 생기는 문서 수',
  'intro': '송금 1,000건을 처리한다. 초파리는 은행식(보내는 은행 원장 기록 + 받는 은행 원장 기록 + 이체 확인증), Money-Robo는 비트코인식(거래 하나가 내역이자 증서). 판정 기준은 <b>서로 맞춰 봐야 할 서로 다른 문서 수</b>(같은 문서의 사본은 하나로 셈, 적을수록 좋음).',
  'fly': ('은행식', '원장에 적고 확인증까지 떼 줘야 확실하지.', '건당 문서 3개'),
  'robo': ('비트코인식', '거래가 곧 증서! 서류는 한 장이면 돼요.', '건당 문서 1개'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>은행식: 1,000건 × (보내는 은행 원장 1 + 받는 은행 원장 1 + 확인증 1). 비트코인식: 1,000건 × 거래 1. 막대는 3,000을 끝으로 한 선형 눈금이다.</p><p class="lim">비트코인 거래는 노드마다 사본이 저장되지만, 모두 같은 문서라 맞춰 볼 대상이 하나다. 대신 모든 노드가 그 문서를 검증하는 비용이 든다(②칸).</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th></th><th>은행 계좌 이체</th><th>비트코인 이체</th></tr></thead><tbody>
   <tr><td>남는 것 (교안)</td><td>거래내역 및 거래증서</td><td>거래내역만 존재</td></tr>
   <tr><td>잔액</td><td>계좌의 잔액 칸</td><td>쓰지 않은 거래 결과 조각의 합</td></tr>
   <tr><td>송금하면</td><td>두 계좌의 잔액 칸을 고침</td><td>입력 조각을 쓰고 지불·거스름돈 조각을 새로 만듦</td></tr>
   <tr><td>확인하는 쪽</td><td>은행</td><td>망의 모든 노드 (검증 → 추가 → 전파)</td></tr></tbody></table></div>
   <p class="sub">첫 줄은 교안 p.34 그림 설명을 옮김. <sup>[1]</sup></p>''',
 'summary_say': ('doc', 'front', 'doc_e08', '비트코인의 잔액은 칸이 아니라 조각이고, 거래는 장부이자 증서예요. 다음 편은 그 거래에 이름 대신 적히는 것, 주소와 익명성이에요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('robo', 'happy', 'robo_e12'), ('fly', 'cry', 'fly_e21'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 Money-Robo가 두 팔을 들고, 초파리 연구원이 폭포 눈물을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 블록체인은 거래장부이자 거래증서다.<br>· 비트코인의 잔액은 쓰지 않은 거래 결과 조각의 합이고, 송금은 조각을 쓰고 새로 만드는 일이다.<br>· 거래는 노드가 검증·추가·전파하고, 이중 지불은 다음 블록이 정리한다.'),
           ('robo', 'happy', 'robo_e12', '문서 1,000개 대 3,000개! 거래가 곧 증서니까요.'),
           ('fly', 'cry', 'fly_e21', '…서류 수로는 못 이기지. 인정. 대신 그 한 장을 모든 노드가 검증한다는 건 잊지 마.'),
           ('asst', 'e16', 'asst_e16', '다음은 3-05, 모두가 보는 거래에 이름 대신 무엇이 적히는지 봐요.')],
 'kg_hint': 'UTXO, 거스름돈, 전파, 이중 지불…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인과 비트코인」 p.34 (블록체인은 거래장부이자 거래증서, 지불되지 않은 결과의 형태, 지갑 앱을 통한 전파와 검증·추가·재전파, 은행 이체 "거래내역 및 거래증서" 대 비트코인 이체 "거래내역만 존재"). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 5절(네트워크 실행 순서, 유효하고 이미 쓰이지 않은 거래만 받아들임), 9절(여러 입력과 출력, 지불과 거스름돈의 두 출력). 대학 강의 자료실 사본으로 확인, 9절은 HackerNoon 재수록본으로 재확인.'],
 'examples': ['지갑 조각 0.5·0.3·0.15·0.05 BTC와 수수료 0.001 BTC — 예시값', '노드 30개 망의 배치와 연결 (시드 34)', '대결: 은행식 건당 문서 3개 — 교안 그림 설명을 단순화한 셈'],
 'gloss_keys': [('UTXO', True), ('거스름돈', True), ('이중 지불', True), ('노드', False), ('거래 수수료', False)],
 'gloss_anchor': {'UTXO': '#why', '거스름돈': '#lv1', '이중 지불': '#lv2', '노드': '#lv2', '거래 수수료': '#lv1'},
 'quiz': {
  'lv1': [{'q': '0.5와 0.3 BTC 조각으로 0.7 BTC를 보내고 수수료가 0.001 BTC라면 거스름돈 출력은?', 'o': ['0.099 BTC', '0.1 BTC', '0.8 BTC', '없다'], 'a': 0, 'why': '0.8 − 0.7 − 0.001 = 0.099.', 'hint': '입력 = 출력 + 수수료.', 'c': 'lab:term/change-output'},
          {'q': '교안이 말한 비트코인 거래가 존재하는 형태는?', 'o': ['지불되지 않은 결과', '계좌의 잔액 칸', '은행의 확인증', '종이 수표'], 'a': 0, 'why': '교안 p.34. 아직 쓰지 않은 거래 결과(UTXO)예요.', 'hint': '"왜" 카드 둘째.', 'c': 'lab:concept/utxo'}],
  'lv2': [{'q': '거래를 받은 노드가 교안에서 설명한 순서대로 하는 일은?', 'o': ['검증 → 내 장부에 추가 → 다른 컴퓨터에 전파', '전파 → 삭제 → 검증', '은행에 문의 → 승인', '아무것도 하지 않는다'], 'a': 0, 'why': '교안 p.34: 거래를 검증한 다음 장부에 추가하고, 다른 컴퓨터들에게도 뿌려요.', 'hint': 'KPI 넷째.', 'c': 'lab:method/tx-propagation'},
          {'q': '같은 조각을 쓰는 두 거래가 동시에 퍼지면 결국 어떻게 정리되나?', 'o': ['다음 블록에 담긴 거래만 남고 다른 쪽은 거부된다', '둘 다 유효하다', '둘 다 사라진다', '은행이 정한다'], 'a': 0, 'why': '노드는 이미 쓰인 조각을 쓰는 거래를 받아들이지 않아요(백서 5절).', 'hint': '"행동으로 보기" 장면.', 'c': 'lab:concept/double-spending'}]},
 'kgspec': {
  'ladder': ['lab:method/utxo-spend', 'lab:method/tx-propagation'],
  'about': ['lab:concept/utxo', 'lab:term/change-output', 'lab:method/tx-propagation', 'lab:concept/double-spending'],
  'nodes': [
   ('lab:method/utxo-spend', 'Method', '조각 쓰기 (입력을 쓰고 출력을 만듦)', 'spending UTXOs', '#lv1', '입력 조각을 통째로 쓰고 지불·거스름돈 출력을 새로 만드는 송금 방식.', 4, [(WP, '9절')]),
   ('lab:method/tx-propagation', 'Method', '거래 전파 (검증 → 추가 → 전파)', 'transaction propagation', '#lv2', '거래를 받은 노드가 검증하고 장부에 추가한 뒤 이웃에게 전달하는 과정.', 4, [(LEC, '교안 p.34'), (WP, '5절')]),
   ('lab:concept/ledger-as-certificate', 'Concept', '장부이자 증서', 'ledger as certificate', '#why', '블록체인은 교환 내역을 적는 장부이면서 그 자체로 거래증서다.', 4, [(LEC, '교안 p.34')]),
   ('lab:method/bank-transfer', 'Method', '은행 계좌 이체 (내역 + 증서)', 'bank transfer', '#duel', '보내는 은행과 받는 은행의 원장 기록, 그리고 이체 확인증이 따로 생기는 방식.', 3, [(LEC, '교안 p.34')]),
   ('lab:metric/documents-count', 'Metric', '서로 다른 문서 수', 'distinct documents', '#duel', '거래를 처리하며 생기는, 서로 맞춰 봐야 할 서로 다른 문서의 수.', 3),
   ('lab:metric/utxo-count', 'Metric', '지갑의 조각 수', 'UTXO count', '#lv1', '지갑에 남은 쓰지 않은 거래 결과의 개수.', 3),
   ('lab:metric/propagation-hops', 'Metric', '전파 홉 수', 'propagation hops', '#lv2', '거래가 망의 모든 노드에 닿기까지 걸린 홉 수.', 3),
   ('lab:limitation/split-view', 'Limitation', '이중 지불 때 갈라진 망', 'split view', '#lv2', '같은 조각을 쓰는 두 거래가 퍼지면 노드마다 먼저 본 거래가 다르다.', 3),
   ('lab:limitation/everyone-sees', 'Limitation', '모든 노드가 모든 거래를 봄', 'every node sees every transaction', '#lv2', '검증하려면 거래가 모두에게 보여야 한다. 개인정보 문제로 이어진다.', 3),
   ('lab:analogy/notes-in-wallet', 'Analogy', '액면 증서 묶음 ↔ UTXO', 'notes in a wallet ~ UTXO', '#lv1', '낸 증서는 찢어지고 지불·거스름 증서가 새로 생긴다.', 3),
   ('lab:question/core', 'Question', '지갑 속 비트코인은 어떤 모양일까?', 'What does bitcoin in a wallet look like?', '#top', None, 3),
   ('lab:question/duel', 'Question', '거래 1,000건에 생기는 문서는 몇 개인가?', 'Documents for 1,000 transfers', '#duel', None, 3),
  ],
  'edges': [
   ('lab:concept/utxo', 'lab:partOf', 'lab:method/utxo-spend', '#lv1'),
   ('lab:term/change-output', 'lab:partOf', 'lab:method/utxo-spend', '#lv1'),
   ('lab:concept/transaction-fee', 'lab:partOf', 'lab:method/utxo-spend', '#lv1'),
   ('lab:method/utxo-spend', 'lab:evaluatedBy', 'lab:metric/utxo-count', '#lv1'),
   ('lab:concept/ledger-as-certificate', 'lab:broader', 'lab:concept/utxo', '#why'),
   ('lab:concept/ledger-as-certificate', 'lab:contrastsWith', 'lab:method/bank-transfer', '#duel'),
   ('lab:method/bank-transfer', 'lab:evaluatedBy', 'lab:metric/documents-count', '#duel'),
   ('lab:method/utxo-spend', 'lab:hasLimitation', 'lab:concept/double-spending', '#lv1'),
   ('lab:concept/double-spending', 'lab:addressedBy', 'lab:method/tx-propagation', '#lv2'),
   ('lab:method/utxo-spend', 'lab:prerequisiteOf', 'lab:method/tx-propagation', '#lv2'),
   ('lab:term/node', 'lab:partOf', 'lab:method/tx-propagation', '#lv2'),
   ('lab:method/tx-propagation', 'lab:evaluatedBy', 'lab:metric/propagation-hops', '#lv2'),
   ('lab:method/tx-propagation', 'lab:hasLimitation', 'lab:limitation/split-view', '#lv2'),
   ('lab:method/tx-propagation', 'lab:hasLimitation', 'lab:limitation/everyone-sees', '#lv2'),
   ('lab:metric/documents-count', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/everyone-sees', 'lab:raises', 'lab:question/core', '#lv2'),
   ('lab:analogy/notes-in-wallet', 'lab:analogyOf', 'lab:concept/utxo', '#lv1'),
  ],
  'claims': [
   ('lab:claim/ledger-and-certificate', '블록체인은 그 자체가 거래장부인 동시에 거래증서이며, 비트코인에서는 각 거래가 지불되지 않은 결과의 형태로 존재한다', '#why', ['lab:concept/ledger-as-certificate', 'lab:concept/utxo'], [(LEC, '교안 p.34')], 'F01'),
   ('lab:claim/broadcast-verify', '거래는 지갑 앱을 통해 네트워크에 뿌려지고, 컴퓨터들은 검증한 다음 자신의 장부에 추가하고 다른 컴퓨터에도 뿌린다', '#why', ['lab:method/tx-propagation'], [(LEC, '교안 p.34')], 'F02'),
   ('lab:claim/bank-vs-btc', '은행 계좌 이체에는 거래내역과 거래증서가 있고, 비트코인 이체에는 거래내역만 존재한다', '#duel', ['lab:method/bank-transfer', 'lab:concept/ledger-as-certificate'], [(LEC, '교안 p.34 그림 설명')], 'F03'),
   ('lab:claim/inputs-outputs', '값을 나누고 합칠 수 있도록 거래는 여러 입력과 출력을 가지며, 출력은 보통 지불과 거스름돈 둘 이하다', '#lv1', ['lab:method/utxo-spend', 'lab:term/change-output'], [(WP, '9절')], 'F04'),
   ('lab:claim/network-steps', '노드는 새 거래를 모아 블록을 만들고 작업증명을 하며, 블록의 거래가 모두 유효하고 이미 쓰이지 않았을 때만 블록을 받아들인다', '#lv2', ['lab:method/tx-propagation', 'lab:concept/double-spending'], [(WP, '5절')], 'F05'),
  ],
  'sims': [('lab:simulation/wallet-spend', '지갑 조각 송금 실험', '#lv1', ['lab:method/utxo-spend']),
           ('lab:simulation/propagation-30', '노드 30개 전파 실험', '#lv2', ['lab:method/tx-propagation']),
           ('lab:simulation/duel-documents', '문서 수 대결', '#duel', ['lab:metric/documents-count'])],
 },
}

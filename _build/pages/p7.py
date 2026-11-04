LEC, YTN, NWS = "lecture2024blockchain", "ytn2020baksa", "newsis2020baksa"
PAGE = {
 'num': '3-07', 'slug': 'misuse-and-tracing', 'key': '3_07', 'anchor': 'D',
 'tab_title': '범죄 악용과 추적', 'meta_title': '범죄 악용과 추적 — 익명성의 그늘과 공개 장부',
 'description': '암호화폐가 범죄에 악용되는 이유를 교안을 따라 정리하고, 공개 장부 위에서 자금 흐름을 홉 단위로 따라가 신원이 확인되는 지점에 닿는 과정을 모형으로 실험하는 해설 페이지. 블록체인 편의 마지막 편',
 'dc_source': '강의 교안 「블록체인과 비트코인」 p.42–44; YTN 2020.03.27; 뉴시스 2020.04.07',
 'h1': '범죄 악용과 추적<br>— 익명성의 그늘과 공개 장부', 'hero_alt': '책상과 서류가 놓인 사무실을 픽셀로 그린 배경',
 'question': '이름 없는 주소와 국경 없는 이동은 왜 범죄자에게 매력적일까? 그런데 모든 거래가 공개된 장부라면, 그 흐름은 정말 감춰질까?',
 'lead': '3-05에서 비트코인은 거래를 공개하고 이름을 뺐습니다. 교안은 같은 성질의 그늘을 짚습니다. 실물이 없어 인터넷으로 바로 이체되고 익명성까지 보장되어 범죄에 악용되는 사례가 늘었다는 것이죠. 동시에 경찰이 비트코인을 압수하고 추적하는 대응에 나섰다고도 씁니다. 왜 악용되는지 정리하고, 공개 장부가 거꾸로 추적의 단서가 되는 과정을 모형으로 따라가 봅니다. 블록체인 편의 마지막 편입니다.',
 'kpis': [('익명성 + 즉시 이체', '범죄에 악용되는 이유 (교안)', 'r', [1]), ('30개가량', '박사방 수사에서 찾은 가상화폐 계좌 (2020.3)', 'm', [2]), ('2천여 건', '구매대행 업체에서 확보한 거래기록', 'a', [2]), ('약 10명', '거래소·구매대행 기록으로 특정해 입건한 유료 회원 (2020.4)', 'g', [3])],
 'hero': [('doc', 'think', 'doc_e09', '익명성은 이름을 숨기지만 거래를 숨기지는 않아요. 그 차이가 수사의 출발점이에요.'),
          ('asst', 'smile', 'asst_e13', '몸값으로 받은 돈이 스무 갈래로 흩어지는 모형을 만들었어요. 각 갈래가 신원 확인 지점에 닿는지 제가 셀게요.'),
          ('fly', 'point', 'fly_e08', '주소에 이름이 없다고 끝이 아니야. 돈은 결국 어딘가에서 현금이나 물건으로 바뀌잖아.'),
          ('robo', 'coin', 'robo_e16', '이름 없는 주소를 몇 번 거치면 그걸로 끝! 추적은 사실상 불가능해요.')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '추적된 흐름을 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 장부를 끝까지 따라간다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 이름 없으면 못 잡는다.')],
 'why_title': '왜 악용과 추적을 보나',
 'why_lead': '기술은 쓰는 사람에 따라 다르게 쓰여요. 3장의 마지막에서는 익명성(3-05)과 즉시 이동(3-04)이 어떻게 악용되는지, 그리고 공개 장부가 어떤 단서를 남기는지 봅니다.',
 'why': [('악용 사례', '비트코인은 실물이 없어 인터넷으로 손쉽게 바로 이체할 수 있고 익명성까지 보장되어, 불법 사이트와 마약 거래 등 범죄에 악용되는 사례가 늘고 있다. <sup>[1]</sup>'),
         ('범죄자에게 매력적인 이유', '거래의 익명성과 추적의 어려움, 국경을 초월한 즉각적인 자금 이동, 기존 금융 시스템의 규제를 우회해 불법 자금을 세탁·은닉하기 쉽다는 점을 교안은 꼽는다. 랜섬웨어 공격의 몸값 요구나 N번방 사건 같은 불법 콘텐츠 거래의 결제 수단으로 선호된다고도 쓴다. <sup>[1]</sup>'),
         ('대응', '경찰은 음란 사이트 운영자로부터 비트코인을 압수하고, 마약 거래에 사용된 비트코인을 추적하는 등 대응에 나섰다. <sup>[1]</sup> 2020년 박사방 사건에서는 주범과 공범이 쓴 가상화폐 계좌 30개가량을 찾고 구매대행 업체의 거래기록을 확보해 유료 회원을 추적했다. <sup>[2]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 은행은 장부를 감추고 신원을 알아요. 비트코인은 장부를 드러내고 신원을 감춰요. 수사는 드러난 장부에서 신원이 드러나는 지점을 찾는 일이에요.'),
 'big_lead': '3-05의 주소 묶기를 수사의 눈으로 다시 보는 칸이자, 블록체인 편 21편을 닫는 칸입니다.',
 'ladder': [('①', '공개 장부 위의 추적', '자금 흐름을 홉 단위로 따라가 신원 확인 지점에 닿는다', '확인 지점에 닿지 않는 흐름은 남는다'),
            ('②', '국경과 규제의 우회', '은행 송금의 확인 지점 vs 직접 이체', '그래서 추적은 장부의 입출구에 기댄다 (모형의 해석)')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '공개 장부 추적', 'title': '이름은 없어도 흐름은 남는다 — 홉 단위 추적',
   'tags': [('방식: 몸값 주소에서 출발해 거래를 하나씩 따라감', 'g'), ('현장: 수사관의 장부 대조', '')],
   'left': '<p>도둑이 훔친 지폐를 여러 사람 손을 거쳐 쓰게 했다. 지폐에 이름은 없다. 그런데 모든 지폐의 일련번호와 손이 바뀐 기록이 게시판에 붙어 있다면? 수사관은 번호를 따라가다 지폐가 신분증을 보여 줘야 하는 창구에 닿는 곳을 찾는다.</p>',
   'right': '<p>비트코인의 모든 거래는 공개 장부에 남는다(3-04). 주소에는 이름이 없지만(3-05), 신원이 확인되는 지점이 있다면 흐름이 사람과 연결될 수 있다. 박사방 사건에서 구매대행 업체 관계자는 송금 신청자의 기록이 남는다고 했고, 경찰은 범행과 관련된 거래로 확인되면 송금자, 곧 유료 회원을 찾을 수 있다고 봤다. <sup>[2]</sup> 실제로 경찰은 거래소 3곳과 구매대행 업체 2곳에 협조를 요청해 기록을 받았고, 유료 회원 약 10명을 특정해 입건했다. <sup>[3]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 몸값 주소에서 흩어진 20갈래</h3>
    <div class="cwrap"><canvas id="c1" aria-label="몸값 주소에서 출발한 20갈래의 자금 흐름을 홉별 열로 그리고, 정해진 홉 안에서 신원 확인 지점에 닿은 갈래를 강조한 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">따라갈 최대 홉 수</span><input type="range" id="r1h" min="0" max="8" step="1" value="6" aria-label="추적할 최대 홉 수"><span class="val" id="v1h">6</span>홉</div>
      <div class="group"><span class="glabel">갈래가 확인 지점에서 끝날 비율 (모형 가정)</span><input type="range" id="r1p" min="30" max="100" step="10" value="70" aria-label="확인 지점 비율"><span class="val" id="v1p">70</span>%</div></div>
    <h3>행동으로 보기 — 장부를 한 칸씩 따라가는 돋보기</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="돋보기가 거래를 한 홉씩 따라가다 신원 확인 지점에 닿으면 표시가 켜지는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 숨은 것은 이름, 남은 것은 길</h4>
    <ol><li>공개 장부에서는 주소에서 주소로 넘어간 모든 홉이 보인다. 이름이 없어도 길은 끊기지 않는다.</li>
      <li>흐름이 송금자 기록을 남기는 지점(거래소, 구매대행 업체 — 이 모형의 "확인 지점")에 닿으면 그 갈래는 사람과 연결된다. 박사방 수사가 바로 이 길을 따랐다. <sup>[2][3]</sup> 따라갈 홉 수를 늘릴수록 더 많은 갈래가 연결된다.</li>
      <li>확인 지점에 닿지 않고 끝나는 갈래는 남는다. 같은 보도는 거래소·대행 업체와 달리 개인 간 직접 거래는 익명성이 보장된다고 짚었고, 경찰은 개인 간 거래도 추적할 계획이라고 밝혔다. <sup>[2]</sup> 교안이 "추적의 어려움"을 범죄자에게 매력적인 이유로 꼽은 것도 이 때문이다. <sup>[1]</sup></li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 확인 지점이 어디에 있느냐가 관건이다. 국경을 넘는 직접 이체는 그런 지점을 얼마나 지나갈까? → 국경과 규제의 우회.</p>''',
   'extra': '<details class="math"><summary>모형으로 보기</summary><p>갈래 20개, 갈래마다 길이 1~7홉(시드 37), 끝 지점이 확인 지점일 확률 p(기본 70%). 최대 h홉까지 따라갈 때 "길이 ≤ h이고 끝이 확인 지점"인 갈래를 연결된 것으로 센다.</p><p class="lim">갈래 수, 길이, 확인 지점 비율은 모두 가정이다. 실제 수사는 주소 묶기(3-05), 거래 패턴, 법적 절차를 통한 정보 요청 등을 함께 쓴다. 이 페이지는 추적을 피하는 방법을 다루지 않는다.</p></details><div class="bridge field"><h4>실제 사례 — 박사방 사건의 가상화폐 추적 (2020)</h4><ul>       <li>경찰은 주범 조주빈과 공범들이 쓴 가상화폐 계좌를 30개 가까이 찾았다. 텔레그램 방에 올린 계좌 3개 중 2개는 가짜였고, 실제로는 한 계좌로 돈을 보내라고 요구한 것으로 파악됐다. <sup>[2]</sup></li>       <li>경찰은 구매대행 업체 베스트코인의 거래기록 2천여 건을 확보했다. 범행과 관련된 거래로 확인되면 송금자, 곧 유료 회원을 찾을 수 있다. 반면 개인 간 직접 거래는 익명성이 보장된다는 한계도 함께 보도됐다. <sup>[2]</sup></li>       <li>주범은 주로 모네로를 썼고 다른 코인도 일부 쓰였다. 경찰은 빗썸·업비트·코인원과 구매대행 업체 베스트코인·비트프록시에 협조를 요청해 기록을 받았고, 유료 회원 약 10명을 특정해 입건했다. 4월 6일에는 거래소·구매대행 업체 약 20곳으로 압수수색을 넓혔다. <sup>[3]</sup></li>       <li>주범의 범죄 수익으로 알려졌던 약 32억 원은 주범이 쓰지 않은 허위 계좌의 거래로, 이 사건과 관련이 없다고 경찰은 설명했다. <sup>[2][3]</sup></li></ul>     <p class="sub">①의 모형에서 "확인 지점"은 이 사건의 거래소·구매대행 업체에 해당한다. 모형의 갈래 수와 비율은 가정이며 사건의 실제 수치가 아니다.</p></div>',
   'say': ('fly', 'type', 'fly_e09', '여섯 홉까지 따라가니 스무 갈래 중 여덟 갈래가 확인 지점에 닿았어. 박사방 수사도 거래소·대행 업체 기록에서 회원을 찾아냈지.')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '국경과 규제', 'title': '확인 지점을 건너뛰는 이동 — 국경과 규제의 우회',
   'tags': [('방식: 송금 경로에서 신원 확인 지점과 걸리는 시간을 셈', 'g'), ('현장: 해외 송금 창구 대 지갑 간 직접 이체', '')],
   'left': '<p>해외로 돈을 보내려면 은행 창구에서 신분증을 내고, 송금 심사를 거치고, 받는 나라 은행에서 다시 확인을 받는다. 지갑에서 지갑으로 바로 보내면 그 창구들을 지나지 않는다. 대신 그 돈을 다시 현금으로 바꾸는 창구에서는 확인을 받아야 할 수 있다.</p>',
   'right': '<p>교안은 암호화폐가 국경을 초월한 즉각적인 자금 이동을 가능하게 해 국제 범죄 네트워크에 유용하게 쓰이고, 기존 금융 시스템의 규제를 우회할 수 있어 불법 자금의 세탁과 은닉에 쓰이기 쉽다고 쓴다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 두 송금 경로의 확인 지점</h3>
    <div class="cwrap"><canvas id="c2" aria-label="은행 해외 송금과 지갑 간 직접 이체 경로를 나란히 그리고, 신원 확인 지점과 걸리는 시간을 표시한 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">직접 이체 뒤 현금화 창구를 거치나</span><button class="bt" data-exit="yes" aria-pressed="true">거친다</button><button class="bt" data-exit="no" aria-pressed="false">거치지 않는다</button></div>
      <div class="group"><span class="glabel">거쳐 가는 지갑 수</span><input type="range" id="r2n" min="0" max="6" step="1" value="3" aria-label="거쳐 가는 지갑 수"><span class="val" id="v2n">3</span>개</div></div>
    <h3>행동으로 보기 — 창구를 지나는 돈</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="은행 경로의 돈은 창구마다 멈춰 확인을 받고, 직접 이체 경로의 돈은 지갑 사이를 바로 건너가는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 확인 지점의 수와 위치</h4>
    <ol><li>은행 해외 송금 경로에는 신원을 확인하는 지점이 여러 번 있다(이 모형에서는 3곳). 시간은 걸리지만 돈과 사람이 계속 연결된다.</li>
      <li>지갑 간 직접 이체는 거쳐 가는 지갑이 늘어도 확인 지점이 없다. 교안이 말한 "국경을 초월한 즉각적인 자금 이동"과 "규제 우회"다. <sup>[1]</sup></li>
      <li>그 돈이 현금화 창구를 거치면 거기서 한 번 연결될 수 있고, 공개 장부를 거슬러 올라가 앞선 이동까지 이어 볼 수 있다(①칸). 거치지 않으면 연결 지점이 없다. 박사방 수사에서 경찰이 거래소·구매대행 업체 약 20곳으로 압수수색을 넓힌 것도 이런 지점을 찾는 일이었다. <sup>[3]</sup></li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 확인 지점의 수와 시간은 이 페이지의 모형 가정이다. 실제 송금 절차와 규제는 나라와 사업자마다 다르다.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면 — 블록체인 편을 닫으며</h4><p>1장은 "은행 없이 서로 모르는 사람끼리 장부를 믿을 수 있을까"에서 시작했다. 2장은 그 장부를 해시와 채굴로 지켰고, 3장은 그 장부 위에서 돈이 어떻게 만들어지고, 거래되고, 숨고, 드러나는지 봤다. 같은 성질이 장점과 그늘을 함께 만든다. 공개 장부는 위조를 막고, 동시에 흐름을 드러낸다. 익명성은 개인정보를 지키고, 동시에 악용된다. 교안도 두 면을 함께 적는다. <sup>[1]</sup></p></div>',
   'say': ('asst', 'e10', 'asst_e10', '은행 경로는 확인 지점 3곳, 직접 이체는 0곳이에요. 현금화 창구를 거치면 1곳이 생기고, 거기서 장부를 거슬러 올라갈 수 있어요.')},
 ],
 'duel': {'title': '몸값 20갈래, 신원까지 닿은 흐름',
  'intro': '몸값 주소에서 흩어진 자금 20갈래를 두 수사관이 맡는다. 주판봇은 "이름 없는 주소는 추적 불가"라며 몸값 주소에서 바로 확인 지점으로 간 갈래만 센다. 초파리는 공개 장부를 최대 6홉까지 따라간다. 판정 기준은 <b>신원 확인 지점까지 연결된 갈래 수</b>(많을수록 좋음). 위 실험과 같은 모형, 시드 37, 확인 지점 비율 70%.',
  'fly': ('6홉까지 추적', '이름이 없어도 길은 공개돼 있어. 끝까지 따라가 봐야지.', '최대 6홉'),
  'robo': ('바로 연결된 것만', '주소를 몇 번 거치면 끝! 이름 없는 주소는 못 따라가요.', '1홉만'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>①과 같은 갈래 20개(시드 37, 확인 지점 비율 70%). 초파리: 길이 ≤ 6이고 끝이 확인 지점인 갈래 수. 주판봇: 길이 1이고 끝이 확인 지점인 갈래 수. 막대는 20을 끝으로 한 선형 눈금이다.</p><p class="lim">모형 가정이며 실제 수사 성과를 나타내지 않는다. 이 페이지는 추적을 피하는 방법을 다루지 않는다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>교안이 꼽은 악용 이유</th><th>공개 장부가 남기는 것</th></tr></thead><tbody>
   <tr><td>거래의 익명성 (주소에 이름 없음)</td><td>주소 사이의 모든 홉, 같은 주인으로 묶이는 주소들 (3-05)</td></tr>
   <tr><td>국경을 초월한 즉각적인 이동</td><td>이동 기록 자체는 장부에 그대로 남음</td></tr>
   <tr><td>기존 금융 규제의 우회</td><td>신원이 확인되는 지점에 닿으면 거슬러 올라가 연결</td></tr>
   <tr><td>랜섬웨어 몸값, 불법 콘텐츠 거래 (N번방 사건)</td><td>압수와 추적. 박사방 사건: 가상화폐 계좌 30개가량 확인, 거래소·구매대행 기록으로 유료 회원 약 10명 입건 <sup>[2][3]</sup></td></tr></tbody></table></div>
   <h3>블록체인 편 21편 한 줄씩 <span class="stampnote">시리즈 정리</span></h3>
   <div class="tw"><table class="tb"><thead><tr><th>장</th><th>물음</th><th>답의 요지</th><th>대결 (초파리 : 주판봇 : 무승부)</th></tr></thead><tbody>
   <tr><td>1장 장부의 진화</td><td>은행 없이 장부를 믿을 수 있을까</td><td>기억 → 장부 → 계약 → 증인 → 은행 → 모두가 나눠 든 장부</td><td>3 : 3 : 1</td></tr>
   <tr><td>2장 블록체인 기술</td><td>나눠 든 장부를 어떻게 지키나</td><td>블록 → 해시 → 사슬 → 이력 → 채굴 → 난이도와 확정</td><td>4 : 3 : 0</td></tr>
   <tr><td>3장 비트코인</td><td>그 장부 위의 돈은 어떤 모습인가</td><td>합의 방식 → 채굴장 → 반감기 → 거래 → 익명성 → 화폐성 → 악용과 추적</td><td>3 : 3 : 1</td></tr>
   <tr><td><b>합계</b></td><td></td><td></td><td><b>10 : 9 : 2</b></td></tr></tbody></table></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '익명성은 이름을 숨기고, 공개 장부는 길을 남겨요. 그리고 이것으로 블록체인 편 스물한 편이 끝나요. 같은 성질이 장점과 그늘을 함께 만든다는 것, 그게 마지막 한 줄이에요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('fly', 'arms', 'fly_e16'), ('robo', 'sigh', 'robo_e20'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 초파리 연구원이 팔짱을 끼고, 주판봇이 식은땀을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 익명성, 즉시 이체, 국경 초월, 규제 우회가 암호화폐를 범죄에 악용되게 한다.<br>· 그러나 주소에 이름이 없을 뿐, 모든 거래는 공개 장부에 남는다.<br>· 흐름이 신원 확인 지점에 닿으면 거슬러 올라가 연결할 수 있다.'),
           ('fly', 'arms', 'fly_e16', '이름이 없다고 길까지 사라지는 건 아니야. 끝까지 따라가면 닿는 데가 있어.'),
           ('robo', 'sigh', 'robo_e20', '바로 연결된 몇 갈래만 셌더니… 장부가 공개돼 있다는 걸 잊었네요.'),
           ('asst', 'e16', 'asst_e16', '블록체인 편 대결 총 집계는 초파리 10승(실격승 2번 포함), 주판봇 9승, 무승부 2번이에요. 스물한 편, 함께 와 주셔서 고마워요.')],
 'kg_hint': '범죄 악용, 추적, 실명 확인, 국경…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인과 비트코인」 p.42 (교안이 인용한 보도: 「비트코인 이용 범죄 성행…익명성 보장 악용」 연합뉴스TV 2017.05.27), p.43 (실물 없는 즉시 이체와 익명성, 불법 사이트·마약 거래 악용, 경찰의 압수·추적 대응), p.44 (익명성과 추적의 어려움, 국경 초월 즉시 이동, 규제 우회와 세탁·은닉, 랜섬웨어 몸값과 N번방 사건 같은 불법 콘텐츠 거래). PDF 2024-10-18 생성.',
                 'YTN (2020.03.27). 「\'박사방 일당 계좌\' 30개가량 확인...유료회원 거래기록 선별 중」. 가상화폐 계좌 30개가량, 게시 계좌 3개 중 2개 가짜, 베스트코인 거래기록 2천여 건, 송금자 특정 가능성, 개인 간 거래의 익명성, 32억 원 허위 계좌. 2026-10-29 확인.',
                 '천민아 (2020.04.07). 「\'박사방 유료회원\' 추적 청신호…가상화폐에 흔적 남겼다」. 뉴시스. 모네로 사용, 거래소 3곳·구매대행 2곳 협조 요청, 유료 회원 약 10명 입건, 거래소·대행 업체 약 20곳 압수수색. 2026-10-29 확인.'],
 'examples': ['몸값 20갈래의 길이(1~7홉, 시드 37)와 확인 지점 비율 70% — 모형 가정 (박사방 사건의 실제 수치 아님)', '송금 경로의 확인 지점 수와 시간 — 모형 가정', '대결: 6홉 추적 대 1홉, 같은 갈래'],
 'gloss_keys': [('추적', True), ('실명 확인', True), ('박사방 사건', True), ('익명성', True), ('주소', False), ('전자지갑', False)],
 'gloss_anchor': {'박사방 사건': '#lv1', '추적': '#lv1', '실명 확인': '#lv1', '익명성': '#why', '주소': '#lv1', '전자지갑': '#lv2'},
 'quiz': {
  'lv1': [{'q': '교안이 꼽은, 비트코인이 범죄에 악용되는 이유가 아닌 것은?', 'o': ['거래 내역이 장부에서 지워지기 때문에', '실물이 없어 인터넷으로 바로 이체할 수 있어서', '익명성이 보장되어서', '국경을 초월해 즉시 이동할 수 있어서'], 'a': 0, 'why': '거래 내역은 공개 장부에 남아요. 나머지는 교안 p.43–44가 꼽은 이유예요.', 'hint': '3-04를 떠올려 보세요.', 'c': 'lab:method/transaction-tracing'},
          {'q': '박사방 사건에서 경찰이 유료 회원을 특정한 주된 단서는?', 'o': ['거래소·구매대행 업체가 남긴 송금 기록', '주소에 적힌 실명', '비트코인 네트워크 운영자의 명단', '채굴자의 증언'], 'a': 0, 'why': '경찰은 거래소 3곳·구매대행 2곳에 협조를 요청해 기록을 받고 약 10명을 입건했어요(뉴시스 2020.04.07).', 'hint': '「실제 사례」 상자.', 'c': 'lab:concept/case-baksabang'}],
  'lv2': [{'q': '교안에 따르면 암호화폐가 불법 자금 세탁·은닉에 쓰이기 쉬운 이유는?', 'o': ['기존 금융 시스템의 규제를 우회할 수 있어서', '거래 수수료가 없어서', '중앙은행이 보증해서', '거래가 느려서'], 'a': 0, 'why': '교안 p.44.', 'hint': '②의 "방식" 설명.', 'c': 'lab:limitation/regulation-bypass'},
          {'q': '교안이 소개한 경찰의 대응은?', 'o': ['비트코인 압수와 마약 거래에 쓰인 비트코인 추적', '비트코인 네트워크 정지', '모든 지갑 삭제', '채굴 금지'], 'a': 0, 'why': '교안 p.43.', 'hint': '"왜" 카드 셋째.', 'c': 'lab:method/transaction-tracing'}]},
 'kgspec': {
  'ladder': ['lab:method/transaction-tracing', 'lab:method/route-checkpoints'],
  'about': ['lab:method/transaction-tracing', 'lab:concept/kyc-checkpoint', 'lab:concept/crypto-misuse', 'lab:limitation/regulation-bypass'],
  'nodes': [
   ('lab:method/route-checkpoints', 'Method', '송금 경로의 확인 지점 비교', 'comparing checkpoints on transfer routes', '#lv2', '은행 해외 송금과 지갑 간 직접 이체 경로에서 신원 확인 지점의 수와 위치를 비교하는 방법.', 3),
   ('lab:concept/crypto-misuse', 'Concept', '암호화폐의 범죄 악용', 'criminal misuse of crypto', '#why', '익명성과 즉시 이체를 이용해 불법 거래·몸값·자금 세탁에 쓰는 일.', 4, [(LEC, '교안 p.43–44')]),
   ('lab:limitation/regulation-bypass', 'Limitation', '기존 금융 규제의 우회', 'bypassing financial regulation', '#lv2', '직접 이체는 기존 금융 시스템의 확인 지점을 지나지 않아 불법 자금 세탁·은닉에 쓰이기 쉽다.', 4, [(LEC, '교안 p.44')]),
   ('lab:concept/cross-border', 'Concept', '국경을 초월한 즉각적 이동', 'instant cross-border transfer', '#lv2', '국경과 관계없이 곧바로 자금을 옮길 수 있는 성질.', 3, [(LEC, '교안 p.44')]),
   ('lab:limitation/untraced-branches', 'Limitation', '확인 지점에 닿지 않는 흐름', 'untraced branches', '#lv1', '신원 확인 지점에 닿지 않고 끝나는 흐름은 사람과 연결되지 않는다.', 3),
   ('lab:metric/traced-flows', 'Metric', '신원까지 연결된 갈래 수', 'flows linked to identity', '#duel', '자금 흐름 갈래 가운데 신원 확인 지점에 닿아 사람과 연결된 수.', 4),
   ('lab:metric/checkpoint-count', 'Metric', '경로의 확인 지점 수', 'checkpoints on route', '#lv2', '송금 경로에서 신원을 확인하는 지점의 수.', 3),
   ('lab:analogy/serial-numbers', 'Analogy', '일련번호가 공개된 지폐 ↔ 공개 장부 추적', 'public serial numbers ~ tracing', '#lv1', '지폐에 이름은 없지만 번호와 손바뀜 기록이 공개되어 있다면 신분증 창구에 닿는 곳을 찾을 수 있다.', 3),
   ('lab:limitation/p2p-anonymity', 'Limitation', '개인 간 직접 거래의 익명성', 'peer-to-peer anonymity', '#lv1', '거래소·대행 업체와 달리 개인 간 직접 거래에는 송금자 기록이 남지 않는다.', 3, [(YTN, 'YTN 2020.03.27')]),
   ('lab:question/core', 'Question', '이름 없는 주소의 흐름은 정말 감춰질까?', 'Are flows from nameless addresses hidden?', '#top', None, 3),
   ('lab:question/duel', 'Question', '20갈래 중 몇 갈래가 신원까지 닿을까?', 'How many flows reach identity?', '#duel', None, 3),
  ],
  'edges': [
   ('lab:concept/pseudonymity', 'lab:prerequisiteOf', 'lab:concept/crypto-misuse', '#why'),
   ('lab:concept/cross-border', 'lab:partOf', 'lab:concept/crypto-misuse', '#lv2'),
   ('lab:limitation/regulation-bypass', 'lab:partOf', 'lab:concept/crypto-misuse', '#lv2'),
   ('lab:concept/crypto-misuse', 'lab:addressedBy', 'lab:method/transaction-tracing', '#lv1', 'mid'),
   ('lab:term/address', 'lab:partOf', 'lab:method/transaction-tracing', '#lv1'),
   ('lab:concept/kyc-checkpoint', 'lab:partOf', 'lab:method/transaction-tracing', '#lv1'),
   ('lab:method/transaction-tracing', 'lab:evaluatedBy', 'lab:metric/traced-flows', '#lv1'),
   ('lab:method/transaction-tracing', 'lab:hasLimitation', 'lab:limitation/untraced-branches', '#lv1'),
   ('lab:limitation/untraced-branches', 'lab:prerequisiteOf', 'lab:method/route-checkpoints', '#lv2'),
   ('lab:method/route-checkpoints', 'lab:evaluatedBy', 'lab:metric/checkpoint-count', '#lv2'),
   ('lab:concept/wallet', 'lab:partOf', 'lab:method/route-checkpoints', '#lv2'),
   ('lab:limitation/regulation-bypass', 'lab:raises', 'lab:question/core', '#lv2'),
   ('lab:metric/traced-flows', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:analogy/serial-numbers', 'lab:analogyOf', 'lab:method/transaction-tracing', '#lv1'),
   ('lab:concept/case-baksabang', 'lab:partOf', 'lab:concept/crypto-misuse', '#why'),
   ('lab:concept/case-baksabang', 'lab:demonstratedBy', 'lab:method/transaction-tracing', '#lv1'),
   ('lab:limitation/untraced-branches', 'lab:broader', 'lab:limitation/p2p-anonymity', '#lv1'),
  ],
  'claims': [
   ('lab:claim/misuse-cases', '비트코인은 실물이 없어 인터넷으로 손쉽게 바로 이체할 수 있고 익명성까지 보장되어 불법 사이트와 마약 거래 등 범죄에 악용되는 사례가 늘고 있다', '#why', ['lab:concept/crypto-misuse'], [(LEC, '교안 p.43')], 'F01'),
   ('lab:claim/police-response', '경찰은 음란 사이트 운영자로부터 비트코인을 압수하고 마약 거래에 사용된 비트코인을 추적하는 등 대응에 나섰다', '#why', ['lab:method/transaction-tracing'], [(LEC, '교안 p.43')], 'F02'),
   ('lab:claim/attractive', '암호화폐는 거래의 익명성과 추적의 어려움으로 범죄자들에게 매력적인 수단이다', '#lv1', ['lab:concept/crypto-misuse', 'lab:limitation/untraced-branches'], [(LEC, '교안 p.44')], 'F03'),
   ('lab:claim/cross-border', '국경을 초월한 즉각적인 자금 이동이 가능해 국제적인 범죄 네트워크에 유용하게 활용된다', '#lv2', ['lab:concept/cross-border'], [(LEC, '교안 p.44')], 'F04'),
   ('lab:claim/bypass', '기존 금융 시스템의 규제를 우회할 수 있어 불법 자금의 세탁과 은닉에 사용되기 쉽고, 랜섬웨어 몸값이나 N번방 사건 같은 불법 콘텐츠 거래의 결제 수단으로 선호된다', '#lv2', ['lab:limitation/regulation-bypass'], [(LEC, '교안 p.44')], 'F05'),
   ('lab:claim/baksa-accounts', '박사방 사건에서 경찰은 주범과 공범들이 쓴 가상화폐 계좌 30개가량을 찾았고, 구매대행 업체의 거래기록 2천여 건을 확보했으며, 범행 관련 거래로 확인되면 송금자를 찾을 수 있다고 보도됐다', '#lv1', ['lab:concept/case-baksabang', 'lab:concept/kyc-checkpoint'], [(YTN, 'YTN 2020.03.27')], 'F06'),
   ('lab:claim/p2p-anon', '거래소·대행 업체와 달리 개인 간 직접 거래는 익명성이 보장되며, 경찰은 개인 간 거래도 추적할 계획이라고 밝혔다', '#lv1', ['lab:limitation/p2p-anonymity'], [(YTN, 'YTN 2020.03.27')], 'F07'),
   ('lab:claim/baksa-members', '경찰은 거래소 3곳과 구매대행 업체 2곳에 협조를 요청해 기록을 받고 유료 회원 약 10명을 특정해 입건했으며, 거래소·대행 업체 약 20곳으로 압수수색을 넓혔다', '#lv1', ['lab:concept/case-baksabang', 'lab:metric/traced-flows'], [(NWS, '뉴시스 2020.04.07')], 'F08'),
  ],
  'sims': [('lab:simulation/ransom-20', '몸값 20갈래 추적 모형', '#lv1', ['lab:method/transaction-tracing']),
           ('lab:simulation/route-compare', '송금 경로 확인 지점 비교', '#lv2', ['lab:method/route-checkpoints']),
           ('lab:simulation/duel-tracing', '추적 대결', '#duel', ['lab:metric/traced-flows'])],
 },
}

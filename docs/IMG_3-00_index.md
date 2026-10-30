# 블록체인 3장 공용 이미지 명세서 (`IMG_3-00_index.md`)

| 항목 | 내용 |
|---|---|
| 챕터 | 블록체인 편 3장 「비트코인」, 페이지 7개 + 목차 |
| 시즌 | 기본 |
| 공용 표정 | 캐릭터 팩 (커밋 ea5da3f), `assets/sprites.js`에 96px + 192px 묶음 · 그림 없음 역할 키: doc_scale, asst_ledger, asst_board |

## 1. 목차·표지 그림
| 키 | 판 | 내용 | 제작 | 우선 |
|---|---|---|---|---|
| bg_ch3_index | F | 장부 위의 돈을 한 장면에: 왼쪽은 단순, 오른쪽으로 갈수록 채굴기와 추첨함 → 채굴장 창고 → 절반씩 낮아지는 금화 계단 → 찢긴 증서와 새 증서 → 가면 쪽지 게시판 → 카페 가격표 → 실로 이은 코르크 판이 차례로 놓인 긴 작업실 | 외부 | P1 |
| cover_ch3 | J | 넷이 함께(블록체인 편 마지막 표지): 박사가 가운데에서 금화 계단(글자 없음)을 가리키고, 초파리와 Money-Robo가 양쪽에서 올려다보고, 하루가 점수판(빈칸 셋)을 든다 | 외부 | P2 |
| thumb_3_01 ~ thumb_3_07 | I | 각 편 bg를 3:2로 자르기 | 직접 | P2 |

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, wide 8:3 background, left side simple and calm for title text, details on the right, a long workshop beside the lab where objects are lined up from left to right like stages: a glowing mining machine next to a wooden lottery box, a distant mining warehouse model, a staircase of gold coin stacks each half the height of the previous, a torn paper note beside two fresh notes, a bulletin board with mask notes, a small cafe chalkboard, and finally a corkboard with strings, warm golden lamp light growing brighter toward the right, no characters, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 2. 페이지별 대표 그림
| 페이지 | 앵커 | bg | outro | 상태 |
|---|---|---|---|---|
| 3-01 | C | bg_3_01 | sc_3_01_outro | bg 의뢰 · outro 합성본 |
| 3-02 | D | bg_3_02 | sc_3_02_outro | bg 의뢰 · outro 합성본 |
| 3-03 | C | bg_3_03 | sc_3_03_outro | bg 의뢰 · outro 합성본 |
| 3-04 | C | bg_3_04 | sc_3_04_outro | bg 의뢰 · outro 합성본 |
| 3-05 | D | bg_3_05 | sc_3_05_outro | bg 의뢰 · outro 합성본 |
| 3-06 | D | bg_3_06 | sc_3_06_outro | bg 의뢰 · outro 합성본 |
| 3-07 | D | bg_3_07 | sc_3_07_outro | bg 의뢰 · outro 합성본 |

## 3. 새 표정 후보 (시리즈 공용, P2)
| 키 | 대신 쓰는 그림 | 쓰는 곳 | 메모 |
|---|---|---|---|
| doc_scale | doc_e13 | 3-03 무승부 판정 | 수평 놋쇠 저울을 두 손으로. 저장소 E25 후보 |
| asst_ledger | asst_e07 | 모든 편 꾸러미 섹션 | 줄무늬 장부를 펼치고 펜 |

## 4. 의뢰 순서 (Genspark 한 세션)
bg_ch3_index → bg_3_01 … bg_3_07 → (선택) cover_ch3 → (선택) sc_3_0n_outro

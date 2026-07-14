# Plan - Cycle 1: 거터 게임 (오픈 프레임, 보너스 없음)

## 목표
`Game` 클래스 최초 구현. 모든 투구가 거터(0핀)일 때 `score()`가 0을 반환한다.
스트라이크/스페어 보너스 없는 가장 단순한 케이스부터 시작.

## 테스트
- 파일: `test_game.py`
- `test_gutter_game`: `roll(0)`을 20번 호출 후 `score() == 0`

## 접근 방식
- `Game.__init__`: `rolls` 리스트 초기화
- `Game.roll(pins)`: `rolls`에 `pins` append
- `Game.score()`: 우선 `sum(self.rolls)` 반환 (오픈 프레임만 고려, 스페어/스트라이크 보너스는 다음 사이클에서 추가)

## 범위 밖
- 스페어/스트라이크 보너스 (다음 사이클)
- 10번 프레임 보너스 투구 (다음 사이클)
- 입력 검증

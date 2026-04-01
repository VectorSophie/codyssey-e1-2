# Python Quiz Game

## Project Overview

Python으로 만든 터미널 기반 퀴즈 게임입니다. 사용자는 메뉴를 통해 퀴즈를 풀고, 새 문제를 추가하고, 목록과 최고 점수를 확인할 수 있습니다.

## Quiz Theme & Selection Reason

- **Theme**: Programming / Python
- **Reason**: 프로그래밍을 배우는 첫 걸음인 만큼, 우리가 사용하는 Python 언어 자체에 대한 지식을 퀴즈로 풀며 기초를 다지기 위해 선정했습니다.

## Execution

```bash
python main.py
```

## Features

- **Play**: 등록된 퀴즈를 순서대로 풀고 최종 점수를 확인합니다.
- **Add**: 문제, 4개의 선택지, 정답 번호(1~4)를 입력해 퀴즈를 추가합니다.
- **List**: 현재 등록된 퀴즈의 번호와 문제 문장을 출력합니다.
- **Score**: 현재 최고 점수(best score)를 확인합니다.
- **Persistence**: 퀴즈 목록과 최고 점수를 `state.json`에 저장/복원합니다.

## File Structure

- `main.py`: 게임 실행 파일, 메뉴/입력 검증/퀴즈 로직/저장 로직 포함
- `state.json`: 퀴즈 데이터 및 최고 점수 저장 파일
- `README.md`: 프로젝트 설명 문서
- `.gitignore`: Git 추적 제외 파일 설정

## Data File Description

`state.json`은 프로젝트 루트에 위치하며 UTF-8 인코딩으로 저장됩니다.

구조:

```json
{
  "quizzes": [
    {
      "question": "문제 문자열",
      "choices": ["선택지1", "선택지2", "선택지3", "선택지4"],
      "answer": 1
    }
  ],
  "best_score": 0
}
```

- `quizzes`: 퀴즈 객체 배열
  - `question` (string): 문제 문장
  - `choices` (string[4]): 4개의 선택지
  - `answer` (int): 정답 번호(1~4)
- `best_score` (int): 현재까지 기록된 최고 점수

## README 제출 체크리스트

- [x] 프로젝트 개요 작성 완료
- [x] 퀴즈 주제 선정 이유 작성 완료
- [x] 실행 방법 (`python main.py`) 작성 완료
- [x] 기능 목록(퀴즈 풀기/추가/목록/점수) 작성 완료
- [x] 파일 구조 작성 완료
- [x] 데이터 파일 설명(state.json 경로/역할/필드 구조) 작성 완료

---
- Git Clone/Pull test complete.

import json
from typing import Any, cast


class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int):
        if len(choices) != 4:
            raise ValueError("choices must contain exactly 4 items")
        if answer < 1 or answer > 4:
            raise ValueError("answer must be between 1 and 4")

        self.question: str = question
        self.choices: list[str] = choices
        self.answer: int = answer

    def display(self):
        print(self.question)
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")


class QuizGame:
    def __init__(self):
        self.state_file: str = "state.json"
        self.quizzes: list[Quiz] = self.get_default_quizzes()
        self.best_score: int = 0
        self.load_data()

    def get_default_quizzes(self) -> list[Quiz]:
        return [
            Quiz(
                "파이썬에서 리스트의 길이를 구하는 함수는 무엇인가요?",
                ["count()", "size()", "len()", "length()"],
                3,
            ),
            Quiz(
                "다음 중 파이썬의 불리언 값이 아닌 것은 무엇인가요?",
                ["True", "False", "None", "Bool"],
                4,
            ),
            Quiz(
                "파이썬에서 딕셔너리의 키-값 쌍을 순회할 때 주로 사용하는 메서드는?",
                ["pairs()", "items()", "entries()", "values()"],
                2,
            ),
            Quiz(
                "객체 지향 프로그래밍에서 클래스의 인스턴스를 만들 때 사용하는 키워드는?",
                ["class", "new", "create", "instance"],
                2,
            ),
            Quiz(
                "파이썬에서 예외를 처리하는 기본 구문은 무엇인가요?",
                ["if/else", "switch/case", "try/except", "for/while"],
                3,
            ),
        ]

    def save_data(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

        with open(self.state_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def load_data(self):
        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                raw_data: object = json.load(file)

            if not isinstance(raw_data, dict):
                raise ValueError

            data = cast(dict[str, Any], raw_data)

            quizzes_data_obj: Any = data["quizzes"]
            if not isinstance(quizzes_data_obj, list):
                raise ValueError

            quizzes_data = cast(list[Any], quizzes_data_obj)
            loaded_quizzes: list[Quiz] = []
            for item_obj in quizzes_data:
                if not isinstance(item_obj, dict):
                    raise ValueError

                item = cast(dict[str, Any], item_obj)
                question_obj: Any = item.get("question")
                choices_obj: Any = item.get("choices")
                answer_obj: Any = item.get("answer")

                if not isinstance(question_obj, str):
                    raise ValueError
                if not isinstance(choices_obj, list):
                    raise ValueError
                if len(choices_obj) != 4 or not all(
                    isinstance(choice, str) for choice in choices_obj
                ):
                    raise ValueError
                if not isinstance(answer_obj, int):
                    raise ValueError

                choices = cast(list[str], choices_obj)
                loaded_quizzes.append(Quiz(question_obj, choices, answer_obj))

            best_score_obj: Any = data["best_score"]
            if not isinstance(best_score_obj, int) or best_score_obj < 0:
                raise ValueError

            self.quizzes = loaded_quizzes
            self.best_score = best_score_obj
        except (
            FileNotFoundError,
            json.JSONDecodeError,
            OSError,
            KeyError,
            ValueError,
            TypeError,
        ):
            self.quizzes = self.get_default_quizzes()
            self.best_score = 0
            self.save_data()

    def get_safe_int_input(self, prompt: str, min_value: int, max_value: int) -> int:
        while True:
            try:
                raw_value = input(prompt)
            except (KeyboardInterrupt, EOFError):
                raise

            value = raw_value.strip()

            if value == "":
                print("입력이 비어 있습니다. 숫자를 입력해 주세요.")
                continue

            try:
                selected = int(value)
            except ValueError:
                print("숫자 변환에 실패했습니다. 숫자만 입력해 주세요.")
                continue

            if not (min_value <= selected <= max_value):
                print(
                    f"허용 범위를 벗어났습니다. {min_value}~{max_value} 사이 숫자를 입력해 주세요."
                )
                continue

            return selected

    def display_menu(self):
        print("\n=== Python Quiz Game ===")
        print("1. Play")
        print("2. Add")
        print("3. List")
        print("4. Score")
        print("5. Exit")

    def play_quiz(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0
        total = len(self.quizzes)

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{number}/{total}]")
            quiz.display()
            user_answer = self.get_safe_int_input(
                "정답 번호를 선택하세요 (1-4): ", 1, 4
            )

            if user_answer == quiz.answer:
                score += 1
                print("정답입니다!")
            else:
                correct_choice = quiz.choices[quiz.answer - 1]
                print(f"오답입니다. 정답은 {quiz.answer}번 ({correct_choice}) 입니다.")

        print("\n=== 퀴즈 결과 ===")
        print(f"총 {total}문제 중 {score}문제를 맞혔습니다.")

        if score > self.best_score:
            self.best_score = score
            self.save_data()
            print(f"최고 점수를 갱신했습니다! 현재 최고 점수: {self.best_score}")

    def add_quiz(self):
        while True:
            question = input("문제를 입력하세요: ").strip()
            if question == "":
                print("문제는 비워둘 수 없습니다. 다시 입력해 주세요.")
                continue
            break

        choices: list[str] = []
        for index in range(1, 5):
            while True:
                choice = input(f"선택지 {index}을(를) 입력하세요: ").strip()
                if choice == "":
                    print("선택지는 비워둘 수 없습니다. 다시 입력해 주세요.")
                    continue
                choices.append(choice)
                break

        answer = self.get_safe_int_input("정답 번호를 입력하세요 (1-4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        self.save_data()
        print("퀴즈가 추가되었습니다.")

    def list_quizzes(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n=== 퀴즈 목록 ===")
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

    def check_best_score(self):
        print(f"현재 최고 점수는 {self.best_score}점입니다.")

    def run(self):
        while True:
            try:
                self.display_menu()
                menu = self.get_safe_int_input("메뉴를 선택하세요 (1-5): ", 1, 5)

                if menu == 1:
                    self.play_quiz()
                elif menu == 2:
                    self.add_quiz()
                elif menu == 3:
                    self.list_quizzes()
                elif menu == 4:
                    self.check_best_score()
                elif menu == 5:
                    print("게임을 종료합니다.")
                    break
            except (KeyboardInterrupt, EOFError):
                print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
                break


if __name__ == "__main__":
    game = QuizGame()
    game.run()

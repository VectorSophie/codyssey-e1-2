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
        self.quizzes: list[Quiz] = [
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

    def play(self):
        print("[Placeholder] Play 기능은 아직 구현되지 않았습니다.")

    def add(self):
        print("[Placeholder] Add 기능은 아직 구현되지 않았습니다.")

    def list_questions(self):
        print("[Placeholder] List 기능은 아직 구현되지 않았습니다.")

    def score(self):
        print("[Placeholder] Score 기능은 아직 구현되지 않았습니다.")

    def run(self):
        while True:
            try:
                self.display_menu()
                menu = self.get_safe_int_input("메뉴를 선택하세요 (1-5): ", 1, 5)

                if menu == 1:
                    self.play()
                elif menu == 2:
                    self.add()
                elif menu == 3:
                    self.list_questions()
                elif menu == 4:
                    self.score()
                elif menu == 5:
                    print("게임을 종료합니다.")
                    break
            except (KeyboardInterrupt, EOFError):
                print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
                break


if __name__ == "__main__":
    game = QuizGame()
    game.run()

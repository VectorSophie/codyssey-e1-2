class QuizGame:
    def __init__(self):
        pass

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

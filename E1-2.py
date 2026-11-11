import json
import os


STATE_FILE = "state.json"


class Quiz:
    """
    퀴즈 1개를 표현하는 클래스
    """

    def __init__(self, question, choices, answer):
        self.question = question      # 문제
        self.choices = choices        # 선택지 4개
        self.answer = answer          # 정답 번호, 1~4

    def show(self):
        """
        퀴즈를 화면에 출력하는 메서드
        """
        print("\n문제:", self.question)

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        """
        사용자의 답이 정답인지 확인하는 메서드
        """
        return user_answer == self.answer

    def to_dict(self):
        """
        Quiz 객체를 JSON에 저장할 수 있는 딕셔너리로 바꾸는 메서드
        """
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @staticmethod
    def from_dict(data):
        """
        JSON에서 읽은 딕셔너리를 Quiz 객체로 바꾸는 메서드
        """
        return Quiz(
            data["question"],
            data["choices"],
            data["answer"]
        )


class QuizGame:
    """
    퀴즈 게임 전체를 관리하는 클래스
    """

    def __init__(self):
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def get_default_quizzes(self):
        """
        기본 퀴즈 5개를 만드는 메서드
        주제: 동물 상식
        """
        return [
            Quiz(
                "강아지는 보통 어떤 소리를 낼까요?",
                ["야옹", "멍멍", "꽥꽥", "음메"],
                2
            ),
            Quiz(
                "고양이가 좋아하는 대표적인 장난감은 무엇일까요?",
                ["공", "실뭉치", "숟가락", "연필"],
                2
            ),
            Quiz(
                "가장 키가 큰 동물은 무엇일까요?",
                ["코끼리", "기린", "사자", "말"],
                2
            ),
            Quiz(
                "펭귄은 주로 어디에서 잘 살까요?",
                ["추운 곳", "사막", "정글", "우주"],
                1
            ),
            Quiz(
                "토끼가 좋아하는 음식으로 가장 잘 알려진 것은?",
                ["당근", "고기", "초콜릿", "커피"],
                1
            )
        ]

    def load_state(self):
        """
        state.json 파일에서 퀴즈와 최고 점수를 불러오는 메서드
        파일이 없거나 손상되었으면 기본 퀴즈를 사용한다.
        """
        if not os.path.exists(STATE_FILE):
            print("저장 파일이 없어 기본 퀴즈를 불러옵니다.")
            self.quizzes = self.get_default_quizzes()
            self.best_score = None
            self.save_state()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.quizzes = []

            for quiz_data in data.get("quizzes", []):
                quiz = Quiz.from_dict(quiz_data)
                self.quizzes.append(quiz)

            self.best_score = data.get("best_score")

            if len(self.quizzes) == 0:
                print("저장된 퀴즈가 없어 기본 퀴즈를 불러옵니다.")
                self.quizzes = self.get_default_quizzes()

        except Exception:
            print("저장 파일이 손상되었습니다.")
            print("기본 퀴즈 데이터로 다시 시작합니다.")

            self.quizzes = self.get_default_quizzes()
            self.best_score = None
            self.save_state()

    def save_state(self):
        """
        퀴즈와 최고 점수를 state.json 파일에 저장하는 메서드
        """
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        try:
            with open(STATE_FILE, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except Exception:
            print("파일 저장 중 문제가 발생했습니다.")

    def input_number(self, message, min_number, max_number):
        """
        숫자를 입력받는 메서드
        잘못 입력하면 다시 입력받는다.
        """
        while True:
            user_input = input(message).strip()

            if user_input == "":
                print("아무것도 입력하지 않았습니다. 다시 입력하세요.")
                continue

            try:
                number = int(user_input)
            except ValueError:
                print("숫자만 입력할 수 있습니다. 다시 입력하세요.")
                continue

            if number < min_number or number > max_number:
                print(f"{min_number}부터 {max_number} 사이의 숫자를 입력하세요.")
                continue

            return number

    def input_text(self, message):
        """
        글자를 입력받는 메서드
        빈 입력은 다시 입력받는다.
        """
        while True:
            text = input(message).strip()

            if text == "":
                print("빈칸으로 둘 수 없습니다. 다시 입력하세요.")
                continue

            return text

    def show_menu(self):
        """
        메뉴를 출력하는 메서드
        """
        print("\n==============================")
        print("        동물 상식 퀴즈 게임")
        print("==============================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 종료")

    def play_quiz(self):
        """
        퀴즈를 푸는 메서드
        """
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n퀴즈를 시작합니다!")

        correct_count = 0
        total_count = len(self.quizzes)

        for quiz in self.quizzes:
            quiz.show()

            user_answer = self.input_number("정답 번호를 입력하세요: ", 1, 4)

            if quiz.is_correct(user_answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print("\n퀴즈가 끝났습니다!")
        print(f"결과: {correct_count}개 정답 / 총 {total_count}문제")

        self.update_best_score(correct_count, total_count)
        self.save_state()

    def update_best_score(self, correct_count, total_count):
        """
        최고 점수를 갱신하는 메서드
        """
        current_rate = correct_count / total_count

        if self.best_score is None:
            self.best_score = {
                "correct": correct_count,
                "total": total_count
            }
            print("첫 점수가 저장되었습니다!")
            return

        best_correct = self.best_score["correct"]
        best_total = self.best_score["total"]
        best_rate = best_correct / best_total

        if current_rate > best_rate:
            self.best_score = {
                "correct": correct_count,
                "total": total_count
            }
            print("축하합니다! 최고 점수가 갱신되었습니다!")
        else:
            print("최고 점수는 갱신되지 않았습니다.")

    def add_quiz(self):
        """
        새 퀴즈를 추가하는 메서드
        """
        print("\n새 퀴즈를 추가합니다.")

        question = self.input_text("문제를 입력하세요: ")

        choices = []

        for i in range(1, 5):
            choice = self.input_text(f"{i}번 선택지를 입력하세요: ")
            choices.append(choice)

        answer = self.input_number("정답 번호를 입력하세요, 1~4: ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        self.save_state()

        print("퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        """
        퀴즈 목록을 보여주는 메서드
        """
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n퀴즈 목록")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}] {quiz.question}")

            for i, choice in enumerate(quiz.choices, start=1):
                print(f"  {i}. {choice}")

            print(f"  정답: {quiz.answer}번")

    def show_best_score(self):
        """
        최고 점수를 보여주는 메서드
        """
        print("\n최고 점수 확인")

        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
            return

        correct = self.best_score["correct"]
        total = self.best_score["total"]
        rate = correct / total * 100

        print(f"최고 점수: {correct}개 정답 / 총 {total}문제")
        print(f"정답률: {rate:.1f}%")

    def run(self):
        """
        게임을 실행하는 메서드
        """
        try:
            while True:
                self.show_menu()

                menu = self.input_number("메뉴 번호를 선택하세요: ", 1, 5)

                if menu == 1:
                    self.play_quiz()
                elif menu == 2:
                    self.add_quiz()
                elif menu == 3:
                    self.show_quiz_list()
                elif menu == 4:
                    self.show_best_score()
                elif menu == 5:
                    print("게임을 종료합니다.")
                    self.save_state()
                    break

        except KeyboardInterrupt:
            print("\nCtrl+C가 입력되었습니다.")
            print("현재 데이터를 저장하고 안전하게 종료합니다.")
            self.save_state()

        except EOFError:
            print("\n입력이 종료되었습니다.")
            print("현재 데이터를 저장하고 안전하게 종료합니다.")
            self.save_state()


if __name__ == "__main__":
    game = QuizGame()
    game.run()
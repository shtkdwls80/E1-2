[과제 목표]

1. Python 기초

1) 변수가 무엇이고, 왜 사용하는지 설명할 수 있다.
   => 하나의 값을 미리 저장해두고 필요할 때 꺼내 사용하는 공간
      STATE_FILE = "state.json"에서와 같이 "state.json"를 STATE_FILE라는 한번만 정의해두면
      나중에 필요할 때 꺼내서 사용함.

    예)
    STATE_FILE = "state.json"      # 저장 파일 이름
    correct_count = 0              # 맞힌 개수
    total_count = len(self.quizzes)  # 전체 문제 수



2) int, str, bool, list, dict의 차이를 설명할 수 있다.
 
자료형  퀴즈 게임에서의 사용	            코드 예
int   	정답 번호, 맞힌 개수, 메뉴 번호  	self.answer = 2, correct_count += 1
str  	문제, 선택지, 사용자 입력	      "강아지는 보통 어떤 소리를 낼까요?"
bool	정답 여부                      	is_correct()가 True/False 반환
list	선택지 4개, 퀴즈 목록	         ["야옹", "멍멍", "꽥꽥", "음메"], self.quizzes
dict	최고 점수, JSON 저장용 데이터	  {"correct": 4, "total": 5}

   

3) if/elif/else로 조건에 따라 다른 동작을 수행할 수 있다.
   if : 조건문
   elif : 조건 외(if 다음 조건)
   else : 그 외(전체 부정)

   예)
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



4) for와 while의 차이를 설명하고 적절히 선택할 수 있다.
   (1) for : 반복횟수와 대상이 정해져 있다(리스트 요소를 하나씩 처리)
   (2) While : 조건이 참인 동안 계속 반복(올바른 입력이 들어올때까지 반복)
   ※ 몇번 돌지 알면 for, 언제 끝날지 모르면 While


	       코드에서의 사용	                    이유
for	      for quiz in self.quizzes:	    퀴즈 개수가 정해져 있어서 하나씩 처리
for	      for i in range(1, 5):     	선택지를 정확히 4번 입력받음
while	  input_number()의 while True:	올바른 입력이 들어올 때까지 몇 번이 될지 모르게 반복
while	  run()의 while True:	        사용자가 “5. 종료”를 선택할 때까지 메뉴를 계속 반복


# for: 횟수/대상이 정해져 있음
for quiz in self.quizzes:
    quiz.show()

# while: 조건이 맞을 때까지 계속
while True:
    user_input = input(message).strip()
    ...
    return number      # 올바른 값이면 여기서 반복 종료







5) 함수를 정의하고, 매개변수와 반환값을 활용할 수 있다.
   함수 : 자주 사용하는 동작에 이름을 붙여서 묶어 둔 것
   매개변수 : 함수가 받는 입력값
   반환값 : 함수가 돌려주는 결과(return)

def input_number(self, message, min_number, max_number):
    ...
    return number

매개변수: message(안내 문구), min_number, max_number(허용 범위)
반환값: 검증을 통과한 숫자 (return number)




2.클래스와 객체

1) 클래스가 무엇이고, 왜 사용하는지 설명할 수 있다.
   관련 데이터와 기능을 한 곳에 모아 코드를 정리해둔 곳
   나중에 코드의 유지보수와 최초 작성시 동일 또는 유사한 코드를 모아서 작성시 편리함
 class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

2)__init__ 메서드와 self의 역할을 설명할 수 있다.
  __init__ : 객체를 만들때 자동으로 실행되는 최기화 메서드. 속성의 첫 값을 정함.
  self : 객체 자기 자신을 가리킴.

def __init__(self):
    self.quizzes = []
    self.best_score = None
    self.load_state()      # 객체 생성과 동시에 저장 데이터 로드


3) 클래스의 속성(attribute)과 메서드(method)를 정의하고 활용할 수 있다.

   속성은 객체가 가진 데이터이고, 메서드는 객체가 할 수 있는 동작입니다.
   quiz.show()                       # 메서드 호출: 문제 출력
   quiz.is_correct(user_answer)      # 메서드 호출: 정답 확인
   quiz.answer                       # 속성 접근: 정답 번호



3. 파일 입출력

1) 파일을 열고, 읽고, 쓰는 기본 과정을 설명할 수 있다.
# 쓰기 (save_state)
with open(STATE_FILE, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# 읽기 (load_state)
with open(STATE_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

2)JSON 형식이 무엇이고, 왜 데이터 저장에 사용하는지 설명할 수 있다.2
  JSON은 데이터를 텍스트로 표현하는 형식으로, 파이썬의 dict/list와 모양이 거의 같습니다. state.json은 이렇게 저장됩니다.
{
    "quizzes": [
        {"question": "강아지는 보통 어떤 소리를 낼까요?", "choices": ["야옹", "멍멍", "꽥꽥", "음메"], "answer": 2}
    ],
    "best_score": {"correct": 4, "total": 5}
}

3)try/except를 사용하여 오류를 처리할 수 있다.

이 프로젝트에서 try/except는 네 군데에서 쓰입니다.

위치	         잡는 오류	                     처리
input_number()	ValueError (숫자가 아닌 입력)	"숫자만 입력할 수 있습니다." 후 재입력
load_state()	Exception (파일 손상 등)    	기본 퀴즈로 초기화 후 계속 실행
save_state()	Exception (저장 실패)	       안내 메시지 출력
run()	       KeyboardInterrupt, EOFError	  데이터를 저장하고 안전하게 종료

try:
    number = int(user_input)
except ValueError:
    print("숫자만 입력할 수 있습니다. 다시 입력하세요.")
    continue

    오류가 나도 프로그램이 죽지 않고 안내 후 계속 진행되는 것이 핵심입니다. 특히 load_state()는 state.json이 망가져도 게임이 시작되도록 해 줍니다.



4.t 기초

1) git이 무엇이고 왜 필요한지 설명할 수 있다.
Git은 파일의 변경 이력을 기록하는 버전 관리 시스템입니다. 퀴즈 게임으로 예를 들면 이렇습니다.

코드를 고치다가 오류가 생겼을 때 잘 돌아가던 시점으로 되돌릴 수 있습니다.
"최고 점수 기능 추가", "입력 검증 추가"처럼 변경 이력이 기록됩니다.
새 기능을 브랜치로 따로 실험하고, 잘 되면 합칠 수 있습니다.
GitHub에 올려 두면 다른 컴퓨터에서도 가져와서 쓸 수 있습니다.


2) init, add, commit, push, pull, checkout, clone이 각각 무엇을 하는지 설명할 수 있다.
git init                          # D:\Test\E1-2 폴더를 Git 저장소로 만듦
git add E1-2.py Readme.md         # 이 파일들의 변경을 커밋 대상으로 올림
git commit -m "퀴즈 게임 초기 버전"  # 변경을 하나의 기록으로 저장
git push                          # 내 커밋을 GitHub로 올림
git pull                          # GitHub의 변경사항을 내려받아 합침
git checkout 브랜치명               # 다른 브랜치나 커밋으로 이동
git clone 저장소주소                # GitHub 저장소를 통째로 내 컴퓨터로 복사


3) 브랜치를 생성하고 병합할 수 있다.
"퀴즈 삭제 기능"을 추가한다고 가정해 봅니다.
git checkout -b feature-delete    # 새 브랜치를 만들고 이동
# E1-2.py 수정 후
git add E1-2.py
git commit -m "퀴즈 삭제 기능 추가"
git checkout main                 # main 브랜치로 돌아감
git merge feature-delete          # 변경을 main에 합침

main은 항상 잘 동작하는 상태로 두고, 새 기능은 별도 브랜치에서 만든 뒤 완성되면 합치는 방식입니다. 병합은 합쳐질 쪽(main)으로 먼저 이동한 뒤 실행합니다.

4) 원격 저장소를 clone하고, pull로 변경사항을 가져올 수 있다.

git clone https://github.com/계정명/저장소명.git   # 처음 한 번: 전체 가져오기
cd 저장소명
git pull                                          # 이후: 새 변경사항만 갱신

다른 컴퓨터에서 퀴즈 게임을 이어서 작업한다면, 처음에 clone으로 가져오고 그 뒤로는 작업 전에 pull로 최신 상태를 받으면 됩니다.
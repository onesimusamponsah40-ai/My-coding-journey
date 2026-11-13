import random


#use dictionary to store the questions
quiz_questions = {

    1 : {
        "question": "Who is the only player in history to win three FIFA World Cups?",
        "check" : "pele",
        "answer": "Pelé achieved this feat with Brazil in 1958, 1962, and 1970. No other player has matched his record."
    },
    2 : {
        "question" : "Which club has won the most UEFA Champions League titles?",
        "check" : "real madrid",
        "answer" : "Real Madrid holds the all-time record with 15 European Cups. They remain well ahead of second-place AC Milan, who have seven."
    },
    3 : {
        "question" : "Who holds the record for the fastest hat-trick in Premier League history?",
        "check" : "sadio mane",
        "answer" : "Sadio Mané scored three goals in just 2 minutes and 56 seconds for Southampton against Aston Villa in 2015."
    },
    4 : {
        "question" : "Which country won the very first FIFA World Cup in 1930?",
        "check" : "uruguay",
        "answer" : "Uruguay won the inaugural tournament on home soil, defeating Argentina 4–2 in the final."
    },
    5 : {
        "question" : "What is the only team to finish an entire 38-game Premier League season unbeaten?",
        "check" : "arsenal",
        "answer" : "Arsenal accomplished this during the 2003–04 campaign, earning the nickname The Invincibles with 26 wins and 12 draws."
    },

    6 : {
        "question" : "Who is the greatest footballer of all time, Lionel Messi or Cristiano Ronaldo?",
        "check" : "messi",
        "answer" : "This classic debate pits Messi's playmaking, dribbling, and World Cup triumph against Ronaldo's unmatched goal-scoring longevity and Champions League dominance."
    },
    7 : {
        "question" : "Which domestic league is the most competitive in the world?",
        "check": "premier league",
        "answer" : "Fans often compare the physical pace and financial depth of the Premier League against the technical quality of La Liga and the tactical discipline of Serie A."
    }
}
#this shuffles the questions and pick them at random
random_questions = list(quiz_questions.values())
random.shuffle(random_questions)
#this is a function that shows the user the questions and also check if the answer is correct or not
print("Quiz Soccer Edition\n")
def show_questions(number,questions_text,check_answers,answer_text,player_score):
    user_answer = input(f"{number}. {questions_text}\nanswer: ")
    if user_answer.strip().lower() == check_answers:
        print("Correct")
        player_score += 1
    else:
        print("Wrong")
    print(f"Answer: {answer_text}")

    print("\n")
    return player_score
    #variable for score
score = 0
#this goes into the Data"quiz_question" and get the questions and answers also the function can display it
for number, data in enumerate(random_questions, start=1):
    score = show_questions(number, data["question"], data["check"], data["answer"], score)
#this print the total score
print(f"total score: {score}/{len(quiz_questions)}")

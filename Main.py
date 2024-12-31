# configuring the model
import google.generativeai as genai
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# function to calculate the result
def determine_result(answer_store):
    score = 0
    pass_threshold = 4
    keywords = ["skills", "experience", "technology", "problem-solving", "motivated", "contribution","Lead", "collaborate", "articulate", "engage","leadership", "initiative", "drive", "responsible", "team lead", "project management" ]
    
    for keyword in keywords:
     if keyword.lower() in answer_store.lower():
            score += 1
    if score >= pass_threshold:
        print("Interview Result: Pass")
    else:
        print("Interview Result: Fail")

answer_store = ""
Question_list = ["Consider yourself as a hiring manager, You should speak in a formal and confident tone. Ask for introduction. Only once you get the answer ask one followup question related to the previous response." , "Consider yourself as a hiring manager, dont greet, You should speak in a confident and formal tone. Ask a question about computer technology based on the interests of user as specified in introduction. Only once you get the answer ask one followup question related to the previous response." , " Consider yourself as a hiring manager, dont greet, You should speak in a formal and confident tone. Ask why should we hire you. Only once you get the answer ask one followup question related to the previous response."]
# loop for generating and printing questions
for question_number in range(len(Question_list)):
    question_prompt = Question_list[question_number]
    try:
       question_response = model.generate_content(question_prompt + answer_store)
       prompt = question_prompt
       question = question_response.text if hasattr(question_response, 'text') else "Could not fetch question"
    except Exception as e:
         print("Error generating question:", e)
         continue
    print("\nInterviewer:", question)
    print("\n")
    user_answer = input("Your answer: ")
    answer_store += "" + user_answer
    try:
      follow_up_prompt = f"Generate a follow-up question based on this answer: {user_answer}"
      follow_up_response = model.generate_content(follow_up_prompt + answer_store)
      follow_up_question = follow_up_response.text if hasattr(follow_up_response, 'text') else "Could not fetch follow-up question"
    except Exception as e:
        print("Error generating follow-up question:", e)
        follow_up_question = "Could not fetch follow-up question due to an error."
    print("\nInterviewer:", follow_up_question)
    print("\n")
    user_answer = input("Your answer: ")
    answer_store += "" + user_answer
# calculating the result
determine_result(answer_store)

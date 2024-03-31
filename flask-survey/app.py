# import the necessary modules from Flask.
from flask import Flask, render_template, redirect, url_for
from surveys import satisfaction_survey, personality_quiz

#create an instance of the Flask class and initialize an empty list called responses
app = Flask(__name__)
responses = []

# define a dictionary called survey that contains the title, instructions, and questions for the survey.
survey = {
    "title": "Customer Satisfaction Survey",
    "instructions": "Please fill out a survey about your experience with us.",
    "questions": [
        "Have you shopped here before?",
        "Did someone else shop with you today?",
        "On average, how much do you spend a month on frisbees?",
        "Are you likely to shop here again?",
    ]
}

#The `show_survey_start` function is a route handler for the root route `/`. It renders a template called `survey_start.html` and passes the `survey` dictionary to the template. This template should display the title and instructions of the survey, and include a button that links to `/questions/0`.
@app.route('/')
def show_survey_start():
    return render_template('survey_start.html', survey=survey)

if __name__ == "__main__":
    app.run(debug=True)
    
#show_question is a route handler for the /questions/<idx> route. It takes an argument idx, which is the index of the question in the questions list. It then renders a template called question.html and passes the question at the given index to the template.
@app.route('/questions/<int:idx>')
def show_question(idx):
    # Add your code here to handle the question
    return render_template('question.html', question=survey['questions'][idx])
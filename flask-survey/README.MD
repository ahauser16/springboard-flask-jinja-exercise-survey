# Project Title

## Description

A brief description of what this project does and who it's for.

## Installation

Provide step by step series of examples and explanations about how to get a development environment running.

```bash
git clone <your-repo-link>
cd <your-repo-name>
npm install

Usage
Provide instructions and examples for use.

Contributing
Details about how to contribute to this project.

License
Information about the license.

```

## Project Instructions:

### Step Zero: Setup

Create a new virtual environment and activate it.

Install Flask and the Flask Debug Toolbar.

Make your project a Git repository, and add **_venv/_** and **\_**pycache**\_** to a new **_.gitignore_** file for your repository.

### Step One: Surveys

We’ve provided a file, **_surveys.py_**, which includes classes for **_Question_** (a single question on a survey, with a question, a list of choices, and whether or not that question should allow for comments) and **_Survey_** (a survey, which has a title, instructions, and a list of **_Question_** objects).

For the main part of this exercise, you’ll only need to worry about the **_satisfaction_survey_** survey in that file. It does not include any questions that allow comments, so you can skip that for now. (Ignore the personality quiz and the **_surveys_** object; those come into play only in the Further Study).

Play with the **_satisfaction_survey_** in ipython to get a feel for how it works: it is an instance of the **_Survey_** class, and its **_.questions_** attribute is a list of instances of the **_Question_** class. You’ll need to understand this structure well, so don’t move on until you feel comfortable with it.

### Step Two: The Start Page

For now, we’ll keep track of the user’s survey responses with a list in the outermost scope in your **_app.py_**. To begin, initialize a variable called **_responses_** to be an empty list. As people answer questions, you should store their answers in this list.

For example, at the end of the survey, you should have in memory on the server a list that looks like this:

```
['Yes', 'No', 'Less than $10,000', 'Yes']
```

Next, let’s handle our first request. When the user goes to the root route, render a page that shows the user the title of the survey, the instructions, and a button to start the survey. The button should serve as a link that directs the user to **_/questions/0_** (the next step will define that route).

Be sure to create a **_base.html_** and use template inheritance!

### Step Three: The Question Page

Next, build a route that can handle questions — it should handle URLs like **_/questions/0_** (the first question), **_/questions/1_**, and so on.

When the user arrives at one of these pages, it should show a form asking the current question, and listing the choices as radio buttons. Answering the question should fire off a POST request to **_/answer_** with the answer the user selected (we’ll handle this route next).

### Step Four: Handling Answers

When the user submits an answer, you should append this answer to your **_responses_** list, and then **redirect** them to the next question.

The Flask Debug Toolbar will be **very useful** in looking at the submitted form data.

### Step Five: Thank The User

The customer satisfaction survey only has 4 questions, so once the user has submitted four responses, there is no new question to task. Once the user has answered all questions, rather than trying to send them to /questions/5, redirect them to a simple “Thank You!” page.

**_Note: It’s possible that, in the future, this survey may include more than four questions, so don’t hard-code 5 as the end. Do this in a way that can handle any number of questions._**

### Step Six: Protecting Questions

Right now, your survey app might be buggy. Once people know the URL structure, it’s possible for them to manually go to **_/questions/3_** before they’ve answered questions 1 and 2. They could also try to go to a question id that doesn’t exist, like **_/questions/7_**.

To fix this problem, you can modify your view function for the question show page to look at the number in the URL and make sure it’s correct. If not, you should redirect the user to the correct URL.

For example, if the user has answered one survey question, but then tries to manually enter **_/questions/4_** in the URL bar, you should redirect them to **_/questions/1_**.

Once they’ve answered all of the questions, trying to access any of the question pages should redirect them to the thank you page.

**\*💡 **Note:** Once this functionality is built, there’s no way to reset the survey. Once it’s complete, you can only see the start page and the thank you page. By stopping and starting your server, you can complete the survey again (since every time the server starts, Flask reads the \***app.py**_ and re-initializes _**responses**_ to an empty list. We’ll fix this problem in Step Eight._**

### Step Seven: Flash Messages

Using flash, if the user does try to tinker with the URL and visit questions out of order, flash a message telling them they’re trying to access an invalid question as part of your redirect.

### Step Eight: Using the Session

Storing answers in a list on the server has some problems. The biggest one is that there’s only one list – if two people try to answer the survey at the same time, they’ll be stepping on each others’ toes!

A better approach is to use the session to store response information, so that’s what we’d like to do next. **If you haven’t learned about the session yet, move on to step 9 and come back to this later.**

To begin, modify your start page so that clicking on the button fires off a POST request to a new route that will set **_session[“responses”]_** to an empty list. The view function should then redirect you to the start of the survey. (This will also take care of the issue mentioned at the end of Step Six.) Then, modify your code so that you reference the session when you’re trying to edit the list of responses.

**_Note: Why are we changing “Start Survey” button from sending a GET request to sending a POST request? Feel free to ask for some support on this question._**

**_Note: When it comes time to modify the session, watch out. Normally, you can append to a list like this:_**

`fruits.append("cherry")`

However, for a list stored in the session, you’ll need to rebind the name in the session, like so:

```
fruits = session['fruits']
fruits.append("cherry")
session['fruits'] = fruits
```

### Step Nine: Celebrate!

Good work!

### FURTHER STUDY

#### FS One: Base Templates

You probably have some repetitive text in the HTML templates (for any page headers/footers/etc). Make a base template and have your other templates inherit from this.

As a hint: you’ll probably want at least two “blocks” one for the page title, in the head section, and one for the content of the page.

#### FS Two: Multiple Surveys

Make your system able to handle more than one survey — we’ve provided a second survey in surveys.py, and provided a dictionary mapping a survey “code” to the survey object.

Add a page that lets the user pick the survey they want to fill out: it should list the available surveys. It should then take you to the start page you made earlier, except for this survey.

You’ll need to figure out a good way to keep track of the survey the user is filling out as they move through the system.

#### FS Three: Allow Comments for Some Questions

The personality quiz survey uses a new feature of the surveys: one of its questions is marked as allowing comments. For this question, you should show the radio buttons of the choices, as usual, but also a multiline text box where the visitor can enter a comment.

You should keep track of the textual comments as well as the radio-button choices. Figure out a good data structure to keep track of these things.

#### FS Four: Much Nicer Thanks Page

Remake your “thanks!” page that is shown at the end of the survey—instead of just saying “thanks”, it should list each question and the provided answer (including any comments), like this:

- **Do you like pretzels?** Yes
- **Are you hungry?** No
- **Do you like burritos, and, if so, what is your favorite kind?** Yes Carnitas

#### FS Five: Prevent Re-Submission

We don’t want users to submit a survey more than once.

Of course, you could put something in the session that says they’ve completed that survey, and check for that, but the cookies that support the session typically only last as long as the browser is running — a user who quits their browser could re-answer the survey.

Figure out a way you could prevent a site visitor from re-filling-out a survey using cookies.

#### FS Six: Lots of Other Ideas

Finish all of these? Want more challenges over the weeeknd? Here are lots of potential ideas to polish this:

- add Bootstrap to your site
- allow users to skip a question
- allow users to go back to a previously-answered question on the survey and change their answer
- ambitious, weekend project: make a web interface to allow users to create surveys through the web (you can mutate the surveys object to append a newly-designed survey to it)

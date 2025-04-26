# here are question for test quiz

class test:
    def __init__(self):
        self.quiz_data = {
    'html': [
        {'question': 'What does HTML stand for?', 'options': ['HyperText Markup Language', 'HyperText Machine Language', 'HyperTool Markup Language'], 'correct': 'HyperText Markup Language'},
        {'question': 'Which HTML tag is used to define an internal style sheet?', 'options': ['<style>', '<script>', '<link>'], 'correct': '<style>'},
        {'question': 'Which attribute is used to provide the URL for a link?', 'options': ['url', 'src', 'href'], 'correct': 'href'},
        {'question': 'Which HTML tag is used to define a table?', 'options': ['<table>', '<tr>', '<td>'], 'correct': '<table>'},
        {'question': 'Which of the following is the correct HTML tag for inserting a line break?', 'options': ['<br>', '<break>', '<newline>'], 'correct': '<br>'},
        {'question': 'What is the correct HTML element for the largest heading?', 'options': ['<head>', '<h1>', '<h6>'], 'correct': '<h1>'},
        {'question': 'Which HTML tag is used to define an unordered list?', 'options': ['<ol>', '<ul>', '<list>'], 'correct': '<ul>'},
        {'question': 'Which HTML tag is used to display an image?', 'options': ['<src>', '<img>', '<picture>'], 'correct': '<img>'},
        {'question': 'How do you create a hyperlink in HTML?', 'options': ["<a href='url'>link</a>", "<link href='url'>link</link>", "<url>link</url>"], 'correct': "<a href='url'>link</a>"},
        {'question': 'What does the <meta> tag define in HTML?', 'options': ['Metadata about the HTML document', 'An external stylesheet link', 'The main content of the webpage'], 'correct': 'Metadata about the HTML document'}
    ],
    'css': [
        {'question': 'What does CSS stand for?', 'options': ['Cascading Style Sheets', 'Creative Style Sheets', 'Computer Style Sheets'], 'correct': 'Cascading Style Sheets'},
        {'question': 'Which property is used to change the background color?', 'options': ['background-color', 'color', 'bg-color'], 'correct': 'background-color'},
        {'question': 'How do you apply a class to an HTML element?', 'options': ["class='name'", "id='name'", "class='name' id='name'"], 'correct': "class='name'"},
        {'question': 'Which CSS property is used to change the text color?', 'options': ['text-color', 'font-color', 'color'], 'correct': 'color'},
        {'question': 'Which CSS selector is used to target an ID?', 'options': ['#', '.', '$'], 'correct': '#'},
        {'question': 'How do you center an element horizontally in CSS?', 'options': ['margin: 0 auto;', 'center: true;', 'align: center;'], 'correct': 'margin: 0 auto;'},
        {'question': 'Which property is used to set the width of a div?', 'options': ['width', 'height', 'size'], 'correct': 'width'},
        {'question': 'Which CSS property is used to change the font size?', 'options': ['font-size', 'font', 'text-size'], 'correct': 'font-size'},
        {'question': 'How do you add a border to an element in CSS?', 'options': ['border: solid;', 'border: 1px;', 'border-width: 2px;'], 'correct': 'border: solid;'},
        {'question': 'Which CSS property is used to control the space between elements?', 'options': ['padding', 'margin', 'spacing'], 'correct': 'margin'}
    ],
    'javascript': [
        {'question': 'Which company developed JavaScript?', 'options': ['Netscape', 'Mozilla', 'Google'], 'correct': 'Netscape'},
        {'question': 'Which symbol is used for comments in JavaScript?', 'options': ['//', '#', '--'], 'correct': '//'},
        {'question': 'How do you declare a variable in JavaScript?', 'options': ['var x;', 'int x;', 'let x;'], 'correct': 'var x;'},
        {'question': 'Which method is used to find an element in an array in JavaScript?', 'options': ['find()', 'get()', 'search()'], 'correct': 'find()'},
        {'question': 'Which of these is NOT a data type in JavaScript?', 'options': ['Integer', 'Number', 'String'], 'correct': 'Integer'},
        {'question': 'What does DOM stand for in JavaScript?', 'options': ['Document Object Model', 'Data Object Method', 'Domain Object Management'], 'correct': 'Document Object Model'},
        {'question': 'What is the result of 5 + "5" in JavaScript?', 'options': ['55', '10', 'Error'], 'correct': '55'},
        {'question': 'Which method is used to add an element to the end of an array?', 'options': ['push()', 'add()', 'append()'], 'correct': 'push()'},
        {'question': 'Which function is used to display an alert box in JavaScript?', 'options': ['alert()', 'msg()', 'popup()'], 'correct': 'alert()'},
        {'question': 'How do you create a function in JavaScript?', 'options': ['function myFunc()', 'create function myFunc()', 'function = myFunc()'], 'correct': 'function myFunc()'}
    ],
    'python': [
        {'question': 'What is the correct syntax for defining a function in Python?', 'options': ['def function_name():', 'function_name[]:', 'def function_name[]:'], 'correct': 'def function_name():'},
        {'question': 'Which of the following is used to define a list in Python?', 'options': ['[]', '()', '{}', '||'], 'correct': '[]'},
        {'question': 'How do you insert a comment in Python?', 'options': ['# This is a comment', '// This is a comment', '/* This is a comment */'], 'correct': '# This is a comment'},
        {'question': 'Which of the following is the correct syntax for an if statement in Python?', 'options': ['if x > 0:', 'if x > 0 then:', 'if x > 0 do:'], 'correct': 'if x > 0:'},
        {'question': 'How do you create a variable in Python?', 'options': ['x = 10', 'int x = 10', 'create x = 10'], 'correct': 'x = 10'},
        {'question': 'Which function is used to output data in Python?', 'options': ['print()', 'output()', 'echo()'], 'correct': 'print()'},
        {'question': 'Which of these is the correct way to define a class in Python?', 'options': ['class MyClass:', 'MyClass class:', 'class MyClass{}'], 'correct': 'class MyClass:'},
        {'question': 'How do you create a dictionary in Python?', 'options': ['{}', '[]', '()'], 'correct': '{}'},
        {'question': 'Which operator is used for exponentiation in Python?', 'options': ['**', '^', '^^'], 'correct': '**'},
        {'question': 'Which of the following is used to loop through a list in Python?', 'options': ['for x in list:', 'loop x in list:', 'foreach x in list:'], 'correct': 'for x in list:'}
    ],
    'flask': [
        {'question': 'What is Flask?', 'options': ['A Python web framework', 'A JavaScript library', 'A database'], 'correct': 'A Python web framework'},
        {'question': 'Which command is used to install Flask?', 'options': ['pip install flask', 'pip install flask-framework', 'npm install flask'], 'correct': 'pip install flask'},
        {'question': 'Which function is used to create a Flask app?', 'options': ['Flask()', 'create_app()', 'initialize()'], 'correct': 'Flask()'},
        {'question': 'What is the default port for Flask app?', 'options': ['5000', '8080', '3000'], 'correct': '5000'},
        {'question': 'Which method is used to handle HTTP GET requests in Flask?', 'options': ['@app.route()', '@app.get()', '@app.request()'], 'correct': '@app.route()'},
        {'question': 'Which decorator is used to create routes in Flask?', 'options': ['@app.route()', '@route()', '@flask.route()'], 'correct': '@app.route()'},
        {'question': 'Which function is used to run a Flask application?', 'options': ['app.run()', 'flask.run()', 'app.execute()'], 'correct': 'app.run()'},
        {'question': 'What is a template engine used in Flask?', 'options': ['Jinja2', 'Handlebars', 'Mustache'], 'correct': 'Jinja2'},
        {'question': 'What method is used to send a response in Flask?', 'options': ['response.send()', 'return()', 'app.send()'], 'correct': 'return()'},
        {'question': 'Which of these is NOT a valid HTTP method in Flask?', 'options': ['PUT', 'DELETE', 'CONNECT'], 'correct': 'CONNECT'}
    ],
    'git': [
        {'question': 'What command is used to initialize a Git repository?', 'options': ['git init', 'git create', 'git start'], 'correct': 'git init'},
        {'question': 'How do you check the status of files in a Git repository?', 'options': ['git status', 'git check', 'git files'], 'correct': 'git status'},
        {'question': 'Which command is used to clone a repository in Git?', 'options': ['git clone', 'git copy', 'git fork'], 'correct': 'git clone'},
        {'question': 'What is the command to add all changes to the staging area?', 'options': ['git add .', 'git stage', 'git include'], 'correct': 'git add .'},
        {'question': 'How do you create a new branch in Git?', 'options': ['git branch <branch_name>', 'git new branch <branch_name>', 'git checkout -b <branch_name>'], 'correct': 'git branch <branch_name>'},
        {'question': 'Which command is used to commit changes in Git?', 'options': ['git commit', 'git push', 'git add'], 'correct': 'git commit'},
        {'question': 'What command is used to merge branches in Git?', 'options': ['git merge', 'git combine', 'git join'], 'correct': 'git merge'},
        {'question': 'Which Git command is used to push changes to a remote repository?', 'options': ['git push', 'git upload', 'git sync'], 'correct': 'git push'},
        {'question': 'How do you pull changes from a remote repository in Git?', 'options': ['git pull', 'git fetch', 'git update'], 'correct': 'git pull'},
        {'question': 'What command is used to view the commit history in Git?', 'options': ['git log', 'git history', 'git commits'], 'correct': 'git log'}
    ],
    'c': [
        {'question': 'Which of the following is used to define a function in C?', 'options': ['void function_name()', 'function_name()', 'def function_name()'], 'correct': 'void function_name()'},
        {'question': 'Which operator is used to assign a value in C?', 'options': ['=', ':', '=='], 'correct': '='},
        {'question': 'Which data type is used to store integers in C?', 'options': ['int', 'float', 'char'], 'correct': 'int'},
        {'question': 'Which function is used to print text in C?', 'options': ['printf()', 'echo()', 'write()'], 'correct': 'printf()'},
        {'question': 'What is the correct way to define a pointer in C?', 'options': ['*ptr', '&ptr', 'ptr*'], 'correct': '*ptr'},
        {'question': 'Which function is used to read input in C?', 'options': ['scanf()', 'input()', 'get()'], 'correct': 'scanf()'},
        {'question': 'Which function is used to open a file in C?', 'options': ['fopen()', 'open()', 'file()'], 'correct': 'fopen()'},
        {'question': 'What is the correct syntax to comment in C?', 'options': ['// comment', '# comment', '/* comment */'], 'correct': '// comment'},
        {'question': 'Which keyword is used to define a constant in C?', 'options': ['const', 'define', 'final'], 'correct': 'const'},
        {'question': 'Which operator is used to get the address of a variable in C?', 'options': ['&', '#', '*'], 'correct': '&'}
    ]
}






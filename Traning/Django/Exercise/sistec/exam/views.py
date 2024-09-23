from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    s= """
    <h1 style="color:blue; text-align: center">Python Basic MCQs</h1>
    <form action="/submit-answers" method="post">
        <div class="question">
            <h3>1. What is the output of the following code: `print(type([]))`?</h3>
            <label><input type="radio" name="q1" value="A"> A. `<class 'list'>`</label><br>
            <label><input type="radio" name="q1" value="B"> B. `<class 'tuple'>`</label><br>
            <label><input type="radio" name="q1" value="C"> C. `<class 'dict'>`</label><br>
            <label><input type="radio" name="q1" value="D"> D. `<class 'set'>`</label>
        </div>

        <div class="question">
            <h3>2. How do you insert a comment in Python code?</h3>
            <label><input type="radio" name="q2" value="A"> A. `// This is a comment`</label><br>
            <label><input type="radio" name="q2" value="B"> B. `<!-- This is a comment -->`</label><br>
            <label><input type="radio" name="q2" value="C"> C. `/* This is a comment */`</label><br>
            <label><input type="radio" name="q2" value="D"> D. `# This is a comment`</label><br>
        </div>

        <div class="question">
            <h3>3. What keyword is used to define a function in Python?</h3>
            <label><input type="radio" name="q3" value="A"> A. `function`</label><br>
            <label><input type="radio" name="q3" value="B"> B. `define`</label><br>
            <label><input type="radio" name="q3" value="C"> C. `func`</label><br>
            <label><input type="radio" name="q3" value="D"> D. `def`</label><br>
        </div>

        <div class="question">
            <h3>4. What is the correct file extension for Python files?</h3>
            <label><input type="radio" name="q4" value="A"> A. `.py`</label><br>
            <label><input type="radio" name="q4" value="B"> B. `.pt`</label><br>
            <label><input type="radio" name="q4" value="C"> C. `.python`</label><br>
            <label><input type="radio" name="q4" value="D"> D. `.pyt`</label><br>
        </div>

        <div class="question">
            <h3>5. How do you create a variable with the numeric value 5 in Python?</h3>
            <label><input type="radio" name="q5" value="A"> A. `int x = 5`</label><br>
            <label><input type="radio" name="q5" value="B"> B. `x = 5`</label><br>
            <label><input type="radio" name="q5" value="C"> C. `var x = 5`</label><br>
            <label><input type="radio" name="q5" value="D"> D. `num x = 5`</label><br>
        </div><br>

        <button type="submit" style="background-color:green">Submit</button>
    </form>"""
    return HttpResponse(s)
# Create your views here.

import uuid
allcourses =  [
    
    {
        "title": """
            7 Days of code :Learn the whole
            concept of Html and Css
        """,
        "names": "Created by mentor Kenny,  mentor sadiq",
        "rating": 5.0,
        "place": 1,
        "price": 100000,
        "image": "Learn HTML5 and CSS3.jpg",
        "link": "html_css",
        "update":"Last updated 31/10/2024",
        
    "goals": [
        "1.Understanding Basics: Teach the foundational concepts of HTML (structure) and CSS (styling), including elements, attributes, selectors, and properties.",
        "2.Building Web Pages: Guide learners through creating simple web pages using semantic HTML and styling them with CSS.",
        "3.Responsive Design: Introduce techniques for making web pages responsive and mobile-friendly, using media queries and flexible layouts.",
        "4.Best Practices: Highlight best practices for coding, including accessibility, semantic markup, and CSS organization.",
        "5.Problem-Solving Skills: Foster critical thinking and problem-solving abilities by presenting common challenges and solutions in web development.",
        "6.Hands-on Projects: Provide practical projects and exercises to reinforce learning and encourage experimentation.",
        "7.Structure Content: HTML is used to create the basic structure of web pages by defining elements like headings, paragraphs, links, images, and lists.",
        "8.Document Hierarchy: HTML establishes a clear hierarchy and organization of content, making it easier for browsers and users to navigate.",
        "9.Interactivity: HTML can integrate with scripts (like JavaScript) to create interactive web applications.",
        "10.Responsive Design: CSS enables responsive layouts that adapt to different screen sizes and devices, enhancing user experience.",
        "11.Separation of Concerns: By separating content (HTML) from presentation (CSS), it allows for cleaner code and easier maintenance.",
        
    ],
    "req":"""
        1.A basic text editor (like Notepad) or a code editor (like Visual Studio Code, Sublime Text, or Atom) to write and edit your HTML and CSS files.
         
    """,
           

    
    },
{

        "title": """
            Java Tutorial Full Course:Beginner to Pro
        """,
        "names": "Oke Stephen Tolu",
        "rating": 5.0,
        "price": 100000,
        "image": "vvypunv4.bmp",
        "link": "javascript",
     "goals": [
        "1.Fundamental Understanding: Teach the basic concepts of JavaScript, including variables, data types, functions, and control structures.",
        "2.DOM Manipulation: Introduce how to interact with the Document Object Model (DOM) to create dynamic web pages.",
        "3.Event Handling: Explain how to handle user events, such as clicks and keyboard input, to make applications more interactive.",
        "4.Asynchronous Programming: Cover concepts like callbacks, promises, and async/await to manage asynchronous operations.",
        "5.Object-Oriented Programming: Provide an understanding of objects, classes, and inheritance in JavaScript.",
        "6.Debugging Techniques: Teach how to troubleshoot and debug JavaScript code effectively."
        "7.Best Practices: Encourage writing clean, maintainable code and introduce common patterns and principles.",
        "8.Frameworks and Libraries: Briefly introduce popular frameworks like React, Vue, or Angular to show how JavaScript is used in modern web development.",
        "9.Project Development: Guide learners through building a small project to apply their skills practically..",
        "10.Resources for Further Learning: Offer suggestions for books, online courses, and documentation for continued learning.",
        "11.Code Readability: Emphasize the importance of writing readable code, including naming conventions and comments.."  
    ]
        
},  
    
{
        "title": """
            Learn Python - Full Course For Beginners [Tutorial]
        """,
        "names": "Oke Stephen Tolu",
        "image": "0j1grfnn.bmp",
        "rating": 4.8,
        "price": 100000,
        "link": "python",
       "goals": [
        "1.Fundamental Concepts: Introduce basic programming concepts such as variables, data types, and control structures (loops and conditionals).",
        "2.Data Structures: Explain Python’s built-in data structures, including lists, tuples, sets, and dictionaries, and their use cases.",
        "3: Functions and Modules: Teach how to define and call functions, as well as how to organize code using modules and packages.",
        "4.File Handling: Cover reading from and writing to files, including handling different file formats (text, CSV, JSON).", 
        "5.Error Handling: Introduce exception handling using try/except blocks to write robust code.",
        "6.Object-Oriented Programming (OOP): Explain OOP concepts such as classes, objects, inheritance, and polymorphism."
        "7.Libraries and Frameworks: Introduce popular libraries (like NumPy, Pandas, and Matplotlib) and frameworks (like Flask or Django) relevant to different domains.",
        "8.Data Analysis: Provide an overview of how to use Python for data analysis, including data manipulation and visualization.",
        "9.Testing and Debugging: Teach best practices for testing code, using frameworks like unittest or pytest, and effective debugging techniques.",
        "10.Asynchronous Programming: Explain concepts of asynchronous programming with async/await and how to handle concurrent tasks.",
        "11.APIs and Networking: Teach how to interact with APIs using the requests library, including handling JSON data."  
       ]     
        
},
{
        "title": """
            Learn Data Science Tutorial - Full Course For Beginners
        """,
        "names": "Ms bumzeal",
        "image": "oux6fdfs.bmp",
        "rating": 4.7,
        "price": 100000,
        "link": "data_science"
        
        
    },
       
{
        "title": """
           Web Development Complete Roadmap For Beginners
        """,
        "names": "Mentor Eri2oluwa , Mentor Samod",
        "image":"c0sfovyx.bmp ",
        "rating": 4.7,
        "price": 100000,
        "link": "web_dev"
        
        
    },
 
{
      "title": """
         100 concept of javascript you need to know - Full Course For Beginners [Tutorial]
        """,
        "names": "Oke stephen Tolu",
        "image":"wrv98evj.bmp",
        "rating": 4.9,
        "price": 100000,
        
        "link": "java"
        
    },
       
]
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("project.html")

@app.route('/courses')
def courses():
    return render_template("second .html", courses = allcourses)

@app.route('/website')
def website():
    return render_template("website.html")


@app.route('/courses/<courseid>')
def eachcourses(courseid):
    for course in allcourses:
        if course['link'] == courseid:
           return render_template("each.html", course = course)
           

if __name__ == "__main__":
    app.run(debug=True)
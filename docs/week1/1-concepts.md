# Core concepts

This is a repeat of content from the lecture. If you attended the lecture, you can skip this.

## HTTP request-response

Web applications provide dynamic content according to actions triggered by the user from a web
browser.

Python-driven web applications use Python code on a web server to determine what actions to take.

The communication between the browser and the server uses a protocol (a set of rules) called **HTTP
(Hypertext Transfer Protocol)**. HTTP is a protocol that dictates how web browsers (clients) request
and receive information, like webpages, images, and videos, from web servers, using a client-server
model for data exchange over the internet. It's a request-response protocol where a browser sends a
request for a resource, and the server sends back a response, forming the basis of most internet
communication.

In a Python web app:

- User makes a **request** for a web resource e.g. by typing a URL into a browser.
- This request gets received by the web server and passed to the app server.
- The app server matches the request to a portion of the app's Python code. Often called a 'route'.
- This Python code is called and when the code runs, it generates a **response** e.g. web page, JSON
  data.
- The app server delivers this response back to the user via the web server using the HTTP protocol.
- The user can then view the response by displaying it in a browser.

An HTTP request contains a start line, headers, and body:

- Start line: e.g. GET my-app/diary.html HTTP/1.0

    - HTTP Method e.g. GET, POST, DELETE, etc.
    - URL e.g. my-app/diary.html
    - HTTP version e.g. HTTP/1.0
- HTTP Headers: additional information to be passed to the server
- Body: GET requests do not usually have a body, POST request usually includes data in the body e.g. form data

An HTTP response contains a status line, headers, and body:

- Status line: e.g. HTTP/1.1 404 Not Found

    - Protocol version e.g. HTTP/1.1
    - Status code, e.g. 404 (not found)
    - Status text e.g. Not Found
- Headers: e.g. content type (e.g. text/html)
- Body: content

You can view examples of HTTP requests and responses in a browser:

- Find and open the developer tools/console window in your browser.
- Find the network section within this.
- Enter a URL in the browser, e.g. https://www.bbc.co.uk, and you should see the request and response
  details in the network section.

You can also view an example of an HTTP request for a REST API which has JSON data instead of HTML,
CSS, JavaScript, etc. Try https://catfact.ninja/fact

## Coursework application architecture

For the coursework you will create two web apps. In coursework 1 you will create a 'front end' app
that provides the pages that your intended users will interact with. In coursework 2 you will
replace the data access with a REST API, a web app that returns JSON structured data to the frontend
app.

The overall solution architecture looks like this:

![Application_architecture.png](../img/app_architecture.png)

## Technologies used to generate and display a web page

HTML provides the basic structure of a web page.

CSS provides the styling for the HTML elements on a web page.

JavaScript is used to create interactive or dynamic elements in a web page on the browser. Note: 
there is no JavaScript coding in this course, and JavaScript is not considered in marking.

The elements of the web page are constructed by the Python code on your web app server, which
returns the necessary files and content in an HTTP response.

### HTML

HTML (HyperText Markup Language) is a simple markup coding language used to layout content on a
webpage.

It consists of HTML tags, sometimes referred to as elements, that define the structure.

Most tags are in pairs at the start and end of an element, though there are a few exceptions that
are single tags.

The basic structure of an HTML page is:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello, world!</title>
</head>
<body>
<h1>Hello, world!</h1>
</body>
</html>
```

HTML documents start with a document type declaration.

The HTML document itself begins with `<html>` and ends with `</html>`.

The invisible part is between `<head>` and `</head>` and has meta-data, i.e. info about the page.

The visible part of the HTML document is between `<body>` and `</body>`.

Basic tag structure: `<start_tag>`some content`</end_tag>`, this is referred to as an element.

You don't need to learn all the HTML tags, use a reference such
as [Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference)
or [w3schools](https://www.w3schools.com/html/default.asp).

## CSS

CSS provides styles for HTML elements.

Web browsers apply CSS rules to an HTML document

A CSS rule consists of:

- A selector, which selects the element(s) you want to style
- A declaration which is a set of properties with values
- A set of CSS rules are contained within a stylesheet

```css
p {
    color: red;
}
```

If applied to the following HTML, the text would display as red.

```html
<p> A paragraph element.</p>
```

Style can be applied to all the occurrences of an HTML element, to all elements defined with a class,
or to an individual element on a page defined by an ID.

```css
/* Defines a style for all HTML H1 headings */
h1 {
    color: navy;
    margin-left: 20px;
}

/* Defines a style for applied to any HTML that includes this class in its definition. 
For example: <p class="myclass">Hello</p> 
*/
.myclass {
    background-color: lightblue;
}

/* Defines a style only for the HTML element that has this ID. 
IDs must be unique in an HTML document (web page). 
e.g. <p id='first-para'>Hello</p>
*/
#first-para {
    font-family: arial;
}
```

Multiple rules can be defined for an element, and there are 'rules' that determine which styles take
precedence. There are also places in which CSS styles can be defined. Defining styles can be
complex.

Writing your own CSS styles is not covered in the course. You will focus on using CSS written by a
third party that you will apply to your pages to style them.

## JavaScript

Programming language that enables you to dynamically update content, control multimedia, animate
images etc. on web pages.

JavaScript can interact with the web page content and change it in response to user actions.

When used on the clientside it runs in the browser after the page arrives and is displayed.

Some of the frameworks used in the course generate JavaScript based on your Python code (e.g. Plotly
Dash). Some of the CSS frameworks (e.g. Bootstrap) also use JavaScript. Your app therefore may
use JavaScript, but you will not write the JavaScript yourself.

While JavaScript is popular in the generation of web apps, this minor teaches Python and so the
writing and assessment and of JavaScript is not included in this module. If you write JavaScript in
the coursework, it will be ignored by the marker and will not contribute to the marks awarded.

## Document object model (DOM) and CSS Object Model (CSSOM)

The Document Object Model (DOM) connects web pages to scripts or programming languages. It is an
object-oriented representation of a web page (document) as a logical tree of elements.

CSS DOM is like the DOM, but for the CSS rather than the HTML.

DOM methods allow programmatic access to the tree to change the document's structure, style or
content.

The process for rendering a web page is:
![Render a web page from HTML and CSS](../img/render-doms.png)

This generates the DOM and the CSS DOM and combines them:
![DOM and CSS DOM > ](../img/doms.png)

_Author of the tree
diagram [Z Zhou](https://medium.com/@zhouzy/css-object-model-cssom-29d0a1951b5f)_

You can then target elements to modify them or their style. Strategies to locate elements in the
DOM include:

- Find elements by id
- Find elements by CSS class
- Find elements by HTML tag
- Find elements by navigating the tree

Finding elements by ID is the method often used in this module as the ID uniquely identifies
an element on a page.

## Python web app code

The web application provides the functionality that handles the incoming HTTP request, handles the
logic to generate a response, and returns an HTTP response

Python acts as the backend language that processes data and dynamically generates content e.g.:

- Generate a chart
- Process a form
- Generate a page with variable content

The server sends back an HTTP response, which could be:

- a web page (HTML, CSS, JavaScript)
- structured data (e.g. JSON from a REST API)

The web apps often use the concept of a 'route' that defines the available URLs for the app and
their associated Python functions.

For example, this is a route for a Flask web app that generates an HTML page with the words "Hello,
World!" If this app is run on localhost you would access it using `http://127.0.0.1:5000/hello`:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
```

## Python web application frameworks

Web application frameworks simplify and accelerate the process of building web-based applications.

They differ in their strengths and may be tailored to specific types of applications.

In this course you are only permitted to use Python web app frameworks, specifically:

- Plotly Dash (coursework 1): interactive data visualization dashboards
- Flask (coursework 1 and coursework 2): general purpose web applications
- Streamlit ((coursework 1)): data apps and machine learning dashboards
- FastAPI (coursework 2): RESTful APIs with automatic documentation

Note that JavaScript web application frameworks such as React must not be used in this module.

The remainder of this week's activities give you a basic example for each of the frameworks for
coursework 1 so that you can make a more informed choice which to use for your application.

## Localhost

You will not be deploying your app to a live web server. To do this requires infrastructure and
configuration not covered in the course. Instead, you will use features of the web application
frameworks to run the code on your own computer, which will behave as a web server referred to as 
'localhost'.

Localhost refers to the hostname that means "this computer" in networking. It is usually associated
with the IP address 127.0.0.1, which is the loopback address. When you access http://localhost in a
browser or use it in a program, you're telling the system to connect to a service running on your
own machine rather than over the internet.

Each app that you run on localhost needs to run on a port. Each of the web app frameworks defaults
to a different port e.g. Flask uses 5000, FastAPI uses 8000, Dash uses 8050, and Streamlit uses 8501.
You can change the default if you already have an app running on these ports.

[Next activity](2-basic-streamlit-app.md)
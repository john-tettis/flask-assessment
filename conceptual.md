### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript? 
 - Python is a language used to program server side logic and routing, javascript is used as a client side language for html dom manipulation and client side logic, as well as for requests to servers.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
 - dict.get('c') if(c in dict): dict.get('c')

- What is a unit test?
 - A unit test is a test meant to test the functionality of a single function in program

- What is an integration test?
 - an integration test is a test meant to test multiple functions in a program to make sure they work smoothly together

- What is the role of web application framework, like Flask?
  - Flask makes server side routing and logic much easier in python

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
	- using a route to pass information is more useful when the variable being passed defines an entire pages content or layout, while query params are more useful for lesser variables like sorting values, counters, search terms, etc

- How do you collect data from a URL placeholder parameter using Flask?
	- @app.route('/<type:var>') def function(var):

- How do you collect data from the query string using Flask?
	-call request.args['key'] or request.args.get('key') 

- How do you collect data from the body of the request using Flask?
	-request.data.get or request.data[]

- What is a cookie and what kinds of things are they commonly used for?
	- cookies are browser-stored data that is passed to the server on each request. They are commonly used for user-specific data that persists through page refreshes. Like username, cart id, or database id to retrieve info from a database, instead of storing it in the browser, for security/data-cap reasons

- What is the session object in Flask?
	- the session a=object is a way of passing and retrieving information into and out of cookies - it is encrypted as well.

- What does Flask's `jsonify()` do?
	- turns a complex data structure into a json response

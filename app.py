from chalice import Chalice, BadRequestError, NotFoundError

app = Chalice(app_name='helloworld')
app.debug = True

dict = {
    "pune":"Maharashtra",
    "surat":"Gujarat",
    "vizag":"AP"
}

obj = {
    "vizag":"AP"
}

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/square/{integer}')
def square(integer):
    integer = int(integer)
    return "Square of {int} is {square}".format(int=integer,square=integer ** 2)

@app.route('/city/{city}')
def state(city):
    city = city.lower()
    try:
        return "{city} city is in {state} state".format(city=city,state=dict[city])
    except KeyError:
        raise BadRequestError("Unknown city '%s', valid choices are: %s" % (
            city, ', '.join(dict.keys())))
    
@app.route('/obj/{key}', methods = ['GET', 'PUT'])
def myobj(key):
    request = app.current_request
    if request.method == 'PUT':
        obj[key] = request.json_body
        return request.to_dict()
    elif request.method == 'GET':
        try:
            return {key : obj[key]}
        except KeyError:
            raise NotFoundError(key)


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#

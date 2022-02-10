from werkzeug.wrappers import Request, Response


def application(env, start_response):
    request = Request(env)
    text = f"Hello, {request.args.get('name', 'World')}!"
    response = Response(text, mimetype='text/plain')
    return response(env, start_response)
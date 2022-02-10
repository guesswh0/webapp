from werkzeug.wrappers import Response


def application(env, start_response):
    response = Response('Hello, World!', mimetype='text/plain')
    return response(env, start_response)

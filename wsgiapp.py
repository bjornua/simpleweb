# -*- coding: utf-8 -*-
import env
import werkzeug
import app

def getwsgihandler(debug):
    appdispatch = app.getdispatcher(debug)

    def dispatch(environ, start_response):
        request = werkzeug.Request(environ)
        response = appdispatch(request)
        return response(environ, start_response)
    
    def safedispatch(environ, start_response):
        try:
            return dispatch(environ, start_response)
        except:
            if debug:
                raise
            else:
                response = werkzeug.Response("Error")
                return response(environ, start_response)

    # Wrap dispatcher with static file server
    dispatch = werkzeug.SharedDataMiddleware(dispatch, {"/static": "static"})
    
    return safedispatch

def main():
    wsgihandler = getwsgihandler(debug=True)
    bind_address = "127.0.0.1"
    port = 5000
    werkzeug.run_simple(
        bind_address, port, wsgihandler, use_debugger=True, use_reloader=True
    )

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
import werkzeug

def getdispatcher(debug=False):
    def dispatch(request):
        return werkzeug.Response("Derping")

    return dispatch

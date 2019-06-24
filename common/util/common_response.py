from flask import jsonify


def response(message, data=None, status=200):
    response_obj = {
        "message": message,
        "status": status
    }
    if data is not None:
        response_obj['data'] = data
    return jsonify(response_obj), status


def cookie_response(message, cookie_name, cookie_value, expires="100", data=None,
                    status=200):
    c_response_tuple = response(message=message, data=data, status=status)
    c_response_tuple[0].set_cookie(cookie_name, cookie_value)
    return c_response_tuple

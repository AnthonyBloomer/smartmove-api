from flask import request, jsonify


def paginate():
    page = 0
    per_page = 25
    params = []
    if request.args.get('page'):
        page = request.args.get('page')
    start_at = int(page) * per_page
    params.append(start_at)
    params.append(per_page)
    return params

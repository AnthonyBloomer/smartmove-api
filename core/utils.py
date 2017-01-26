from flask import request, jsonify


def paginate():
    page = 0
    per_page = 25
    params = []
    if request.args.get('page'):
        page = request.args.get('page')
    try:
        start_at = int(page) * per_page
    except ValueError:
        return jsonify({'Error Code': '500', 'Message': 'Value error: Page requires int.'})
    params.append(start_at)
    params.append(per_page)
    return params

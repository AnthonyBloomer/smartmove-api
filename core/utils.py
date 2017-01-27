from flask import request
import gviz_api
import json


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


def gviz_json(columns_order, order_by, desc, data):
    data = [tuple(data.values()) for data in data]
    data_table = gviz_api.DataTable(desc)
    data_table.LoadData(data)
    json_str = data_table.ToJSon(columns_order=columns_order, order_by=order_by)
    parsed_json = json.loads(json_str)
    return parsed_json

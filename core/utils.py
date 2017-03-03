from flask import request
from gvizapi import gviz_api
import json
from .connection import conn


def paginate(page=0, per_page=25):
    page = page
    per_page = per_page
    params = []
    if request.args.get('page'):
        page = request.args.get('page')
    start_at = int(page) * per_page
    params.append(start_at)
    params.append(per_page)
    return params


def gviz_json(desc, data, columns_order=None, order_by=None):
    data = [tuple(d.values()) for d in data]
    data_table = gviz_api.DataTable(desc)
    data_table.LoadData(data)
    json_str = data_table.ToJSon(columns_order=columns_order, order_by=order_by)
    parsed_json = json.loads(json_str)
    return parsed_json


def validate_key(api_key):
    with conn.cursor() as cursor:
        sql = ""
        cursor.execute(sql, api_key)
        result = cursor.fetchone()
        if result:
            return True

from src.get_data import read_params
import pandas as pd
import joblib
import json
import os


class ColumnNotFound(Exception):
    def __init__(self, message="column not found"):
        self.message = message
        super().__init__(self.message)


class NotInRange(Exception):
    def __init__(self, message="Values are not in range"):
        self.message = message
        super().__init__(self.message)


class MissingColumns(Exception):
    def __init__(self, message="Some columns are missing"):
        self.message = message
        super().__init__(self.message)


def predict(data):
    params = read_params("params.yaml")
    model_dir_path = params["webapp_model_dir"]
    data = pd.DataFrame(data, index=[0])
    model = joblib.load(model_dir_path)
    out = model.predict(data)[0]
    try:
        if 3 <= out <= 8:
            return out
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected result"


def get_schema(schema_path=os.path.join("notebooks","schema.json")):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema


def validation(data):
    def _column_validation(col):
        schema = get_schema()
        if col not in list(schema.keys()):
            raise ColumnNotFound

    def _column_missing_check(data=data):
        schema = get_schema()
        for i in schema.keys():
            if i not in data.keys():
                raise MissingColumns

    for col in data.keys():
        _column_validation(col)

    _column_missing_check()
    return True


def api_response(data):
    try:
        if validation(data):
            response = predict(data)
            return response
    except ColumnNotFound as e:
        response = {
            "the_exected_cols": ",".join(list(get_schema().keys())),
            "response": str(e),
        }
        return response
    except MissingColumns as e:
        response = {
            "the_exected_cols": ",".join(list(get_schema().keys())),
            "response": str(e),
        }
        return response

from flask import Flask, request, jsonify, Blueprint
from app.utils import get_minimum, get_maximum, calc_average, calc_percentile, get_median
from app.invalid_usage import InvalidUsage
from app.validate import InputsValidator, validate_input

api = Blueprint('api', __name__, url_prefix='/api/v1')


def create_app(config='dev'):
    app = Flask(__name__)
    app.register_blueprint(api)
    return app

@api.route('/')
def index():
    return jsonify({"message": "Sojern Math library"})


def request_args():
    """Get args from request"""
    print(request.json)
    data = request.json
    return data.get("values"), data.get("quantifier")


@api.post('/min')
def minimum():
    if not is_valid_request():
        return jsonify(status="error", message="Please send a valid request"), 400

    values, quantifier = request_args()
    if quantifier >= len(values):
        result = values
    else:
        result = get_minimum(values, quantifier)

    return jsonify(status="success", min=result), 200


@api.post('/max')
def maximum():
    if not is_valid_request():
        return jsonify(status="error", message="Please send a valid request"), 400

    errors = validate_input(request, True)

    if errors is not None:
        raise InvalidUsage(errors)

    values, quantifier = request_args()
    if quantifier >= len(values):
        result = values
    else:
        result = get_maximum(values, quantifier)

    return jsonify(status="success", max=result), 200


@api.post('/average')
def average():
    if not is_valid_request():
        return jsonify(status="error", message="Please send a valid request"), 400

    errors = validate_input(request, False)
    if errors is not None:
        raise InvalidUsage(errors)

    values = request.json.get("values")
    avg = calc_average(values)

    return jsonify(status="success", average=avg), 200


@api.post('/percentile')
def percentile():
    values, quantifier = request_args()
    errors = validate_input(request, True)
    if errors is not None:
        raise InvalidUsage(errors)

    if not is_valid_request():
        return jsonify(status="error", message="Please send a valid request"), 400

    if quantifier > 100 or quantifier <= 0:
        return jsonify(status="error", message="Percentile quantifier needs to be in the range of <= 100 or > 0"), 400

    _percentile = calc_percentile(values, quantifier)
    return jsonify(status="success", percentile=_percentile), 200


@api.post('/median')
def median():
    if not is_valid_request():
        return jsonify(status="error", message="Please send a valid request"), 400

    errors = validate_input(request, False)
    if errors is not None:
        raise InvalidUsage(errors)

    values = request.json.get("values")
    median = get_median(values)
    return jsonify(status="success", median=median), 200


def is_valid_request():
    header = request.headers['Content-Type']
    is_json = request.is_json

    if header == 'application/json' and is_json:
        return True

    return False


@api.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app = create_app("Production")
    app.run(host='0.0.0.0')

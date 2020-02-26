import json
import numpy
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    dimension: int = None
    if req.params.get("dimension"):
        dimension = int(req.params["dimension"])

    if dimension is None:
        return func.HttpResponse(body="Pass ?dimension=1 query param", mimetype="text/plain")

    array = numpy.random.rand(dimension, dimension)
    result = {
        "shape": str(array.shape),
        "dtype": str(array.dtype),
        "name": "Num",
        "result": str(array)
    }

    return func.HttpResponse(body=json.dumps(result), mimetype="application/json")

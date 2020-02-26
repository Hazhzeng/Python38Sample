import logging

import azure.functions as func
import dataclasses

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if (name := req.params.get('name')) is not None:
        return func.HttpResponse(f"38 Hello {name}!")
    else:
        return func.HttpResponse(
             "38 Please pass a name on the query string or in the request body",
             status_code=400
        )

import logging

import azure.functions as func
import dataclasses

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"37 Hello {name}!")
    else:
        return func.HttpResponse(
             "37 Please pass a name on the query string or in the request body",
             status_code=400
        )

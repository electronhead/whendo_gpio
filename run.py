"""
This script runs the api server with optionally supplied host and port.
"""
import argparse
import uvicorn

"""
in this section import the alfalfa modules that define additional Actions.
These should be imported before importing whendo.api.main
"""
import whendo_gpio.imports

"""
import the main script that creates the FastAPI instance (main.app).
"""
from whendo.api import main

"""
parse command line arguments
"""
parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, default="127.0.0.1", dest="host")
parser.add_argument("--port", type=int, default=8000, dest="port")
parser.add_argument("--workers", type=int, default=1, dest="workers")
args = parser.parse_args()

"""
initialize shared server information
"""
import whendo.core.util as util
util.SystemInfo.init(host=args.host, port=args.port)

"""
uvicorn is the ASGI server that runs the api specified with FastAPI.
"""
uvicorn.run(main.app, host=args.host, port=args.port, workers=args.workers)

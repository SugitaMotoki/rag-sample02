import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ".."))

from tests.interfaces.provider_classes import PythonProvider

provider = PythonProvider()
call_api = provider.get_call_api()

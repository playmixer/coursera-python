import json
from functools import wraps

def to_json(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		return json.dumps(func(*args, **kwargs))
	return wrapper


@to_json
def get_data():
	return {'a':42}


if __name__ == "__main__":
	print(get_data())
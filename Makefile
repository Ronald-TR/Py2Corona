setup:
		pip install pipenv
		pipenv install --three
		pipenv install --dev
		
test:
		python tests/testcase.py
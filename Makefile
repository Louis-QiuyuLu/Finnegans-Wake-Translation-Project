.PHONY: check test generate build serve

check:
	python3 scripts/project.py check

test:
	python3 -m unittest discover -s tests -v
	node --test tests/test_reader_model.cjs

generate:
	python3 scripts/project.py generate

build:
	python3 scripts/project.py build

serve: build
	python3 -m http.server 8000 --directory dist/site --bind 127.0.0.1

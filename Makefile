lint:
    pylint app

test:
    pytest tests
	
all: lint test
.PHONY: lint test all
.PHONY: lint format generate clean

lint:
	@echo "Linting proto files..."
	buf lint

format:
	@echo "Formatting proto files..."
	buf format -w

generate: lint
	@echo "Generating code with buf..."
	@mkdir -p generated/go generated/python
	buf generate
	@echo "Code generation complete!"

clean:
	@echo "Cleaning generated files..."
	rm -rf generated/go/* generated/python/*
	@echo "Clean complete!"

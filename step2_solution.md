# Solution
In order to use `buf`, we first need to [install](https://buf.build/docs/cli/installation/) it.
After installing, I recommend going through the [introduction page](https://buf.build/docs/cli/) of their CLI to better understand what features are available and what problem they solve.
## Workspace Configuration
We need to create a `buf.yaml` for `buf` to know how to interact with our project. A very simple file that works for our project would look something like this:
```
version: v2
modules:
  - path: proto
lint:
  use:
    - STANDARD
breaking:
  use:
    - FILE
```
- `version: v2` means we're using the latest `buf` configuration format. There's also `v1` and there are some incompatibilities between both versions, so sticking to newer versions for newer projects is better.
- `modules: - path: proto` tells `buf` where to find our proto files. By default this would be the project root so we need to specify it.
- `lint: use: - STANDARD` enables `buf`'s recommended linting rules for proto files. Here we could add additional linting rules, ignore files or rules, etc.
- `breaking: use: - FILE` enables breaking change detection between proto versions.
- There are several other configuration options available for the `buf.yaml` file. They are all properly documented [here](https://buf.build/docs/configuration/v2/buf-yaml/).

After installing `buf` and adding the `buf.yaml` file, we should be able to run the following commands:
```
buf lint
buf format -w
```
## Generation Configuration
For `buf` to generate stubs for us, we need to define a separate file - `buf.gen.yaml`. This file tells `buf` how and where to generate the stubs for us.
```
version: v2
clean: true
inputs:
  - directory: proto
plugins:
  # Go plugins
  - remote: buf.build/protocolbuffers/go
    out: generated/go
    opt:
      - paths=source_relative
  - remote: buf.build/grpc/go
    out: generated/go
    opt:
      - paths=source_relative
  # Python plugins
  - remote: buf.build/protocolbuffers/python
    out: generated/python
  - remote: buf.build/protocolbuffers/pyi
    out: generated/python
```
- `version: v2` - again, using v2 instead of v1 for more features.
- `clean: true` cleans the output directories before generating, ensuring we generate fresh files every time.
- `plugins` tells `buf` exactly what tools to use to generate our code. These tools can be `local`, which means we have local installations of the tools (like we did in previous steps) or remote, which enables us to generate files without locally installing them. We also need to specify the output directory for each of these tools and any additional options we need.
- As with the `buf.yaml` file, there are several more configurations available to us, thoroughly documented [here](https://buf.build/docs/configuration/v2/buf-gen-yaml/).
Once we have defined the `buf.gen.yaml` file, we should be able to run the `buf generate` command without issues!
## Makefile
Just for simplicity, we could create a `Makefile` where we define all of the important commands in our project.
```
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
```
Specifically, having a command that both lints and generates the code is very useful to simplify our workflow.
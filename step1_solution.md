# Solution
The first step to work effectively with proto files is to install the protocol buffer compiler:
- https://grpc.io/docs/protoc-installation/
- https://protobuf.dev/installation/
## Python
To start, we need to install some dependencies into our Python environment
```
grpcio
grpcio-tools
protobuf
```
Once all of those are installed, the command to build out stub files is the following:
```
$ python -m grpc_tools.protoc \
    --proto_path=proto \
    --python_out=generated/python \
    --grpc_python_out=generated/python \
    proto/coffeeshop.proto
```
Here's a breakdown of that command
- `python -m grpc_tools.protoc` means we're invoking the `protoc` functionality of the `grpc_tools` package
- `--proto_path=proto` tells protoc where to look for proto files. Especially important if we have dependencies within the proto files we're generating code for
- `--python_out=generated/python` tells protoc the path where we want to generate the code for our messages (or structures)
- `--grpc_python_out=generated/python` tells protoc the path where we want to generate the code for our services
- `proto/coffeeshop.proto` is the argument to the command, specifying which file we want to generate stubs for. We could pass several files here

This will generate two files in `generated/python/`
- `coffeeshop_pb2.py` - Message classes (DrinkItem, AddDrinkRequest, etc.)
- `coffeeshop_pb2_grpc.py` - Service classes (server/client interfaces)

To encapsulate this into a script, we could first add our dependencies to a `requirements.txt` file, and then a script to call this command.

## Go
Again, we start by installing some dependencies
```
$ go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
$ go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```
After that, we should be able to run a very similar command to the Python to generate our code
```
protoc \
    --proto_path=proto \
    --go_out=generated/go \
    --go_opt=paths=source_relative \
    --go-grpc_out=generated/go \
    --go-grpc_opt=paths=source_relative \
    proto/coffeeshop.proto
```
Here's a breakdown of that command
- `protoc` means we're invoking the `protoc` functionality of the `grpc_tools` package
- `--proto_path=proto` tells protoc where to look for proto files. Especially important if we have dependencies within the proto files we're generating code for
- `--go_out=generated/go` tells protoc the path where we want to generate the code for our messages (or structures)
- `--go_opt=paths=source_relative` tells protoc to generate simple Go files that will be imported with relative paths. The alternative would be using a module which would mean generated code is better encapsulated but more complicated to import
- `--go-grpc_out=generated/go` tells protoc the path where we want to generate the code for our services
- `--go-grpc_opt=paths=source_relative` sames as previous paths option
- `proto/coffeeshop.proto` is the argument to the command, specifying which file we want to generate stubs for. We could pass several files here

This will generate two files in `generated/go/`
- `coffeeshop.pb.go` - Message classes (DrinkItem, AddDrinkRequest, etc.)
- `coffeeshop_grpc.pb.go` - Service classes (server/client interfaces)

If we look into the generated files, there will be some dependencies that we don't have locally. In order to solve this, we should initialize our project as a Go module and run the `go mod tidy` command to fetch those dependencies.
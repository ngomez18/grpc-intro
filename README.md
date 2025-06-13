# Coffee Shop gRPC

## Step 1
### Proto definition
In the `proto/coffeeshop.proto` file you will find definitions for our Coffee Shop service.

This service currently implements only an rpc to create a new menu item, and an rpc to fetch the menu. Each of those rpcs defines the necessary inputs and outputs for the procedure to work

### Stub generation
One of the advantages of gRPC is the code generation tools available to generate stubs for our services, which prevents a lot of boilerplate code.
There are several different tools available to generate this stubs, supporting many different languages. For this exercise, we will try to create equivalent gRPC servers and clients using both Go and Python.

For Python see:
- https://grpc.io/docs/languages/python/quickstart/#generate-grpc-code
- https://grpc.io/docs/languages/python/generated-code/

For Go see:
- https://grpc.io/docs/languages/go/quickstart/

### Expected output
After being able to generate the code via command line, you should be able to create scripts as such:
- `scripts/generate_python_stubs.sh`
- `scripts/generate_go_stubs.sh`

And the generated directory should have the following structure
```
grpc-intro/
├── proto/
│   └── coffeeshop.proto
├── generated/
│   ├── python/
│   │   ├── __init__.py
│   │   ├── coffeeshop_pb2.py
│   │   └── coffeeshop_pb2_grpc.py
│   └── go/
│       ├── coffeeshop.pb.go
│       └── coffeeshop_grpc.pb.go
└── scripts/
    ├── requirements.txt
    ├── generate_python.sh
    └── generate_go.sh
```
Feel free to add any additional files you need for your scripts to work (Python requirements file, Go module file, etc).


### Solution
#### Python
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

To encapsulate this into a script, we could first add our dependencies to a `requirements.txt` file inside the `scripts` dir, and then a script to call this command.
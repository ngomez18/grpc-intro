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
- `scripts/generate_pytho.sh`
- `scripts/generate_go.sh`

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
    ├── generate_python.sh
    └── generate_go.sh
```
Feel free to add any additional files you need for your scripts to work (Python requirements file, Go module file, etc).

#!/bin/bash

PROTO_PATH="proto"
OUTPUT_PATH="generated/go"
PROTO_FILES=("coffeeshop.proto")

echo "Generating Go gRPC stubs..."
echo "Proto path: $PROTO_PATH"
echo "Output path: $OUTPUT_PATH"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_PATH"

# Build the full paths by adding proto_path prefix
FULL_PROTO_PATHS=()
for file in "${PROTO_FILES[@]}"; do
    FULL_PROTO_PATHS+=("$PROTO_PATH/$file")
done

echo "Proto files: ${FULL_PROTO_PATHS[*]}"

protoc \
    --proto_path="$PROTO_PATH" \
    --go_out="$OUTPUT_PATH" \
    --go_opt=paths=source_relative \
    --go-grpc_out="$OUTPUT_PATH" \
    --go-grpc_opt=paths=source_relative \
    "${FULL_PROTO_PATHS[@]}"

if [ $? -eq 0 ]; then
    echo "Go stubs generated successfully!"
    echo "Generated files:"
    tree "$OUTPUT_PATH"
else
    echo "Error generating Go stubs"
    exit 1
fi

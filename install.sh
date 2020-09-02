#!/bin/bash

## Build the plugins
if [ ! -d grpc-swift ]; then
        git clone -b main https://github.com/grpc/grpc-swift.git
        cd grpc-swift
        make plugins
        cp protoc-gen-grpc-swift* ../
        cp protoc-gen-swift* ../
        cd ../
else
        cp ./grpc-swift/protoc-gen-grpc-swift* .
        cp ./grpc-swift/protoc-gen-swift* .
        cd ../
fi

## Generate your Swift code from proto files
# Add the path in your PATH
export PATH=:$pwd:$PATH
protoc *.proto --swift_out=. --grpc-swift_out=.

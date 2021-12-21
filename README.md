# calculator-grpc

## to install

* python and pip are supposed to be installed

* cd calculator-grpc

* pip install grpcio

* pip install grpcio-tools

* python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

* python server.py

* python client.py

## documentation
proto3: https://developers.google.com/protocol-buffers/docs/proto3

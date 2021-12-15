# calculator-grpc for Python

## to install
git clone https://github.com/oceane-sailorin/calculator-grpc
cd calculator-grpc
pip install grpcio
pip install grpcio-tools
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
python server.py
python client.py

## documentation
proto3: https://developers.google.com/protocol-buffers/docs/proto3

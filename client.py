# client

# import grpc
import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc


# creating a stub

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create client
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create request message
som = calculator_pb2.List1(number1=4,number2=3)

# make the call
response = stub.Sum(som)

# print the response
print(response.value)

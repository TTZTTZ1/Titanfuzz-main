import torch

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply Sigmoid activation
sigmoid = torch.nn.Sigmoid()
output_tensor = sigmoid(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after Sigmoid Activation:")
print(output_tensor)
import torch

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the Sigmoid function
sigmoid = torch.nn.Sigmoid()
output_tensor = sigmoid(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
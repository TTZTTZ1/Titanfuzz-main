import torch

# Create a tensor with random values
input_tensor = torch.randn(3)

# Apply the Sigmoid function
sigmoid_function = torch.nn.Sigmoid()
output_tensor = sigmoid_function(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after applying Sigmoid:", output_tensor)
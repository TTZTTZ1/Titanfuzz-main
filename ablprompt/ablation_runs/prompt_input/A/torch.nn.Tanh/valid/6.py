import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 3)

# Apply the Tanh function from torch.nn
tanh_function = torch.nn.Tanh()
output_tensor = tanh_function(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after applying Tanh:")
print(output_tensor)
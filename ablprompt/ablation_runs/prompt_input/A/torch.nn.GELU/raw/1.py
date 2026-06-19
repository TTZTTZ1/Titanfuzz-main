import torch

# Create a tensor of random values
input_tensor = torch.randn(3, 3)

# Apply GELU activation function
gelu_output = torch.nn.functional.gelu(input_tensor)

print(gelu_output)
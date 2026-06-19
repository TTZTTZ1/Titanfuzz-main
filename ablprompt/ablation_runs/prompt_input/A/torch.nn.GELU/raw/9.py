import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 4)

# Apply GELU activation function
gelu_output = torch.nn.functional.gelu(input_tensor)

print(gelu_output)
import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 3)

# Apply the tanh function to the tensor
output_tensor = torch.tanh(input_tensor)

print(output_tensor)
import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply softmax along dimension 1
softmax_output = torch.nn.functional.softmax(input_tensor, dim=1)

print(softmax_output)
import torch

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply log_softmax along dimension 1
output_tensor = torch.nn.functional.log_softmax(input_tensor, dim=1)

print(output_tensor)
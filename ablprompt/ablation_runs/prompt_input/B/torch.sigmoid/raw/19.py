import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply sigmoid function
output_tensor = torch.sigmoid(input_tensor)

print(output_tensor)
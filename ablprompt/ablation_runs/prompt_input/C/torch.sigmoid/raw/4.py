import torch

# Create a random tensor as input
input_tensor = torch.randn(3, 4)

# Apply the sigmoid function
output_tensor = torch.sigmoid(input_tensor)

print(output_tensor)
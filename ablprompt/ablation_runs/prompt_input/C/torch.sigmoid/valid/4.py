import torch

# Create a random tensor with float values
input_tensor = torch.randn(3, 4)

# Apply the sigmoid function to the input tensor
output_tensor = torch.sigmoid(input_tensor)

print(output_tensor)
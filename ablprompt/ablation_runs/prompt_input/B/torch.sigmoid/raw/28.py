import torch

# Create a random tensor with values ranging from -5 to 5
input_tensor = torch.randn(3, 4) * 10

# Apply the sigmoid function
output_tensor = torch.sigmoid(input_tensor)

print(output_tensor)
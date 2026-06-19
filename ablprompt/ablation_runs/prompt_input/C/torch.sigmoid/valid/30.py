import torch

# Create a random tensor with values between -5 and 5
input_tensor = torch.randn(3, 4) * 10

# Apply sigmoid activation function
output_tensor = torch.sigmoid(input_tensor)

print(output_tensor)
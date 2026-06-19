import torch

# Create a random tensor with values between -5 and 5
input_tensor = torch.rand(3, 4) * 10 - 5

# Apply the sigmoid function
output_tensor = torch.sigmoid(input_tensor)

print(output_tensor)
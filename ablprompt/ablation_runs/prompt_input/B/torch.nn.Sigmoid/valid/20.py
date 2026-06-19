import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply Sigmoid activation
sigmoid = torch.nn.Sigmoid()
output_tensor = sigmoid(input_tensor)

print(output_tensor)
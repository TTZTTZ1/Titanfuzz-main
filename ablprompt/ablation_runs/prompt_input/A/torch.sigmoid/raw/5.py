import torch

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply sigmoid function
output_tensor = torch.sigmoid(input_tensor)

print(output_tensor)
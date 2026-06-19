import torch

# Create a tensor with some values
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the sigmoid function
output_tensor = torch.sigmoid(input_tensor)

print(output_tensor)
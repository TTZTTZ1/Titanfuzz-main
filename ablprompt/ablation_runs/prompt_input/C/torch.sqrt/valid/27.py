import torch

# Create a tensor with both positive and negative values
input_tensor = torch.tensor([-4.0, -1.0, 0.0, 1.0, 4.0], dtype=torch.float32)

# Compute the element-wise square root
output_tensor = torch.sqrt(input_tensor)

print(output_tensor)
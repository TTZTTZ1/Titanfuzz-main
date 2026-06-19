import torch

# Create a random tensor with negative and positive values
input_tensor = torch.tensor([-4.0, -1.0, 0.0, 1.0, 4.0], dtype=torch.float32)

# Compute the element-wise square root
result_tensor = torch.sqrt(input_tensor)

print(result_tensor)
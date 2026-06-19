import torch

# Create a tensor
x = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)

# Call the tan function from torch
result = torch.tan(x)

print(result)
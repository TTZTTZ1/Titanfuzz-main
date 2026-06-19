import torch

# Create a tensor
x = torch.tensor([0.0, 1.5708, -1.5708], dtype=torch.float32)

# Call the tan function
result = torch.tan(x)

print(result)
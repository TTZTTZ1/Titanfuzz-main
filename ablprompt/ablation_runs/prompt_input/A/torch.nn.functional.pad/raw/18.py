import torch
import torch.nn.functional as F

# Create a tensor
tensor = torch.randn(2, 3)

# Pad the tensor
padded_tensor = F.pad(tensor, (1, 1, 2, 2), "constant", value=0)

print(padded_tensor)
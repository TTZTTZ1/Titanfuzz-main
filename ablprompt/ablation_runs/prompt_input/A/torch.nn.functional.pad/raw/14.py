import torch
import torch.nn.functional as F

# Create a tensor to pad
input_tensor = torch.randn(1, 3, 224, 224)

# Define padding parameters
padding = (10, 10, 5, 5)  # (left, right, top, bottom)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, padding, "constant", value=0)

print(padded_tensor.shape)
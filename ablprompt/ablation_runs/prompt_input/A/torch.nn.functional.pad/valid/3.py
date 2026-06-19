import torch
import torch.nn.functional as F

# Create a sample tensor
input_tensor = torch.randn(2, 3)

# Define padding values (pad before/after each dimension)
padding = (1, 1)  # Padding for each dimension: (left, right, top, bottom)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, padding, "constant", value=0)

print("Original Tensor:", input_tensor)
print("Padded Tensor:", padded_tensor)
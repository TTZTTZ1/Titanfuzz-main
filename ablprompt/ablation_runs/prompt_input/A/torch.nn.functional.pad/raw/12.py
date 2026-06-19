import torch
import torch.nn.functional as F

# Create a tensor
input_tensor = torch.randn(3, 4)

# Define padding
pad = (1, 2, 0, 1)  # Padding for each side: (left, right, top, bottom)

# Apply padding using torch.nn.functional.pad
padded_tensor = F.pad(input_tensor, pad, "constant", value=0)

print("Original Tensor:")
print(input_tensor)
print("Padded Tensor:")
print(padded_tensor)
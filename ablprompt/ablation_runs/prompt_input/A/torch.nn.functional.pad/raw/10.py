import torch
import torch.nn.functional as F

# Example tensor to pad
input_tensor = torch.randn(1, 3, 5, 5)

# Define padding parameters
padding = (2, 2, 2, 2)  # Padding of 2 on each side in height and width dimensions

# Call the pad function
padded_tensor = F.pad(input_tensor, padding, "constant", 0)

print(padded_tensor.shape)
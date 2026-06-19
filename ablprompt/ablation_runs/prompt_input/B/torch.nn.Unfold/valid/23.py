import torch
from torch.nn import Unfold

# Example input tensor
input_tensor = torch.randn(1, 1, 5, 5)

# Create an instance of Unfold
unfold = Unfold(kernel_size=3, stride=1, padding=1)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)
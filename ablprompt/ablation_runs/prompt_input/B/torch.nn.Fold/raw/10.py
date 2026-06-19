import torch
from torch.nn import Fold

# Define the input tensor
input_tensor = torch.randn(1, 16, 8)

# Define the Fold layer
fold_layer = Fold(output_size=(16, 16), kernel_size=4, stride=2, padding=1, dilation=1)

# Apply the Fold layer
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)
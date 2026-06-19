import torch
from torch.nn import Unfold

# Example usage of torch.nn.Unfold
input_tensor = torch.randn(1, 3, 8, 8)
unfold = Unfold(kernel_size=3, stride=2, padding=1)
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 9, 25])
import torch
from torch.nn import Unfold

# Example input tensor (batch_size=1, channels=1, height=4, width=4)
input_tensor = torch.randn(1, 1, 4, 4)

# Create an instance of Unfold
unfold = Unfold(kernel_size=(2, 2), stride=(1, 1), padding=(0, 0))

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 4, 9])
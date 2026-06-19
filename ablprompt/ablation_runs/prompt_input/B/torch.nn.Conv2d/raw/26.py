import torch
from torch.nn import Conv2d

# Example usage of torch.nn.Conv2d
input_tensor = torch.randn(1, 3, 32, 32)
conv_layer = Conv2d(in_channels=3, out_channels=64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
output_tensor = conv_layer(input_tensor)
print(output_tensor.shape)
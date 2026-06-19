import torch
from torch import nn

# Define the TransformerEncoderLayer
encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8)

# Create a random input tensor
src = torch.rand(10, 32, 512)  # (sequence length, batch size, feature size)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)
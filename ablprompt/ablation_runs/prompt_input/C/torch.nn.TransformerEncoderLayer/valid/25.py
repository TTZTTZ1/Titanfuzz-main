import torch
from torch.nn import TransformerEncoderLayer

# Define the dimensions
d_model = 512
nhead = 8

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead)

# Generate random input tensor
src = torch.rand(10, 32, 512)  # (seq_len, batch, features)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
import torch
import torch.nn as nn

# Define the dimensions
d_model = 512
nhead = 8

# Create an instance of TransformerEncoderLayer
encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead)

# Generate random input tensor
src = torch.randn(10, 32, d_model)  # (seq_len, batch, features)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
import torch
from torch.nn import TransformerEncoderLayer

# Define a sample input tensor
src = torch.rand(10, 32, 512)  # (sequence length, batch size, embedding dimension)

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=512, nhead=8)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Expected output shape: (sequence length, batch size, embedding dimension)
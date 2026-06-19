import torch
from torch.nn import TransformerEncoderLayer

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=512, nhead=8)

# Prepare input tensor
src = torch.randn(10, 32, 512)  # (seq_len, batch, features)

# Apply the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should be (10, 32, 512)
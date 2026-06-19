import torch
from torch.nn import TransformerEncoderLayer

# Define the model parameters
d_model = 512
nhead = 8

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead)

# Prepare the input tensor
src = torch.randn(10, 32, d_model)  # (seq_len, batch, features)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Output should be (seq_len, batch, d_model)
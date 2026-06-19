import torch
from torch.nn import TransformerEncoderLayer

# Define the dimensions for the input and output
d_model = 512
nhead = 8

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model, nhead)

# Generate a random input tensor
src = torch.rand(10, 32, d_model)  # (sequence length, batch size, feature number)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)
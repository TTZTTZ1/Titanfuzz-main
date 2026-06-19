import torch
from torch.nn import TransformerEncoderLayer

# Define the dimensions for the input tensor and the model
d_model = 512
nhead = 8

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model, nhead)

# Generate a random input tensor
src = torch.rand(10, 32, d_model)  # seq_len x batch_size x d_model

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)
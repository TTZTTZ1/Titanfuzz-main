import torch
from torch import nn

# Define the model parameters
d_model = 512
nhead = 8
num_layers = 6

# Create an instance of TransformerEncoderLayer
encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead)

# Create a stack of TransformerEncoderLayers
transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

# Generate random input data
src = torch.rand(10, 32, 512)  # (seq_len, batch, features)

# Pass the input through the transformer encoder
output = transformer_encoder(src)

print(output.shape)  # Output should be (seq_len, batch, d_model)
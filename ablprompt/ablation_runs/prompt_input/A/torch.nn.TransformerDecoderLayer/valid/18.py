import torch
from torch.nn import TransformerDecoderLayer

# Define the dimensions
d_model = 512
nhead = 8

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead)

# Dummy input tensors
tgt = torch.rand(10, 32, d_model)  # Target sequence
memory = torch.rand(20, 32, d_model)  # Memory sequence

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)
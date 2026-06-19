import torch
from torch.nn import TransformerDecoderLayer

# Define the dimensions for the transformer decoder layer
d_model = 512
nhead = 8

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead)

# Dummy input tensors
tgt = torch.randn(10, 32, d_model)  # Target sequence of length 10, batch size 32, feature size 512
memory = torch.randn(20, 32, d_model)  # Memory sequence of length 20, batch size 32, feature size 512

# Perform a forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
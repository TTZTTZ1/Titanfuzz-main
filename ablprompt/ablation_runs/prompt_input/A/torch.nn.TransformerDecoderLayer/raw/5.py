import torch
from torch.nn import TransformerDecoderLayer

# Define some example input tensors
d_model = 512
nhead = 8
src = torch.rand(10, 32, d_model)
tgt = torch.rand(20, 32, d_model)

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Perform a forward pass through the decoder layer
output = decoder_layer(tgt, src)

print(output.shape)  # Should print: torch.Size([20, 32, 512])
import torch
from torch.nn import TransformerDecoderLayer

# Define some input tensors
d_model = 512
nhead = 8
src = torch.rand(32, 10, d_model)
tgt = torch.rand(32, 10, d_model)

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead)

# Perform a forward pass
output = decoder_layer(tgt, src)

print(output.shape)  # Should print: torch.Size([32, 10, 512])
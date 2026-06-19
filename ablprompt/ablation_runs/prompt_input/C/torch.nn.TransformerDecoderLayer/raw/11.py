import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Prepare input tensors
tgt = torch.rand(10, 32, d_model)  # (sequence length, batch size, feature dimension)
memory = torch.rand(20, 32, d_model)  # (sequence length, batch size, feature dimension)

# Perform forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be (10, 32, 512)
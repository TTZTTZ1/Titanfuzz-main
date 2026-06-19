import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8

# Create a TransformerDecoderLayer instance
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Generate random input tensors
tgt = torch.randn(10, 32, d_model)  # (sequence length, batch size, feature dimension)
memory = torch.randn(20, 32, d_model)  # (sequence length, batch size, feature dimension)

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be (10, 32, 512)
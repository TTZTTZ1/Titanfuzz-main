import torch
from torch.nn import TransformerDecoderLayer

# Define model dimensions
d_model = 512
nhead = 8

# Create a TransformerDecoderLayer instance
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Dummy input tensors
tgt = torch.randn(32, 10, d_model)  # Batch size 32, sequence length 10
memory = torch.randn(32, 10, d_model)  # Same batch size and sequence length as tgt

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [32, 10, 512]
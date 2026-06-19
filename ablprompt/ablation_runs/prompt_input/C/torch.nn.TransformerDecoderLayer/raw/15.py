import torch
from torch.nn import TransformerDecoderLayer

# Define model dimensions
d_model = 512
nhead = 8

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Dummy input tensors
tgt = torch.randn(32, 64, d_model)  # Batch size: 32, Sequence length: 64, Feature dimension: 512
memory = torch.randn(32, 50, d_model)  # Batch size: 32, Sequence length: 50, Feature dimension: 512

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [32, 64, 512]
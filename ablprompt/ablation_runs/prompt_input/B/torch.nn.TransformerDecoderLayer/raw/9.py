import torch
from torch.nn import TransformerDecoderLayer

# Define model dimensions
d_model = 512
nhead = 8

# Create a TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Prepare input tensors
tgt = torch.rand(32, 64, d_model)  # Batch size: 32, Sequence length: 64
memory = torch.rand(32, 128, d_model)  # Batch size: 32, Sequence length: 128

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [32, 64, 512]
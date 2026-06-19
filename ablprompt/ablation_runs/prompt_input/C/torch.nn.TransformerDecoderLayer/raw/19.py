import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8

# Create a transformer decoder layer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Generate random inputs
tgt = torch.randn(32, 64, d_model)  # Batch size 32, sequence length 64, feature dimension 512
memory = torch.randn(32, 512, d_model)  # Batch size 32, sequence length 512, feature dimension 512

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [32, 64, 512]
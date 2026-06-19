import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Prepare input tensors
tgt = torch.randn(32, 10, d_model)  # Batch size 32, sequence length 10, feature dimension 512
memory = torch.randn(32, 20, d_model)  # Batch size 32, sequence length 20, feature dimension 512

# Perform forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [32, 10, 512]
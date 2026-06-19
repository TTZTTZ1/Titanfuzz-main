import torch
from torch.nn import TransformerDecoderLayer

# Define model dimensions
d_model = 512
nhead = 8

# Create a TransformerDecoderLayer instance
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Dummy input tensors
tgt = torch.randn(10, 32, d_model)  # (sequence_length, batch_size, d_model)
memory = torch.randn(10, 32, d_model)  # (sequence_length, batch_size, d_model)

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be (sequence_length, batch_size, d_model)
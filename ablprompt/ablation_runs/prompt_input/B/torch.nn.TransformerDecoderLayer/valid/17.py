import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Dummy input tensors
tgt = torch.randn(10, 32, d_model)  # (seq_len, batch_size, d_model)
memory = torch.randn(10, 32, d_model)  # (seq_len, batch_size, d_model)

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be (seq_len, batch_size, d_model)
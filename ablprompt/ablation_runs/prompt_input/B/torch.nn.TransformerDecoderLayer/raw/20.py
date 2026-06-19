import torch
from torch import nn

# Define the dimensions
d_model = 512
nhead = 8
dim_feedforward = 2048
batch_size = 32
seq_len = 10

# Create dummy tensors
tgt = torch.randn(seq_len, batch_size, d_model)
memory = torch.randn(seq_len, batch_size, d_model)

# Initialize the TransformerDecoderLayer
decoder_layer = nn.TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward)

# Perform the forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [seq_len, batch_size, d_model]
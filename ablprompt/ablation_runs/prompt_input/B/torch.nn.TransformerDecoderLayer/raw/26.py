import torch
from torch import nn

# Define the dimensions
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_size = 32
tgt_seq_len = 10
memory_seq_len = 15

# Create a dummy input tensor for the target sequence
tgt = torch.randn(batch_size, tgt_seq_len, d_model)

# Create a dummy input tensor for the memory (encoder output)
memory = torch.randn(batch_size, memory_seq_len, d_model)

# Initialize the TransformerDecoderLayer
decoder_layer = nn.TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout)

# Perform the forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [batch_size, tgt_seq_len, d_model]
import torch
import torch.nn as nn

# Define the dimensions
d_model = 512
nhead = 8
dim_feedforward = 2048
batch_size = 32
tgt_seq_len = 10
src_seq_len = 15

# Create dummy tensors
tgt = torch.randn(batch_size, tgt_seq_len, d_model)
memory = torch.randn(batch_size, src_seq_len, d_model)

# Initialize the TransformerDecoderLayer
decoder_layer = nn.TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward)

# Perform the forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [batch_size, tgt_seq_len, d_model]
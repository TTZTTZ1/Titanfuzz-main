import torch
from torch.nn import TransformerDecoderLayer, MultiheadAttention, Linear, LayerNorm

# Define the dimensions
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_size = 32
src_seq_len = 10
tgt_seq_len = 15

# Create a sample input
src = torch.randn(src_seq_len, batch_size, d_model)
tgt = torch.randn(tgt_seq_len, batch_size, d_model)

# Initialize the layers
self_attn = MultiheadAttention(d_model, nhead, dropout=dropout)
ffn = Linear(d_model, dim_feedforward)
layer_norm1 = LayerNorm(d_model)
layer_norm2 = LayerNorm(d_model)

# Create the TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout)

# Perform the forward pass
output = decoder_layer(tgt, src, tgt_mask=None, memory_mask=None, tgt_key_padding_mask=None, memory_key_padding_mask=None)

print(output.shape)  # Should be [tgt_seq_len, batch_size, d_model]
import torch
from torch.nn import TransformerEncoderLayer, MultiheadAttention

# Define the model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1

# Create a custom multi-head attention mechanism
multihead_attn = MultiheadAttention(embed_dim=d_model, num_heads=nhead)

# Initialize the TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout)

# Generate random input tensor
src = torch.randn(10, 32, d_model)  # (seq_len, batch, features)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
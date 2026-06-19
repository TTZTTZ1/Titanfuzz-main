import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout)

# Prepare input tensors
tgt = torch.randn(10, 32, d_model)  # (sequence length, batch size, feature dimension)
memory = torch.randn(10, 32, d_model)  # (sequence length, batch size, feature dimension)

# Perform forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be (10, 32, 512)
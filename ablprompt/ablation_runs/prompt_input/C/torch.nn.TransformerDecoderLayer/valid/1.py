import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout)

# Dummy input tensors
tgt = torch.randn(10, 32, d_model)  # Batch size 32, sequence length 10, feature dimension 512
memory = torch.randn(10, 32, d_model)  # Same dimensions as tgt

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [10, 32, 512]
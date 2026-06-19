import torch
from torch.nn import TransformerDecoderLayer

# Define model dimensions and parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, activation=activation)

# Dummy input tensors
tgt = torch.randn(32, 10, d_model)  # Batch size 32, sequence length 10, feature dimension 512
memory = torch.randn(32, 20, d_model)  # Batch size 32, sequence length 20, feature dimension 512

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([32, 10, 512])
import torch
from torch.nn import TransformerEncoderLayer

# Define model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create a TransformerEncoderLayer instance
encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, activation=activation)

# Prepare input tensor
src = torch.rand(10, 32, 512)  # (seq_len, batch, features)

# Forward pass through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
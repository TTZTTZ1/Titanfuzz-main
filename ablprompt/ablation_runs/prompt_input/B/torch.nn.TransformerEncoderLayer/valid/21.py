import torch
from torch.nn import TransformerEncoderLayer

# Define the model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, activation=activation)

# Prepare the input tensor
src = torch.randn(10, 32, d_model)  # (seq_len, batch, features)

# Apply the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
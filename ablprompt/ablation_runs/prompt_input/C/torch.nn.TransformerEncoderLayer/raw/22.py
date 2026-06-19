import torch
import torch.nn as nn

# Define the dimensions and other parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_size = 32
sequence_length = 10

# Create an instance of TransformerEncoderLayer
encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout)

# Generate random source data
src = torch.randn(sequence_length, batch_size, d_model)

# Pass the source data through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should be [sequence_length, batch_size, d_model]
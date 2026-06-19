import torch
from torch.nn import TransformerEncoderLayer

# Define the input dimensions and other parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_first = True

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout, batch_first)

# Prepare some sample input data (batch_size, seq_len, d_model)
batch_size = 32
seq_len = 10
sample_input = torch.randn(batch_size, seq_len, d_model)

# Pass the input through the encoder layer
output = encoder_layer(sample_input)

print(output.shape)  # Output should be (batch_size, seq_len, d_model)
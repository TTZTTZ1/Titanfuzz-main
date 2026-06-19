import torch
from torch.nn import TransformerEncoderLayer

# Define the model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout)

# Example input tensor (batch_size, seq_len, d_model)
src = torch.rand(10, 32, 512)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Expected output shape: (seq_len, batch_size, d_model)
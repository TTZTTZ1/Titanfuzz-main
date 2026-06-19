import torch
from torch.nn import TransformerEncoderLayer

# Define the dimensions for the input tensor and the model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1

# Create an instance of TransformerEncoderLayer
transformer_encoder_layer = TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout)

# Generate a random input tensor
src = torch.rand(10, 32, d_model)  # (sequence length, batch size, feature size)

# Pass the input through the transformer encoder layer
output = transformer_encoder_layer(src)

print(output.shape)
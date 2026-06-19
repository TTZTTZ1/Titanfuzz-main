import torch
from torch.nn import TransformerDecoderLayer

# Define the input dimensions and other parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout, activation)

# Dummy input tensors
src = torch.rand(32, 10, d_model)  # (sequence length, batch size, embedding dimension)
tgt = torch.rand(20, 10, d_model)  # (sequence length, batch size, embedding dimension)

# Forward pass through the decoder layer
output = decoder_layer(tgt, src)

print(output.shape)  # Should print: torch.Size([20, 10, 512])
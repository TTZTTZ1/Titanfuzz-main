import torch
from torch.nn import TransformerDecoderLayer, Embedding, Linear

# Define the input dimensions and other parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
layer_norm_eps = 1e-5

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout, layer_norm_eps)

# Create dummy input tensors for testing
tgt = torch.rand(10, 32, d_model)  # Target sequence of length 10, batch size 32, feature dimension 512
memory = torch.rand(20, 32, d_model)  # Memory sequence of length 20, batch size 32, feature dimension 512

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)
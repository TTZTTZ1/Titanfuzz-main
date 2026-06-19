import torch
from torch.nn import TransformerDecoderLayer, MultiheadAttention

# Define the input dimensions and other parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create an instance of MultiheadAttention
multihead_attn = MultiheadAttention(d_model, nhead)

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout, activation)

# Dummy input tensors for testing
tgt = torch.rand(10, 32, d_model)  # Target sequence of shape (sequence_length, batch_size, d_model)
memory = torch.rand(20, 32, d_model)  # Memory sequence of shape (sequence_length, batch_size, d_model)

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
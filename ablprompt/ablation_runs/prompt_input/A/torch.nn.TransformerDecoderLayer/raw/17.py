import torch
from torch.nn import TransformerDecoderLayer, Linear, LayerNorm

# Define the input dimensions and other parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout, activation)

# Prepare some dummy input tensors
tgt = torch.randn(32, 10, d_model)  # Target sequence (batch_size, seq_len, d_model)
memory = torch.randn(32, 20, d_model)  # Memory sequence (batch_size, memory_seq_len, d_model)

# Perform a forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([32, 10, 512])
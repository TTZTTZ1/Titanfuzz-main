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

# Example inputs for the decoder layer
tgt = torch.rand(32, 10, d_model)  # Target sequence of shape (sequence_length, batch_size, d_model)
memory = torch.rand(32, 10, d_model)  # Memory sequence of shape (sequence_length, batch_size, d_model)

# Forward pass through the transformer decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
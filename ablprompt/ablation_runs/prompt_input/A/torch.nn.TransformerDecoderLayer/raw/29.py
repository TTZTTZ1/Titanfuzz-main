import torch
from torch.nn import TransformerDecoderLayer

# Define the dimensions for the model
d_model = 512
nhead = 8

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead)

# Example input tensors
tgt = torch.rand(10, 32, d_model)  # Target sequence of shape (seq_len, batch_size, d_model)
memory = torch.rand(20, 32, d_model)  # Memory sequence of shape (seq_len, batch_size, d_model)

# Perform a forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
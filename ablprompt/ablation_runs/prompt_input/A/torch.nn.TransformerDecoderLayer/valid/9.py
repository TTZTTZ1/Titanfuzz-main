import torch
from torch.nn import TransformerDecoderLayer

# Define the dimensions for the input and output embeddings
d_model = 512
nhead = 8

# Create an instance of the TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead)

# Prepare some sample input data
tgt = torch.rand(10, 32, d_model)  # (sequence length, batch size, embedding dimension)
memory = torch.rand(20, 32, d_model)  # (sequence length, batch size, embedding dimension)

# Pass the input data through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
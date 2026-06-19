import torch
from torch.nn import TransformerDecoderLayer

# Define the dimensions for the input and output embeddings, as well as the number of heads in the multi-head attention mechanism
d_model = 512
nhead = 8

# Create an instance of the TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Generate random input tensors for the decoder layer
tgt = torch.randn(10, 32, d_model)  # (sequence length, batch size, embedding dimension)
memory = torch.randn(20, 32, d_model)  # (sequence length, batch size, embedding dimension)

# Pass the input tensors through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
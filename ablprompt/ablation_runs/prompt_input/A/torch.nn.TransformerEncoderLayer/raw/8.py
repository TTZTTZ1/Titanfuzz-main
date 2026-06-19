import torch
from torch.nn import TransformerEncoderLayer

# Define the dimensions for the input and output embeddings
d_model = 512
nhead = 8

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model, nhead)

# Example input tensor (batch_size, sequence_length, d_model)
src = torch.rand(10, 32, d_model)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
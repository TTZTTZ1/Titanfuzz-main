import torch
from torch.nn import TransformerEncoderLayer

# Define the dimensions for the input and output of the transformer layer
d_model = 512
nhead = 8

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model, nhead)

# Example input tensor (batch_size, seq_len, d_model)
src = torch.rand(10, 32, 512)  # batch size of 10, sequence length of 32

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
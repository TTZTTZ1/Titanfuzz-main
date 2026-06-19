import torch
from torch.nn import TransformerEncoderLayer

# Define the dimensions for the input tensor
d_model = 512
nhead = 8

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model, nhead)

# Create a random input tensor with shape (sequence_length, batch_size, d_model)
sequence_length = 10
batch_size = 32
input_tensor = torch.randn(sequence_length, batch_size, d_model)

# Pass the input tensor through the encoder layer
output_tensor = encoder_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([10, 32, 512])
import torch
from torch.nn import TransformerEncoderLayer

# Define the dimensions for the input and output embeddings, as well as the number of heads in the multi-head attention mechanism.
d_model = 512
nhead = 8

# Create an instance of the TransformerEncoderLayer.
transformer_encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead)

# Generate a random input tensor with shape (sequence_length, batch_size, d_model).
sequence_length = 10
batch_size = 32
input_tensor = torch.randn(sequence_length, batch_size, d_model)

# Pass the input tensor through the transformer encoder layer to get the output.
output_tensor = transformer_encoder_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([10, 32, 512])
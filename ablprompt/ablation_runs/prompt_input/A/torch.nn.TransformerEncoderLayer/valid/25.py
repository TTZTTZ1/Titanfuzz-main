import torch
from torch.nn import TransformerEncoderLayer

# Define the input tensor and other parameters
input_tensor = torch.rand(10, 32, 512)  # (sequence_length, batch_size, embedding_dim)
d_model = 512
nhead = 8

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead)

# Pass the input tensor through the encoder layer
output_tensor = encoder_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([10, 32, 512])
import torch
from torch.nn import TransformerEncoderLayer

# Define the input tensor and other parameters
input_tensor = torch.rand(10, 32, 512)  # (sequence length, batch size, embedding dimension)
d_model = 512
nhead = 8

# Create an instance of TransformerEncoderLayer
transformer_encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead)

# Pass the input tensor through the transformer encoder layer
output_tensor = transformer_encoder_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([10, 32, 512])
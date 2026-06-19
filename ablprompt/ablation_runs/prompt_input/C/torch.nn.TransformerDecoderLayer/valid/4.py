import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Prepare input tensors
tgt = torch.randn(10, 32, d_model)  # Shape: [sequence_length, batch_size, d_model]
memory = torch.randn(20, 32, d_model)  # Shape: [sequence_length, batch_size, d_model]

# Perform forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
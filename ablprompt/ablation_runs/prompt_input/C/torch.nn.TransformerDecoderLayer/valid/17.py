import torch
from torch.nn import TransformerDecoderLayer

# Define the model parameters
d_model = 512
nhead = 8

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Prepare the input tensors
tgt = torch.rand(10, 32, d_model)  # (sequence_length, batch_size, d_model)
memory = torch.rand(10, 32, d_model)  # (sequence_length, batch_size, d_model)

# Perform the forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be (10, 32, 512)
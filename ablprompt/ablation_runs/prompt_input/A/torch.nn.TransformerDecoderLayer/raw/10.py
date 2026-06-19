import torch
from torch.nn import TransformerDecoderLayer

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=512, nhead=8)

# Prepare input tensors
tgt = torch.rand(10, 32, 512)  # Target sequence of shape (sequence_length, batch_size, d_model)
memory = torch.rand(20, 32, 512)  # Memory sequence of shape (sequence_length, batch_size, d_model)

# Perform a forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
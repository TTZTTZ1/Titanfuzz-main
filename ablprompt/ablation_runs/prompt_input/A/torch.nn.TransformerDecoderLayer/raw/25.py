import torch
from torch.nn import TransformerDecoderLayer

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=512, nhead=8)

# Dummy input tensors
tgt = torch.rand(10, 32, 512)  # (sequence length, batch size, embedding dimension)
memory = torch.rand(20, 32, 512)  # (sequence length, batch size, embedding dimension)

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
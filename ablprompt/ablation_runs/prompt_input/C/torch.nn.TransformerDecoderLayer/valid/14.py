import torch
from torch.nn import TransformerDecoderLayer

# Initialize the TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=512, nhead=8)

# Create dummy input tensors
tgt = torch.randn(10, 32, 512)  # (sequence length, batch size, feature dim)
memory = torch.randn(10, 32, 512)  # (sequence length, batch size, feature dim)

# Perform the forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
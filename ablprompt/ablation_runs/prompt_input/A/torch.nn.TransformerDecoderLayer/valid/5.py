import torch
from torch.nn import TransformerDecoderLayer

# Create a TransformerDecoderLayer instance
decoder_layer = TransformerDecoderLayer(d_model=512, nhead=8)

# Prepare input tensors
tgt = torch.randn(10, 32, 512)  # (sequence_length, batch_size, d_model)
memory = torch.randn(20, 32, 512)  # (sequence_length, batch_size, d_model)

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
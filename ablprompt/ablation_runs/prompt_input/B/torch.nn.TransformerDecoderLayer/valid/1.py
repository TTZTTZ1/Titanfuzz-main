import torch
from torch.nn import TransformerDecoderLayer

# Create a TransformerDecoderLayer instance
decoder_layer = TransformerDecoderLayer(d_model=512, nhead=8)

# Prepare input tensors
tgt = torch.randn(10, 32, 512)  # Batch size of 32, sequence length of 10, feature dimension of 512
memory = torch.randn(20, 32, 512)  # Batch size of 32, sequence length of 20, feature dimension of 512

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [10, 32, 512]
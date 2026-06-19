import torch
from torch.nn import Transformer

# Initialize the Transformer model
model = Transformer(d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dim_feedforward=2048, dropout=0.1)

# Dummy input tensors for demonstration
src = torch.rand((10, 32, 512))  # (sequence length, batch size, embedding dimension)
tgt = torch.rand((20, 32, 512))  # (sequence length, batch size, embedding dimension)

# Forward pass through the Transformer model
output = model(src, tgt)

print(output.shape)  # Should print: torch.Size([20, 32, 512])
import torch
from torch.nn import Transformer

# Initialize the Transformer model
model = Transformer(d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dim_feedforward=2048)

# Dummy input tensors
src = torch.rand((10, 32, 512))  # (sequence length, batch size, feature dimensions)
tgt = torch.rand((20, 32, 512))  # (sequence length, batch size, feature dimensions)

# Forward pass through the model
output = model(src, tgt)

print(output.shape)  # Should print: torch.Size([20, 32, 512])
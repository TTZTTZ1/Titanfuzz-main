import torch
from torch.nn import Transformer

# Initialize a simple Transformer model
model = Transformer(d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dim_feedforward=2048)

# Example input tensors for encoding and decoding
src = torch.rand((10, 32, 512))  # (sequence_length, batch_size, d_model)
tgt = torch.rand((20, 32, 512))  # (sequence_length, batch_size, d_model)

# Forward pass through the transformer
output = model(src, tgt)

print(output.shape)  # Should print: torch.Size([20, 32, 512])
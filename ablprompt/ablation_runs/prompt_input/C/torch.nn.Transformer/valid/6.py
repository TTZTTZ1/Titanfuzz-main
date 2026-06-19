import torch
from torch.nn import Transformer

# Define model parameters
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048

# Create the Transformer model
model = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers, num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward)

# Dummy input tensors
src = torch.rand((10, 32, d_model))
tgt = torch.rand((20, 32, d_model))

# Forward pass
output = model(src, tgt)

print(output.shape)  # Should be (20, 32, d_model)
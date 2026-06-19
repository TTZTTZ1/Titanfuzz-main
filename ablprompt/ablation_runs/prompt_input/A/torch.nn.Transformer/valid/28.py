import torch
from torch.nn import Transformer

# Define model parameters
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1

# Initialize the transformer model
transformer_model = Transformer(d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout)

# Example input tensors
src = torch.rand((10, 32, d_model))
tgt = torch.rand((20, 32, d_model))

# Forward pass through the transformer
output = transformer_model(src, tgt)

print(output.shape)
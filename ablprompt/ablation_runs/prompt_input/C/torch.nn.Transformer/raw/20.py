import torch
from torch.nn import Transformer

# Define model parameters
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create the Transformer model
transformer = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers,
                          num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward,
                          dropout=dropout, activation=activation)

# Dummy input tensors
src = torch.rand((10, 32, 512))
tgt = torch.rand((20, 32, 512))

# Forward pass
output = transformer(src, tgt)

print(output.shape)  # Should be (20, 32, 512)
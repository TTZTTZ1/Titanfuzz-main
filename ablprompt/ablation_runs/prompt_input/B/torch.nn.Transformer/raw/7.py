import torch
from torch.nn import Transformer

# Define model parameters
d_model = 256
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Initialize the Transformer model
model = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers,
                   num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward,
                   dropout=dropout, activation=activation)

# Create dummy input data
src = torch.rand(10, 32, d_model)  # (sequence_length, batch_size, d_model)
tgt = torch.rand(20, 32, d_model)  # (sequence_length, batch_size, d_model)

# Forward pass
output = model(src, tgt)
print(output.shape)  # Expected output shape: (20, 32, 256)
import torch
from torch.nn import Transformer

# Define model parameters
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1

# Initialize the Transformer model
model = Transformer(d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout)

# Example input tensors
src = torch.rand(10, 32, d_model)  # (sequence length, batch size, embedding dimension)
tgt = torch.rand(20, 32, d_model)  # (sequence length, batch size, embedding dimension)

# Forward pass
output = model(src, tgt)

print(output.shape)  # Should be (tgt_len, batch_size, d_model)
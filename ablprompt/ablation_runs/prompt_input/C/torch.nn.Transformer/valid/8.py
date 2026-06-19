import torch
import torch.nn as nn

# Define hyperparameters
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create the Transformer model
transformer = nn.Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers,
                            num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward,
                            dropout=dropout, activation=activation)

# Generate some dummy data
src = torch.rand(10, 32, d_model)  # (sequence_length, batch_size, embedding_dim)
tgt = torch.rand(20, 32, d_model)  # (sequence_length, batch_size, embedding_dim)

# Forward pass
output = transformer(src, tgt)

print(output.shape)  # Should be (20, 32, 512)
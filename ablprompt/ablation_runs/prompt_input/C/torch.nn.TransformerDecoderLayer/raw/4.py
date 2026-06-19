import torch
import torch.nn as nn

# Define the dimensions
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_size = 32
sequence_length = 10

# Create dummy tensors for target and memory
tgt = torch.randn(sequence_length, batch_size, d_model)
memory = torch.randn(sequence_length, batch_size, d_model)

# Initialize the TransformerDecoderLayer
decoder_layer = nn.TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout)

# Forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [sequence_length, batch_size, d_model]
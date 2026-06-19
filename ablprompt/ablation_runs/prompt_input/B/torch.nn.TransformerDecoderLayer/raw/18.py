import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_first = True

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, batch_first=batch_first)

# Dummy input tensors
tgt = torch.rand(10, 32, d_model) if batch_first else torch.rand(32, 10, d_model)
memory = torch.rand(15, 32, d_model) if batch_first else torch.rand(32, 15, d_model)

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)
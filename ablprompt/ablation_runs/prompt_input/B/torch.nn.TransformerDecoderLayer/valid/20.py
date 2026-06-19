import torch
from torch import nn

# Define the model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_first = True
norm_first = False

# Create an instance of TransformerDecoderLayer
decoder_layer = nn.TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, batch_first=batch_first, norm_first=norm_first)

# Create dummy input tensors
tgt = torch.randn(32, 10, d_model) if batch_first else torch.randn(10, 32, d_model)
memory = torch.randn(32, 15, d_model) if batch_first else torch.randn(15, 32, d_model)

# Perform the forward pass
output = decoder_layer(tgt, memory)

print(output.shape)
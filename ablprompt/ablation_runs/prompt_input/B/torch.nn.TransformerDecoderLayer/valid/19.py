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

# Prepare input tensors
tgt = torch.rand(32, 10, d_model) if batch_first else torch.rand(10, 32, d_model)
memory = torch.rand(32, 15, d_model) if batch_first else torch.rand(15, 32, d_model)

# Perform forward pass
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [32, 10, 512] if batch_first=True
import torch
from torch.nn import TransformerDecoderLayer

# Define the dimensions
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_first = True
norm_first = False

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, batch_first=batch_first, norm_first=norm_first)

# Prepare the input tensors
tgt = torch.randn(3, 10, d_model) if not batch_first else torch.randn(10, 3, d_model)
memory = torch.randn(3, 10, d_model) if not batch_first else torch.randn(10, 3, d_model)

# Perform the forward pass
output = decoder_layer(tgt, memory)

print(output.shape)
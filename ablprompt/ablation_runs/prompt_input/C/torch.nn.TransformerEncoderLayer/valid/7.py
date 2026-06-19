import torch
from torch import nn

# Define the model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_first = False
norm_first = True

# Create an instance of TransformerEncoderLayer
encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, batch_first=batch_first, norm_first=norm_first)

# Prepare some sample data
src = torch.randn(10, 32, 512)  # (seq_len, batch, features)

# Pass the data through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
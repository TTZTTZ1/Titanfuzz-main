import torch
from torch.nn import TransformerEncoderLayer

# Define model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_first = False
norm_first = True

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, batch_first=batch_first, norm_first=norm_first)

# Prepare input data
src = torch.randn(32, 10, d_model)  # (batch, seq_len, d_model)

# Apply the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([32, 10, 512])
import torch
from torch.nn import TransformerEncoderLayer

# Define model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_first = True
norm_first = False

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, batch_first=batch_first, norm_first=norm_first)

# Prepare source tensor
src = torch.randn(10, 32, 512)  # (seq_len, batch, features)

# Apply the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
import torch
from torch.nn import TransformerEncoderLayer

# Define model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'
layer_norm_eps = 1e-05
batch_first = False
norm_first = False
bias = True
device = None
dtype = None

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, 
                                        dropout=dropout, activation=activation, layer_norm_eps=layer_norm_eps, 
                                        batch_first=batch_first, norm_first=norm_first, bias=bias, 
                                        device=device, dtype=dtype)

# Prepare input data
src = torch.randn(10, 32, 512)  # (seq_len, batch, features)

# Apply the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
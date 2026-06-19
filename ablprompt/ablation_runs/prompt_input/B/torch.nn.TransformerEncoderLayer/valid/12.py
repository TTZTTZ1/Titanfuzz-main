import torch
from torch.nn import TransformerEncoderLayer

# Define the model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'
layer_norm_eps = 1e-05
batch_first = False
norm_first = False
bias = True

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, 
                                       dropout=dropout, activation=activation, layer_norm_eps=layer_norm_eps, 
                                       batch_first=batch_first, norm_first=norm_first, bias=bias)

# Prepare input tensor
src = torch.randn(32, 10, d_model)  # (batch_size, sequence_length, d_model)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Expected output shape: (batch_size, sequence_length, d_model)
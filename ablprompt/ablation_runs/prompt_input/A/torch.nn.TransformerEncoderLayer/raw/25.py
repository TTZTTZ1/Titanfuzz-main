import torch
from torch.nn import TransformerEncoderLayer

# Define the input parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
layer_norm_eps = 1e-5
batch_first = True

# Create an instance of TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout, layer_norm_eps, batch_first)

# Generate some random input data
src = torch.rand(10, 32, d_model)  # (sequence_length, batch_size, d_model)

# Pass the input through the encoder layer
output = encoder_layer(src)

print(output.shape)  # Should be (10, 32, 512)
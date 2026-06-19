import torch
from torch.nn import TransformerEncoderLayer

# Define the model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
layer_norm_eps = 1e-5
batch_first = True

# Create an instance of TransformerEncoderLayer
transformer_encoder_layer = TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout, layer_norm_eps, batch_first)

# Example input tensor (batch_size, sequence_length, d_model)
input_tensor = torch.randn(10, 32, 512)

# Pass the input through the transformer encoder layer
output_tensor = transformer_encoder_layer(input_tensor)

print(output_tensor.shape)  # Output shape should be (10, 32, 512)
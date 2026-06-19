import torch
from torch.nn import Transformer, TransformerEncoderLayer, TransformerDecoderLayer

# Define the model
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

encoder_layer = TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout, activation)
decoder_layer = TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout, activation)
transformer = Transformer(encoder_layer, decoder_layer, num_encoder_layers, num_decoder_layers, d_model, nhead, dim_feedforward, dropout, activation)

# Prepare data
src = torch.rand((10, 32, d_model))
tgt = torch.rand((20, 32, d_model))

# Forward pass
output = transformer(src, tgt)
print(output.shape)  # Should be (20, 32, d_model)
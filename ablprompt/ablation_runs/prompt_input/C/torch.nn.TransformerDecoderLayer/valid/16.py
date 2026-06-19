import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'
layer_norm_eps = 1e-05
batch_first = False
norm_first = True

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward,
                                         dropout=dropout, activation=activation, layer_norm_eps=layer_norm_eps,
                                         batch_first=batch_first, norm_first=norm_first)

# Dummy input tensors
tgt = torch.randn(10, 32, d_model)  # (sequence_length, batch_size, d_model)
memory = torch.randn(10, 32, d_model)  # (sequence_length, batch_size, d_model)

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be (10, 32, 512)
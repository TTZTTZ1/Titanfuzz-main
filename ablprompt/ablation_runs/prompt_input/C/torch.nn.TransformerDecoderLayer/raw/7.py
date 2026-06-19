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
norm_first = False
bias = True
device = None
dtype = None

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward,
                                        dropout=dropout, activation=activation, layer_norm_eps=layer_norm_eps,
                                        batch_first=batch_first, norm_first=norm_first, bias=bias,
                                        device=device, dtype=dtype)

# Dummy input tensors
tgt = torch.randn(32, 64, d_model)  # Batch size 32, sequence length 64, feature dimension 512
memory = torch.randn(32, 128, d_model)  # Batch size 32, sequence length 128, feature dimension 512

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [32, 64, 512]
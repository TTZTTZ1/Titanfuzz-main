import torch
from torch.nn import TransformerDecoderLayer

# Define the model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, activation=activation)

# Prepare input tensors
tgt = torch.randn(10, 32, d_model)  # Batch size: 32, Sequence length: 10, Feature dimension: 512
memory = torch.randn(10, 32, d_model)  # Batch size: 32, Sequence length: 10, Feature dimension: 512

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [10, 32, 512]
import torch
from torch.nn import TransformerDecoderLayer

# Define model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
batch_first = True
norm_first = False

# Create a TransformerDecoderLayer instance
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, batch_first=batch_first, norm_first=norm_first)

# Dummy input tensors
tgt = torch.randn(3, 10, d_model)  # [batch_size, seq_len, d_model]
memory = torch.randn(3, 10, d_model)  # [batch_size, seq_len, d_model]

# Forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should be [batch_size, seq_len, d_model]
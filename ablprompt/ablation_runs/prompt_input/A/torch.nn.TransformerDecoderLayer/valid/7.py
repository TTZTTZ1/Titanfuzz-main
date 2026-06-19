import torch
from torch.nn import TransformerDecoderLayer

# Define input dimensions and other parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout)

# Dummy input tensors for demonstration
tgt = torch.randn(10, 32, d_model)  # Target sequence of shape (seq_len, batch_size, d_model)
memory = torch.randn(10, 32, d_model)  # Memory sequence of shape (seq_len, batch_size, d_model)

# Perform a forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
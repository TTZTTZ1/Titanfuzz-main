import torch
from torch.nn import TransformerDecoderLayer

# Define the dimensions for the input and output embeddings, number of heads, and feedforward network hidden size
d_model = 512
nhead = 8
dim_feedforward = 2048

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward)

# Example input tensors: memory (encoder outputs) and tgt (decoder inputs)
memory = torch.rand(10, 32, d_model)  # Shape: (seq_len, batch_size, d_model)
tgt = torch.rand(20, 32, d_model)     # Shape: (tgt_seq_len, batch_size, d_model)

# Perform a forward pass through the decoder layer
output = decoder_layer(tgt, memory)

print(output.shape)  # Should print: torch.Size([20, 32, 512])
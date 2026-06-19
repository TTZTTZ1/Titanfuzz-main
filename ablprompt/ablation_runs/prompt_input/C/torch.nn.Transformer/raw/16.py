import torch
import torch.nn as nn

# Define the dimensions
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
batch_size = 16
src_seq_len = 10
tgt_seq_len = 10
input_dim = 512

# Create random input tensors
src = torch.rand(batch_size, src_seq_len, input_dim)
tgt = torch.rand(batch_size, tgt_seq_len, input_dim)

# Initialize the Transformer model
transformer = nn.Transformer(d_model=d_model, nhead=nhead, 
                            num_encoder_layers=num_encoder_layers, 
                            num_decoder_layers=num_decoder_layers, 
                            dim_feedforward=dim_feedforward, 
                            batch_first=True)

# Generate a causal mask for the target sequence
tgt_mask = nn.Transformer.generate_square_subsequent_mask(tgt.size(1))

# Perform the forward pass
output = transformer(src, tgt, tgt_mask=tgt_mask)

print(output.shape)  # Should be (16, 10, 512)
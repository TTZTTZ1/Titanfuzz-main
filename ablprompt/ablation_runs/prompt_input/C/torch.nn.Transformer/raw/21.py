import torch
from torch.nn import Transformer

# Define model parameters
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048

# Initialize the Transformer model
model = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers, num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward)

# Create dummy input tensors
src = torch.rand(10, 32, 512)  # (sequence_length, batch_size, d_model)
tgt = torch.rand(20, 32, 512)  # (sequence_length, batch_size, d_model)

# Generate a square causal mask for the decoder
tgt_mask = generate_square_subsequent_mask(tgt.size(0)).to(device=model.device)

# Forward pass through the model
output = model(src, tgt, tgt_mask=tgt_mask)

print(output.shape)  # Expected output shape: (20, 32, 512)
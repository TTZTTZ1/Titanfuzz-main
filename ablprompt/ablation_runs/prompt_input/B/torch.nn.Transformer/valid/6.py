import torch
from torch.nn import Transformer

# Define model parameters
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Initialize the Transformer model
model = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers, 
                    num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward, 
                    dropout=dropout, activation=activation)

# Dummy input data
src = torch.rand((10, 32, 512))
tgt = torch.rand((20, 32, 512))

# Generate a causal mask for the decoder
tgt_mask = model.generate_square_subsequent_mask(tgt.size(0)).to(device='cuda' if torch.cuda.is_available() else 'cpu')

# Forward pass
output = model(src, tgt, tgt_mask=tgt_mask)

print(output.shape)  # Expected output shape: (20, 32, 512)
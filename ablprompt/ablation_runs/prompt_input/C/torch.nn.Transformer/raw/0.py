import torch
import torch.nn as nn

# Define model parameters
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'
batch_first = True

# Create the Transformer model
transformer = nn.Transformer(
    d_model=d_model,
    nhead=nhead,
    num_encoder_layers=num_encoder_layers,
    num_decoder_layers=num_decoder_layers,
    dim_feedforward=dim_feedforward,
    dropout=dropout,
    activation=activation,
    batch_first=batch_first
)

# Dummy input data
src = torch.rand(10, 32, d_model)  # (seq_len, batch_size, d_model)
tgt = torch.rand(20, 32, d_model)  # (seq_len, batch_size, d_model)

# Generate a causal mask for the decoder
tgt_mask = nn.Transformer.generate_square_subsequent_mask(tgt.size(0)).to(device='cuda' if torch.cuda.is_available() else 'cpu')

# Forward pass
output = transformer(src, tgt, tgt_mask=tgt_mask)

print(output.shape)  # Should be (tgt_seq_len, batch_size, d_model)
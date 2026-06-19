import torch
from torch.nn import Transformer, LayerNorm, Linear
from torch.nn.functional import pad

# Define a simple model using Transformer
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, input_dim, output_dim, d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6):
        super(SimpleTransformerModel, self).__init__()
        self.embedding = Linear(input_dim, d_model)
        self.transformer = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers, num_decoder_layers=num_decoder_layers)
        self.fc_out = Linear(d_model, output_dim)

    def forward(self, src, tgt):
        src = self.embedding(src)
        tgt = self.embedding(tgt)
        output = self.transformer(src, tgt)
        return self.fc_out(output)

# Create an instance of the model
model = SimpleTransformerModel(input_dim=10, output_dim=5)

# Dummy input data
src = torch.rand(10, 32, 10)  # (sequence length, batch size, input dimension)
tgt = torch.rand(15, 32, 10)  # (sequence length, batch size, input dimension)

# Forward pass
output = model(src, tgt)
print(output.shape)  # Expected shape: (15, 32, 5)
import torch
from torch.nn import Transformer, MultiHeadAttention, Linear, LayerNorm

# Define a simple model using Transformer
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim, nhead, num_layers):
        super(SimpleTransformerModel, self).__init__()
        self.embedding = Linear(input_dim, hidden_dim)
        self.transformer = Transformer(d_model=hidden_dim, nhead=nhead, num_encoder_layers=num_layers, num_decoder_layers=num_layers)
        self.fc_out = Linear(hidden_dim, output_dim)
        self.norm = LayerNorm(hidden_dim)

    def forward(self, src, tgt):
        src = self.embedding(src) * torch.sqrt(torch.tensor(hidden_dim, dtype=torch.float32))
        tgt = self.embedding(tgt) * torch.sqrt(torch.tensor(hidden_dim, dtype=torch.float32))
        src = self.norm(src)
        tgt = self.norm(tgt)
        output = self.transformer(src, tgt)
        return self.fc_out(output)

# Example usage
input_dim = 10
output_dim = 1
hidden_dim = 256
nhead = 8
num_layers = 2

model = SimpleTransformerModel(input_dim, output_dim, hidden_dim, nhead, num_layers)
src = torch.rand(10, 32, input_dim)  # (seq_len, batch_size, input_dim)
tgt = torch.rand(10, 32, input_dim)  # (seq_len, batch_size, input_dim)

output = model(src, tgt)
print(output.shape)  # Should be (seq_len, batch_size, output_dim)
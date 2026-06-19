import torch
from torch.nn import Transformer, MultiHeadAttention, Linear, LayerNorm

# Define a simple model using Transformer
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, vocab_size):
        super(SimpleTransformerModel, self).__init__()
        self.embedding = Linear(vocab_size, d_model)
        self.transformer = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers,
                                        num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward)
        self.fc_out = Linear(d_model, vocab_size)

    def forward(self, src, tgt):
        src = self.embedding(src) * torch.sqrt(torch.tensor(d_model, dtype=torch.float32))
        tgt = self.embedding(tgt) * torch.sqrt(torch.tensor(d_model, dtype=torch.float32))
        output = self.transformer(src, tgt)
        return self.fc_out(output)

# Initialize the model
model = SimpleTransformerModel(d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dim_feedforward=2048, vocab_size=10000)

# Dummy data
src = torch.randint(0, 10000, (10, 32))
tgt = torch.randint(0, 10000, (10, 32))

# Forward pass
output = model(src, tgt)
print(output.shape)  # Should be (10, 32, 10000)
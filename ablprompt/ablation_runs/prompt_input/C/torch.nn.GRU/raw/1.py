import torch
import torch.nn as nn

# Define the GRU model
class GRUNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False):
        super(GRUNet, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional)
        
    def forward(self, x):
        h0 = torch.zeros(self.num_layers * (2 if self.bidirectional else 1), x.size(0), self.hidden_size).to(x.device)
        out, _ = self.gru(x, h0)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
bidirectional = True

model = GRUNet(input_size, hidden_size, num_layers, bidirectional)
input_seq = torch.randn(5, 3, 10)  # (seq_len, batch, input_size)

output = model(input_seq)
print(output.shape)  # Should be (5, 3, 40) if bidirectional=True
import torch
import torch.nn as nn

# Define the GRU model
class GRUNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(GRUNet, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(num_layers, x.size(0), hidden_size).to(x.device)
        out, _ = self.gru(x, h0)
        out = self.fc(out[:, -1, :])
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
output_size = 1
batch_size = 3
seq_length = 5

model = GRUNet(input_size, hidden_size, num_layers, output_size)
input_data = torch.randn(seq_length, batch_size, input_size)
output = model(input_data)
print(output.shape)  # Should be (batch_size, output_size)
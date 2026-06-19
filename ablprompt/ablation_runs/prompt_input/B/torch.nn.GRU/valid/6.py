import torch
import torch.nn as nn

# Define the GRU model
class GRUNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False):
        super(GRUNet, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers, bidirectional=bidirectional)
        self.fc = nn.Linear(hidden_size * (2 if bidirectional else 1), 1)

    def forward(self, x):
        out, _ = self.gru(x)
        out = self.fc(out[:, -1, :])
        return out

# Create an instance of the GRU model
input_size = 10
hidden_size = 20
num_layers = 2
bidirectional = True
model = GRUNet(input_size, hidden_size, num_layers, bidirectional)

# Generate random input data
batch_size = 3
seq_length = 5
input_data = torch.randn(seq_length, batch_size, input_size)

# Forward pass through the model
output = model(input_data)
print(output.shape)  # Should be (batch_size, 1)
import torch
import torch.nn as nn

# Define the GRU model
class GRUNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(GRUNet, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.gru(x)
        out = self.fc(out[:, -1, :])
        return out

# Initialize the model
input_size = 10
hidden_size = 20
num_layers = 2
output_size = 1
model = GRUNet(input_size, hidden_size, num_layers, output_size)

# Create dummy input data
batch_size = 3
sequence_length = 5
x = torch.randn(batch_size, sequence_length, input_size)

# Forward pass
output = model(x)
print(output.shape)  # Expected output shape: (batch_size, output_size)
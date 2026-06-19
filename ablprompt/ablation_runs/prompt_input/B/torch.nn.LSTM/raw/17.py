import torch
import torch.nn as nn

# Define an LSTM model
class SimpleLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False):
        super(SimpleLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, bidirectional=bidirectional)
        self.fc = nn.Linear(hidden_size * (2 if bidirectional else 1), 1)

    def forward(self, x):
        h0 = torch.zeros(num_layers * (2 if self.lstm.bidirectional else 1), x.size(0), hidden_size).to(x.device)
        c0 = torch.zeros(num_layers * (2 if self.lstm.bidirectional else 1), x.size(0), hidden_size).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
sequence_length = 5
device = 'cpu'

model = SimpleLSTM(input_size, hidden_size, num_layers, bidirectional=True).to(device)
input_data = torch.randn(sequence_length, batch_size, input_size).to(device)
output = model(input_data)
print(output.shape)  # Should print torch.Size([3, 1])
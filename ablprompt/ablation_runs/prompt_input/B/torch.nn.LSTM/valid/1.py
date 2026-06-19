import torch
import torch.nn as nn

# Define an LSTM model with multiple layers and bidirectional processing
class BiLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(BiLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_size * 2, num_classes)  # Multiply by 2 for bidirectional

    def forward(self, x):
        h0 = torch.zeros(self.num_layers * 2, x.size(0), self.hidden_size).to(x.device)  # 2 for bidirectional
        c0 = torch.zeros(self.num_layers * 2, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.lstm(x, (h0, c0))  # out: tensor of shape (batch_size, seq_length, hidden_size*2)
        out = self.fc(out[:, -1, :])  # take only the last time step
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
num_classes = 5
batch_size = 3
seq_length = 5

model = BiLSTM(input_size, hidden_size, num_layers, num_classes)
input_data = torch.randn(batch_size, seq_length, input_size)
output = model(input_data)
print(output.shape)  # Should print: torch.Size([3, 5])
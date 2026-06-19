import torch
import torch.nn as nn

# Define a simple RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x, hidden):
        out, hidden = self.rnn(x, hidden)
        out = self.fc(out[-1, :, :])
        return out, hidden

# Initialize parameters
input_size = 10
hidden_size = 20
output_size = 5
batch_size = 3
seq_length = 4

# Create an instance of the RNN model
rnn_model = SimpleRNN(input_size, hidden_size, output_size)

# Generate random input data and initial hidden state
inputs = torch.randn(seq_length, batch_size, input_size)
hidden = torch.zeros(1, batch_size, hidden_size)

# Forward pass through the RNN model
output, new_hidden = rnn_model(inputs, hidden)

print("Output:", output)
print("New Hidden State:", new_hidden)
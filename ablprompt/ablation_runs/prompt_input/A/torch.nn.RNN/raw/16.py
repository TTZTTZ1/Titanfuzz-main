import torch
import torch.nn as nn

# Define an RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # Initialize hidden state with zeros
        h0 = torch.zeros(1, 1, self.hidden_size).to(x.device)
        
        # Forward propagate RNN
        out, _ = self.rnn(x, h0)
        
        # Decode the hidden state of the last time step
        out = self.fc(out[-1])
        return out

# Example usage
input_size = 10
hidden_size = 20
output_size = 1
batch_size = 5
sequence_length = 3

model = SimpleRNN(input_size, hidden_size, output_size)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Create dummy data
inputs = torch.randn(sequence_length, batch_size, input_size)
targets = torch.randn(batch_size, output_size)

# Forward pass
outputs = model(inputs)
loss = criterion(outputs, targets)

# Backward and optimize
optimizer.zero_grad()
loss.backward()
optimizer.step()

print(f'Loss: {loss.item()}')
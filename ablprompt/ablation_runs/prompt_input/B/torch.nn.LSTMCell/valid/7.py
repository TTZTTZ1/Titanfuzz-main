import torch
from torch.nn import LSTMCell

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = LSTMCell(input_size, hidden_size)

# Create random input and initial states
batch_size = 5
input_tensor = torch.randn(batch_size, input_size)
hx = torch.zeros(batch_size, hidden_size)
cx = torch.zeros(batch_size, hidden_size)

# Process input through LSTMCell
for i in range(3):  # Simulate 3 time steps
    hx, cx = lstm_cell(input_tensor, (hx, cx))

print("Final hidden state:", hx)
print("Final cell state:", cx)
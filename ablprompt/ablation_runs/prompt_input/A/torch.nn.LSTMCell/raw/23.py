import torch

# Initialize LSTMCell
input_size = 10
hidden_size = 20
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Input data and initial hidden state
input_data = torch.randn(5, input_size)  # Sequence of 5 inputs
hx = torch.zeros(1, hidden_size)
cx = torch.zeros(1, hidden_size)

# Forward pass through LSTMCell
hx, cx = lstm_cell(input_data, (hx, cx))

print("Output:", hx)
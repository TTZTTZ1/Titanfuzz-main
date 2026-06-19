import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial hidden/cell states
input_tensor = torch.randn(1, input_size)
hx = torch.randn(1, hidden_size)
cx = torch.randn(1, hidden_size)

# Forward pass through LSTMCell
hx, cx = lstm_cell(input_tensor, (hx, cx))

print("Updated hidden state:", hx)
print("Updated cell state:", cx)
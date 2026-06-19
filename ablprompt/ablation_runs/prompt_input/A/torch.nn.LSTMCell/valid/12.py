import torch

# Define input dimensions and hidden state dimensions
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input tensor and hidden state
input_tensor = torch.randn(1, input_size)
hidden_state = (torch.randn(1, hidden_size), torch.randn(1, hidden_size))

# Perform a single step of LSTM computation
new_hidden_state = lstm_cell(input_tensor, hidden_state)

print(new_hidden_state)
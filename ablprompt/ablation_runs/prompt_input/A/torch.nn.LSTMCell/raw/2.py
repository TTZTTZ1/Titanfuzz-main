import torch

# Define input size, hidden size, and batch size
input_size = 10
hidden_size = 20
batch_size = 32

# Create an LSTM cell instance
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Generate random input and hidden state
input_data = torch.randn(batch_size, input_size)
hidden_state = (torch.randn(batch_size, hidden_size), torch.randn(batch_size, hidden_size))

# Perform a forward pass through the LSTM cell
new_hidden_state = lstm_cell(input_data, hidden_state)

print(new_hidden_state)
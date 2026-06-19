import torch

# Define input size, hidden size and batch size
input_size = 10
hidden_size = 20
batch_size = 5

# Create an LSTMCell instance
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and hidden state
input_data = torch.randn(batch_size, input_size)
hidden_state = (torch.randn(batch_size, hidden_size), torch.randn(batch_size, hidden_size))

# Perform one step of LSTM computation
next_hidden_state, next_cell_state = lstm_cell(input_data, hidden_state)

print("Next Hidden State:", next_hidden_state)
print("Next Cell State:", next_cell_state)
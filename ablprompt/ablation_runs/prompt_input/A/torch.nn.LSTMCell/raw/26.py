import torch

# Define input dimensions and hidden size
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and hidden state
input_data = torch.randn(1, input_size)
hidden_state = torch.randn(1, hidden_size)
cell_state = torch.randn(1, hidden_size)

# Perform one step of LSTM computation
new_hidden_state, new_cell_state = lstm_cell(input_data, (hidden_state, cell_state))

print("New Hidden State:", new_hidden_state)
print("New Cell State:", new_cell_state)
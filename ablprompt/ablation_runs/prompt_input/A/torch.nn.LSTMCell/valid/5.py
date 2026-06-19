import torch

# Define input dimensions and hidden size for LSTM
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input tensor of shape (batch_size, input_size)
batch_size = 32
input_tensor = torch.randn(batch_size, input_size)

# Initialize hidden state and cell state
hidden_state = torch.zeros(batch_size, hidden_size)
cell_state = torch.zeros(batch_size, hidden_size)

# Perform one step of LSTM computation
next_hidden_state, next_cell_state = lstm_cell(input_tensor, (hidden_state, cell_state))

print("Next Hidden State:", next_hidden_state.shape)
print("Next Cell State:", next_cell_state.shape)
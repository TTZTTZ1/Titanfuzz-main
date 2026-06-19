import torch

# Define input size, hidden size, and batch size
input_size = 10
hidden_size = 20
batch_size = 5

# Create an instance of LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input tensor and hidden state
input_tensor = torch.randn(batch_size, input_size)
prev_hidden_state = torch.randn(batch_size, hidden_size)
prev_cell_state = torch.randn(batch_size, hidden_size)

# Forward pass through LSTMCell
next_hidden_state, next_cell_state = lstm_cell(input_tensor, (prev_hidden_state, prev_cell_state))

print("Next Hidden State:", next_hidden_state)
print("Next Cell State:", next_cell_state)
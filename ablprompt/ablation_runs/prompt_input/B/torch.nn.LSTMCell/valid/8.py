import torch
from torch.nn import LSTMCell

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = LSTMCell(input_size, hidden_size)

# Input data and initial hidden/cell states
input_data = torch.randn(5, 3, input_size)  # (seq_len, batch, input_size)
hx = torch.zeros(3, hidden_size)           # (batch, hidden_size)
cx = torch.zeros(3, hidden_size)           # (batch, hidden_size)

# Process sequence through LSTMCell
for i in range(input_data.size(0)):
    hx, cx = lstm_cell(input_data[i], (hx, cx))

print(hx.shape)  # Should print: torch.Size([3, 20])
print(cx.shape)  # Should print: torch.Size([3, 20])
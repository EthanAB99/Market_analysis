import torch
import torch.nn as nn

class LSTMClassifier(nn.Module)
    def __init__(self, input_size, hidden_size, num_layers, num_classes, dropout=0.2):
        super(LSTMClassifier, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, 
                            batch_first=True, dropout=dropout)
        self.fc = nn.Linear(hidden_size, num_classes)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)  # lstm_out: [batch_size, seq_len, hidden_size]
        out = lstm_out[:, -1, :]    # Get last time step
        out = self.fc(out)          # Final output
        return out  # For classification, logits are returned (no softmax if using CrossEntropyLoss)
# ACM AI SIG - Wine Quality Analysis

Neural network implementation for wine quality classification using the UCI Wine Quality dataset.

## Files

- `nn.py` - Main neural network implementation with PyTorch
- `wine_quality_correlation_heatmap.png` - Correlation visualization of wine features
- `wine_quality_distribution.png` - Distribution plot of wine quality ratings

## Features

- Multi-layer perceptron neural network
- UCI Wine Quality dataset integration
- Data preprocessing and visualization
- Training with validation metrics
- Automated plot generation

## Dependencies

```bash
pip install torch pandas numpy matplotlib seaborn scikit-learn ucimlrepo
```

## Usage

```bash
python nn.py
```

The script will automatically:
1. Download the UCI Wine Quality dataset
2. Preprocess the data
3. Train the neural network
4. Generate visualization plots
5. Display training metrics

## Output

The script generates two visualization files:
- Correlation heatmap showing relationships between wine features
- Distribution plot showing the distribution of wine quality ratings

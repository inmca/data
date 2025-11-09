# Common Plots Library

This folder contains minimal, clean implementations of common plots using matplotlib and seaborn with CSV datasets.

## Available Plots

1. **barplot.py** - Bar chart (iris.csv)
2. **heatmap.py** - Heatmap visualization (iris.csv)
3. **histogram.py** - Histogram (iris.csv)
4. **scatter_plot.py** - Scatter plot (iris.csv)
5. **line_plot.py** - Line plot with legend (iris.csv)
6. **boxplot.py** - Box plot (iris.csv)
7. **violin_plot.py** - Violin plot (iris.csv)
8. **pie_chart.py** - Pie chart (titanic_train.csv)
9. **area_plot.py** - Area plot (iris.csv)
10. **distribution_plot.py** - Distribution plot with KDE (winequality-white-1.csv)
11. **pairplot.py** - Pair plot (iris.csv)
12. **count_plot.py** - Count plot (titanic_train.csv)
13. **regression_plot.py** - Regression plot (iris.csv)

All plots include:

- CSV dataset loading from ./assets/ folder
- Title
- X and Y labels
- Legends (where applicable)
- Clean, minimal code
- Grid (where appropriate)

## Datasets Used

- **iris.csv** - Used for most plots (sepal/petal measurements by species)
- **titanic_train.csv** - Used for categorical plots (class distribution, counts)
- **winequality-white-1.csv** - Used for distribution plot

## Usage

Simply run any plot file:

```bash
python plots/barplot.py
```

Note: Requires pandas, matplotlib, and seaborn libraries. Ensure CSV files are in the `./assets/` folder.

### Author

    Farhang Jaryani - Postdoctoral Fellow - farhang.jaryani@bcm.edu, fxjaryan@texaschildrens.org
    The Gallo Brain Tumor Research Lab, Department of Pediatrics, Section of Hematology-Oncology, Baylor College of Medicine

# Gene Similarity Visualization Project

This project provides various visualizations of gene similarity based on a similarity matrix calculated between different genes.

## Features

- **Heatmap**: Visualizes gene similarity values as a color-coded grid.
- **Clustered Dendrogram**: Displays hierarchical clustering of genes based on their similarity.
- **Network Graph**: Visualizes gene pairs as nodes and edges with thickness representing similarity.
- **3D Similarity Matrix**: A 3D surface plot where each point represents similarity between two genes.
- **Bubble Chart**: Represents gene pairs with bubble sizes proportional to similarity values.
- **Bar Plot**: Shows the average similarity between each gene and all other genes.

## Sample Charts

Here are some sample visualizations generated by the project:

### 1. Heatmap

![Heatmap](images/heatmap.png)

### 2. Bubble Chart

![Bubble Chart](images/bubble_chart.png)

### 3. Network Graph

![Network Graph](images/network_graph.png)

### 4. Bar Plot

![Bar Plot](images/bar_plot.png)

## Requirements

To run the project, the following packages are required (available in `requirements.txt`):
- seaborn
- matplotlib
- pandas
- click
- numpy
- scipy
- networkx

## Usage

1. Clone the repository.
2. Install the necessary dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```
   The package is available on PyPI. You can install it using `pip`:

   ```bash
      pip install gene-similarity
   ```

3. Use the provided command-line interface to generate visualizations by running:

   ```bash
   python -m gene_similarity -f sample_genes_2.fa -l output_folder
   ```

This will generate various visualizations of gene similarity based on the input data.

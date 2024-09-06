import os
from abc import ABC, abstractmethod


class OutputHandlerBase(ABC):
    def __init__(self, similarity_map):
        self._similarity_map = similarity_map

    @abstractmethod
    def render(self, output_path):
        pass


class HeatmapOutputHandler(OutputHandlerBase):
    def render(self, output_path="stdout"):
        if output_path == "stdout":
            self._render_stdout()
        else:
            self._render_file(output_path)

    def _create_sim_table(self):
        # Calculate the dimension of the table (assuming square matrix)
        dimension = int(len(self._similarity_map) ** 0.5)
        result = [[0 for _ in range(dimension)] for _ in range(dimension)]
        column_names = self._extract_column_names()

        # Populate the result matrix with similarity values
        for gene_pair, similarity in self._similarity_map.items():
            row = column_names.index(gene_pair[0]._name)
            column = column_names.index(gene_pair[1]._name)
            result[row][column] = similarity
        return result

    def _render_stdout(self):
        table = self._create_sim_table()
        column_names = self._extract_column_names()
        first_row = [[""] + column_names]
        table = first_row + [
            [column_names[row_number]] + row for row_number, row in enumerate(table)
        ]
        with open("heatmap.csv", "w") as f:
            for row in table:
                f.write("\t".join(map(str, row)) + "\n")

    def _render_file(self, output_path):
        table = self._create_sim_table()
        column_names = self._extract_column_names()
        first_row = [[""] + column_names]
        table = first_row + [
            [column_names[row_number]] + row for row_number, row in enumerate(table)
        ]
        
        # Ensure the directory exists
        os.makedirs(output_path, exist_ok=True)
        
        heatmap_file = os.path.join(output_path, "heatmap.csv")
        with open(heatmap_file, "w") as f:
            for row in table:
                f.write("\t".join(map(str, row)) + "\n")

    def _extract_column_names(self):
        result = set()
        for gene_pair in self._similarity_map.keys():
            result.add(gene_pair[0]._name)  # Use the _name attribute
            result.add(gene_pair[1]._name)  # Use the _name attribute
        return sorted(result)

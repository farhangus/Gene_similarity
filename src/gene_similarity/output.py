from abc import ABC, abstractmethod
from pprint import pprint


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
        dimension = int(len(self._similarity_map) ** 0.5)
        result = [[0 for _ in range(dimension)] for _ in range(dimension)]
        column_names = self._extract_column_names()

        for gene_pair, similarity in self._similarity_map.items():
            row = column_names.index(gene_pair[0])
            column = column_names.index(gene_pair[1])
            result[row][column] = similarity
        return result

    def _render_stdout(self):
        table = self._create_sim_table()
        column_names = self._extract_column_names()
        first_row = [[""] + column_names]
        table = first_row + [
            [column_names[row_number]] + row for row_number, row in enumerate(table)
        ]
        for row in table:
            print("\t".join(map(str, row)))

    def _extract_column_names(self):
        result = set()
        for gene_pair in self._similarity_map.keys():
            result.add(gene_pair[0])
            result.add(gene_pair[1])
        return sorted(result, key=str)

    def _render_file(self, output_path):
        pass

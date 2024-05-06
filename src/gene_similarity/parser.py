class Parser:
    GENE_INDICATOR = ">"

    def __init__(self, file_path):
        self._file_path = file_path

    def parse(self):
        result = {}
        last_gene = None
        with open(self._file_path) as file:
            for line in file.readlines():
                line = line.strip()
                if line.startswith(Parser.GENE_INDICATOR):
                    gene_name = self._extract_gene_name(line)
                    last_gene = gene_name
                    continue
                result[last_gene] = line
        return result

    def _extract_gene_name(self, line):
        return line[1:]

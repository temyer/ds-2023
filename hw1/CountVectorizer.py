from typing import List

class CountVectorizer:
    def __init__(self, lowercase: bool = True) -> None:
        self.lowercase = lowercase
        self.__vocabulary = []


    def get_feature_names(self) -> List[str]:
        return self.__vocabulary


    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        self.__vocabulary = []

        if self.lowercase:
            corpus = map(str.lower, corpus)

        matrix: List[List[int]] = []

        for sentence in corpus:
            row = [0] * len(self.__vocabulary)
            for word in sentence.split():
                if word not in self.__vocabulary:
                    self.__vocabulary.append(word)
                    row.append(1)
                else:
                    idx = self.__vocabulary.index(word)
                    row[idx] += 1
            matrix.append(row)

        for row in matrix:
            voc_size = len(self.__vocabulary)
            row_size = len(row)
            if row_size < voc_size:
                row.extend([0] * (voc_size - row_size))

        return matrix

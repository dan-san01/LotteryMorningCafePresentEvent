import pandas as pd
import copy

class PreprocessModule:
    def __init__(self, df):
        self.df = df

    def removalDuplicate(self, header_name):
        """
        Get the element number that was duplicated by mistake for removing from dataframe 
            with handle names of its people.
        How : 
        1. Original handle name list -(minus) handle name list with duplicates removed.
        2. Get duplicate array number to search difference of 1. .
            but except when correctly applying (no_thinking_num = 0)
        """
        row_list = list(self.df[header_name])
        duplicate_list = copy.copy(row_list)
        delete_duplicate_list = list(set(row_list))

        count = 0
        for i in delete_duplicate_list:
            for j in duplicate_list:
                if i == j:
                    duplicate_list.remove(j)
                    break
            count += 1

        remain_array_num = []
        no_thinking_num = 0
        for duplicate_name in duplicate_list:
            one_remain_array_num = [i for i, x in enumerate(row_list) if x == duplicate_name]
            one_remain_array_num.pop(no_thinking_num)
            for array_num in one_remain_array_num:
                remain_array_num.append(array_num)
        return remain_array_num


def preprocessDataFrame(df, ShouldPreprocessExecute):
    """
    Preprocess of dataframe.
    """
    if ShouldPreprocessExecute:
        specified_headername = "ハンドルネームを入力してください"
        remove_array_nums = PreprocessModule(df).removalDuplicate(specified_headername)
        df = df.drop(index=df.index[remove_array_nums])
        return df
    else:
        return df
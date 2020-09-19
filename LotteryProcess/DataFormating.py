import pandas as pd

def generateOtherRandomNumbers(N_applicant, rdm_numbers):
    list_N_applicant = list(range(N_applicant))
    for i in rdm_numbers:
        list_N_applicant.remove(i)
    return list_N_applicant


def generateLotteryDataFrame(df, rdm_numbers):
    """
    Generate the lottery list of DataFrame type with the numbers in list.
    """
    header = df.columns.values
    lottery_df = pd.DataFrame(index=[], columns=header)
    for i in rdm_numbers:
        lottery_df = pd.concat([lottery_df, df[i:i+1]])
    return lottery_df
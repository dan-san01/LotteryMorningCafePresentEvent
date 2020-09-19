import pandas as pd
import random
import LotteryProcess

def main():
    """ init """
    lottery_num = 20
    ShouldPreprocessExecute = True 
    directory_path = "../100thAnniversary"
    present_list_fpath = directory_path + "/" + "present_list.csv"
    present_unable_list_fpath = directory_path + "/" + "present_unable_list.csv"
    lottery_list_fpath = directory_path + "/" + "lottery_list.csv"

    """ lottery process """
    print("Start the lottery process.")
    df = pd.read_csv(lottery_list_fpath)
    preprocessed_df = LotteryProcess.preprocess.preprocessDataFrame(df, ShouldPreprocessExecute)
    number_of_applicant = len(preprocessed_df)
    random_numbers = random.sample(range(number_of_applicant), k=lottery_num)
    other_random_numbers = LotteryProcess.DataFormating.generateOtherRandomNumbers(number_of_applicant, random_numbers)
    present_list_df = LotteryProcess.DataFormating.generateLotteryDataFrame(preprocessed_df, random_numbers)
    present_unable_list_df = LotteryProcess.DataFormating.generateLotteryDataFrame(preprocessed_df, other_random_numbers)
    present_list_df.to_csv(present_list_fpath)
    present_unable_list_df.to_csv(present_unable_list_fpath)
    print("End the lottery process.")

    return 0

if __name__=="__main__":
    main()
    #test_main()
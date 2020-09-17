import pandas as pd
import random
import copy

def main():
    choice_num = 10
    directory_name = "../100thAnniversary"
    fname = directory_name + "/" + "contact_list.csv"
    df = pd.read_csv(fname)

    #lottery process
    print("Start the lottery.")
    Lottery_df = df.sample(choice_num)
    write_winning_fname = directory_name + "/" + "winning_list.csv"
    Lottery_df.to_csv(write_winning_fname)
    print('write : {}'.format(write_winning_fname))
    print("End the lottery.")

    return 0

if __name__=="__main__":
    main()
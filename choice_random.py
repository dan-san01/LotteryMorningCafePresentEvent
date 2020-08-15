import pandas as pd
import random
import copy

def WriteCSV(write_fname, contact_list):
    write_df = pd.DataFrame([[contact_list[i]] for i in range(len(contact_list))])
    write_df.to_csv(write_fname)
    print('write : {}'.format(write_fname))
    return 0

def main():
    choice_num = 1
    directory_name = "../100thAnniversary"
    fname = directory_name + "/" + "contact_list.csv"
    df = pd.read_csv(fname)
    contact_info_list = list(set(df['連絡先となるDiscord IDもしくはTwitter IDを入力してください'].tolist()))
    defeat_info_list = copy.copy(contact_info_list)

    print("Start the lottery.")

    winning_list = random.sample(contact_info_list, choice_num)

    write_hit_fname = directory_name + "/" + "winning_list.csv"
    WriteCSV(write_hit_fname, winning_list)

    for contact_info in winning_list:
        defeat_info_list.remove(contact_info)

    write_defeat_fname = directory_name + "/" + "defeat_list.csv"
    WriteCSV(write_defeat_fname, defeat_info_list)

    print("End the lottery.")

    return 0

if __name__=="__main__":
    main()
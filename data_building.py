import pandas as pd
from sklearn.model_selection import train_test_split

raw_data_path = '/Users/sujayr/PycharmProjects/covidfaketweets/shortened_twitter_ids - twitter_ids_cleaned.csv'
destination_folder = '/Users/sujayr/PycharmProjects/covidfaketweets'

train_test_ratio = 0.10
train_valid_ratio = 0.80

first_n_words = 200

def trim_string(x):
    x = x.split(maxsplit=first_n_words)
    x = ' '.join(x[:first_n_words])
    return x

df_raw = pd.read_csv(raw_data_path)


#df_raw['label'] = (df_raw['label'] == '1').astype('int')
#print(df_raw['label'])
#df_raw['titletext'] = df_raw['title'] + ". " + df_raw['text']
df_raw['titletext'] = df_raw['title'].fillna("") + ". " + df_raw['text']

df_raw = df_raw.reindex(columns=['label', 'title', 'text', 'titletext'])

df_raw.drop( df_raw[df_raw.text.str.len() < 5].index, inplace=True)

df_raw['text'] = df_raw['text'].apply(trim_string)
df_raw['titletext'] = df_raw['titletext'].apply(trim_string)

df_real = df_raw[df_raw['label'] == 0]
df_fake = df_raw[df_raw['label'] == 1]

df_real_full_train, df_real_test = train_test_split(df_real, train_size = train_test_ratio, random_state = 1)
df_fake_full_train, df_fake_test = train_test_split(df_fake, train_size = train_test_ratio, random_state = 1)

df_real_train, df_real_valid = train_test_split(df_real_full_train, train_size = train_valid_ratio, random_state = 1)
df_fake_train, df_fake_valid = train_test_split(df_fake_full_train, train_size = train_valid_ratio, random_state = 1)

df_train = pd.concat([df_real_train, df_fake_train], ignore_index=True, sort=False)
df_valid = pd.concat([df_real_valid, df_fake_valid], ignore_index=True, sort=False)
df_test = pd.concat([df_real_test, df_fake_test], ignore_index=True, sort=False)

df_train.to_csv(destination_folder + '/train.csv', index=False)
df_valid.to_csv(destination_folder + '/valid.csv', index=False)
df_test.to_csv(destination_folder + '/test.csv', index=False)


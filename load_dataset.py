import torch
import spacy
from torchtext.legacy import data
# Models

import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence


label_field = data.Field(sequential=False, use_vocab=False, batch_first=True, dtype=torch.float)
text_field = data.Field(tokenize='spacy', lower=True, include_lengths=True, batch_first=True)
fields = [('label', label_field), ('title', text_field), ('text', text_field), ('titletext', text_field)]

# TabularDataset

train, valid, test = data.TabularDataset.splits(path='/Users/sujayr/PycharmProjects/covidfaketweets', train='train.csv', validation='valid.csv', test='test.csv',
                                           format='CSV', fields=fields, skip_header=True)

# Iterators

train_iter = data.BucketIterator(train, batch_size=32, sort_key=lambda x: len(x.text),
                             sort=True, sort_within_batch=True)
valid_iter = data.BucketIterator(valid, batch_size=32, sort_key=lambda x: len(x.text),
                             sort=True, sort_within_batch=True)
test_iter = data.BucketIterator(test, batch_size=32, sort_key=lambda x: len(x.text),
                            sort=True, sort_within_batch=True)

# Vocabulary

text_field.build_vocab(train, min_freq=3)
# -*- coding: utf8 -*-

import unittest
import os
from ccg_nlpy import local_pipeline

if os.path.exists('annotation-cache'):
    os.remove('annotation-cache')
lp = local_pipeline.LocalPipeline()


class TestLocalPipeline(unittest.TestCase):
    def setUp(self):
        self.lp = lp

    def test_doc(self):
        ta = self.lp.doc("Hello,  how are you.\n\n\n I am doing fine")
        tokens = [
            'Hello', ',', 'how', 'are', 'you', '.', 'I', 'am', 'doing', 'fine'
        ]
        self.assertEqual(ta.get_tokens, tokens)

        testarr = [6, 10]
        self.assertEqual(ta.get_sentence_end_token_indices, testarr)

        self.assertEqual(ta.get_score, 1.0)

        self.assertEqual(ta.get_text, "Hello,  how are you.\n\n\n I am doing fine")

    def test_doc_illigal_characters(self):
        ta = self.lp.doc(u"Hillary Clinton�s Candidacy Reveals Generational Schism Among Women https://t.co/6u3lmN7nIL")

        tokens = ['Hillary', 'Clintons', 'Candidacy', 'Reveals', 'Generational', 'Schism', 'Among', 'Women',
                  'https://t.co/6u3lmN7nIL']
        self.assertEqual(ta.get_tokens, tokens)

        self.assertEqual(ta.get_text,
                         "Hillary Clintons Candidacy Reveals Generational Schism Among Women https://t.co/6u3lmN7nIL")

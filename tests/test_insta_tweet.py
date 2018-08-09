#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `insta_tweet` package."""


import unittest
import tweepy
from insta_tweet import insta_tweet

class Testinsta_tweet(unittest.TestCase):

    def testinsta_tweet(self):
        response=insta_tweet.insta_tweet1('godemperormusk')
        self.assertEqual(response,"godemperormusk")

if __name__ == '__main__':
    unittest.main()

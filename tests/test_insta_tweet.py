#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `insta_tweet` package."""


import unittest
from click.testing import CliRunner

from insta_tweet import insta_tweet
from insta_tweet import cli

class TestInsta_tweet(unittest.TestCase):
    """Tests for `insta_tweet` package."""

    #def testapi_info(self):
    #    response=insta_tweet.insta_tweet('godemperormusk')
    #    self.assertEqual(response,"DONE")

    def test_insta_tweet(self):
        response=insta_tweet.insta_tweet('godemperormusk')
        self.assertEqual(response,"DONE")

if __name__ == '__main__':
    unittest.main()

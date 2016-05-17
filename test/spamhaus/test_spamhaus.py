import py.test

from csirtg_smrt import Smrt
from csirtg_smrt.rule import Rule
from cifsdk.constants import REMOTE_ADDR
from pprint import pprint

rule = 'rules/default/spamhaus.yml'
rule = Rule(path=rule)
rule.fetcher = 'file'
s = Smrt(REMOTE_ADDR, 1234, client='dummy')


def test_spamhaus_drop():
    rule.feeds['drop']['remote'] = 'test/spamhaus/drop.txt'
    x = s.process(rule, feed="drop")
    assert len(x) > 0


def test_spamhaus_edrop():
    rule.feeds['edrop']['remote'] = 'test/spamhaus/edrop.txt'
    x = s.process(rule, feed="edrop")
    assert len(x) > 0
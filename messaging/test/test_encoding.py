# -*- coding: utf-8 -*-
import unittest

from messaging.pdu import PDU

class TestEncodingFunctions(unittest.TestCase):

    def setUp(self):
        self.pdu = PDU()

    def test_encoding_7bit_message(self):
        number = "+34616585119"
        text = "hola"
        csca = "+34646456456"
        expected = "07914346466554F611000B914316565811F90000AA04E8373B0C"

        pdu = self.pdu.encode_pdu(number, text, csca=csca)[0]
        self.assertEqual(pdu[1], expected)

    def test_encoding_ucs2_message(self):
        number = "+34616585119"
        text = u'あ叶葉'
        csca = '+34646456456'
        expected = "07914346466554F611000B914316565811F90008AA06304253F68449"

        pdu = self.pdu.encode_pdu(number, text, csca=csca)[0]
        self.assertEqual(pdu[1], expected)

    def test_decoding_7bit_pdu(self):
        pdu = "07911326040000F0040B911346610089F60000208062917314080CC8F71D14969741F977FD07"
        expected = "How are you?"
        _csca = "+31624000000"
        number = "+31641600986"

        sender, datestr, text, csca, ref, cnt, seq, fmt = self.pdu.decode_pdu(pdu)
        self.assertEqual(text, expected)
        self.assertEqual(csca, _csca)
        self.assertEqual(number, sender)

    def test_decoding_ucs2_pdu(self):
        expected = u"中兴通讯"
        pdu = "07914306073011F0040B914316709807F2000880604290224080084E2D5174901A8BAF"
        _csca = "+34607003110"
        number = "+34610789702"

        sender, datestr, text, csca, ref, cnt, seq, fmt = self.pdu.decode_pdu(pdu)
        self.assertEqual(csca, _csca)
        self.assertEqual(number, sender)
        self.assertEqual(text, expected)


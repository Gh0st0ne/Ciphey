
def test_Hex_WUttUCRb():
    # {'PlainText Sentences': 'As we look forward to the beginning of a new millennium with new challenges and new opportunities, we can look back at the last century of Canadian history and state with certainty that Canada is rightly regarded, the world over, as an extraordinary success.', 'Encrypted Texts': {'PlainText': 'As we look forward to the beginning of a new millennium with new challenges and new opportunities, we can look back at the last century of Canadian history and state with certainty that Canada is rightly regarded, the world over, as an extraordinary success.', 'EncryptedText': '4173207765206c6f6f6b20666f727761726420746f2074686520626567696e6e696e67206f662061206e6577206d696c6c656e6e69756d2077697468206e6577206368616c6c656e67657320616e64206e6577206f70706f7274756e69746965732c2077652063616e206c6f6f6b206261636b20617420746865206c6173742063656e74757279206f662043616e616469616e20686973746f727920616e642073746174652077697468206365727461696e747920746861742043616e6164612069732072696768746c792072656761726465642c2074686520776f726c64206f7665722c20617320616e2065787472616f7264696e61727920737563636573732e', 'CipherUsed': 'Hex'}}
    res = ciphey.main('4173207765206c6f6f6b20666f727761726420746f2074686520626567696e6e696e67206f662061206e6577206d696c6c656e6e69756d2077697468206e6577206368616c6c656e67657320616e64206e6577206f70706f7274756e69746965732c2077652063616e206c6f6f6b206261636b20617420746865206c6173742063656e74757279206f662043616e616469616e20686973746f727920616e642073746174652077697468206365727461696e747920746861742043616e6164612069732072696768746c792072656761726465642c2074686520776f726c64206f7665722c20617320616e2065787472616f7264696e61727920737563636573732e')

    assert lc.checkLanguage(res) == True
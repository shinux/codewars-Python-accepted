"""
Caesar Ciphers are one of the most basic forms of encryption. It consists of a message and a key, and it shifts the letters of the message for the value of the key.

Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.

Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, numbers, spaces, and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!

"""
import string

def encryptor(key, message):
    _al = list(string.ascii_lowercase)
    _final = ''
    for i in message:
        if not i.isalpha():
            _final += i
            continue
        upper = False
        if i not in _al:
            _index = _al.index(i.lower()) + key
            upper = True
        else:
            _index = _al.index(i) + key
        while _index >= 26 or _index < -26:
            if _index >= 26:
                _index = _index -26
            elif _index < -26:
                _index = _index + 26
        _final += _al[_index].upper() if upper else _al[_index]
    return _final


if __name__ == '__main__':
    print(encryptor(27, 'Whoopi Goldberg'))
    print(encryptor(-5, 'Hello World!'))
    print(encryptor(-39,'Too Many Cooks.'))
    print(encryptor(-98, 'Fln'))
    print(encryptor(15, 'clr'))

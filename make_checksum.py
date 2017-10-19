#!/usr/bin/env python
# -*- coding: utf-8 -*-


from hashlib import md5


def md5_file(filename):
    """

    :param filename: 文件名包含路径
    :return: md5值
    """
    with open(filename, 'rb') as f:
        md5obj = md5()
        while 1:
            buf = f.read(1024)
            if not buf:
                break
            md5obj.update(buf)
    return md5obj.hexdigest()


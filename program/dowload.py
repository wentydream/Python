#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   实现文件下载,显示下载进度

import os
import requests

def download_file(url,save_path="1.png"):
    if save_path == "":
        save_path = url.split(os.path.sep)[-1]
    with requests.get(url, stream=True) as fget:
        # 此时只有响应头被下载
        file_size = int(fget.headers["Content-Length"])
        print('-' * 32)
        print(f"Name: {save_path}")
        print(f"Size: {file_size/(1000**2)}Mb")
        print(f"Link: {url}")
        print('-' * 32)
        chunk_size = 512
        file_done = 0
        with open(save_path, "wb") as fw:
            for chunk in fget.iter_content(chunk_size):
                fw.write(chunk)
                file_done = file_done + chunk_size
                percent = file_done / file_size
                if file_done <= file_size:
                    print(f"Download: {percent:.2%}", end='\r')
                else:
                    print("Download: 100%  ")


if __name__ == "__main__":
    download_file("https://www.baidu.com/img/flexible/logo/pc/result.png")
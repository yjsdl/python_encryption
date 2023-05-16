# -*- coding: utf-8 -*-
# @date：2023/5/16 14:11
# @Author：crab-pc
# @file： uploadfile
import hashlib
import io
import zipfile

# file = zipfile.ZipFile('安徽大学.zip', 'r')


with open(r'F:\mysubject\python_encryption\JsReverse\安徽大学.zip', 'rb') as f:
    file = f.read()

def get_md5():
    files = []
    spark = hashlib.md5()
    size = len(file)
    offset = 1024 * 1024 * 2
    chunks = file[:offset]
    files.append(chunks)

    cur = offset

    while cur < size:
        if cur + offset >= size:
            files.append(file[cur:cur+offset])
        else:
            mid = cur + int(offset/2)
            end = cur + offset
            files.append(file[cur:cur+2])
            files.append(file[mid:mid+2])
            files.append(file[end-2:end])
        cur += offset
    ones = b''
    for one in files:
        ones += one
    spark.update(ones)
    return spark.hexdigest()

def calculateHashSample(file: str) -> str:
    """想不到吧，文件摘要的hash"""
    s = 1024 * 1024 * 2
    md5 = hashlib.md5()
    with open(file, 'rb') as z_file_obj:
        md5.update(z_file_obj.read(s))
        while chuck := z_file_obj.read(s):
            if len(chuck) < s:
                md5.update(chuck)
                continue
            md5.update(chuck[:2])
            md5.update(chuck[int(s / 2): int(s / 2) + 2])
            md5.update(chuck[-2:])
    return md5.hexdigest()


# print(get_md5())
print(calculateHashSample(r'F:\mysubject\python_encryption\JsReverse\安徽大学.zip'))

"""47190191"""

# def upload_zip_file(file_absolute_path):
#     file_name = os.path.split(file_absolute_path)[-1]
#     upload_bug_file = (file_name, open(file, 'rb'), 'application/zip')
#     m = MultipartEncoder(fields={'file_name': file_name, 'file_path': upload_bug_file})
#     print("脚本上传文件：%s" % file)
#     resp = requests.post(url=SERVER_IP + UPLOAD_FILE, data=m, headers={'Content-Type': m.content_type})
#     print("上传file -=-=- status_code: %s, resp_text: %s" % (resp.status_code, resp.text))

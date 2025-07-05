# set_disk.py

# 노트북을 사용할 때 용량이 적어 주기적으로 확인 후 삭제 혹은 백업이 필요하다.

import shutil
import os

path = '/'

disk_info = shutil.disk_usage(path)
total = disk_info.total
used = disk_info.used
free = disk_info.free

if used/total > 0.8:
  print("사용량 경고")
  #os.remove()
  # 삭제
  # 백업

import time
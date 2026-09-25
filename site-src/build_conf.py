# check_site.py などから公開アドレスを参照するための小さなファイル（build.py の DOMAIN と同じ値を取り出す）
import re
DOMAIN = re.search(r"^DOMAIN = '([^']*)'", open('build.py', encoding='utf-8').read(), re.M).group(1)

# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
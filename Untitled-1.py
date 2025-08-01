chuoi = "ai! code python @dog 12dog$ hoc_vui"
"""   ket_qua = "a-@-h"   """
kq = []
for tu in chuoi.split():
  co_db = any(not c.isalpha() and not c.isdigit() for c in tu)
  ko_so = any(c.isalpha() for c in tu) and not any(c.isdigit() for c in tu)
  if co_db and ko_so:
    kq.append(tu)
  chu_dau = kq[0]
for tu in kq:
  chu_dau = tu[0]
print(chu_dau)
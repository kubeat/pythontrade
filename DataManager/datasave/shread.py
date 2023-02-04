import shelve
with shelve.open('localdata') as s:
  existing = s['key1']
print(existing)
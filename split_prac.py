'''
📋 Split() method: Used to split a string.

🧩 Parameters: separator(The delimiter according which to split the string)
of strings to  

(method) split: (sep: str | None = ..., maxsplit: SupportsIndex = ...) -> list[str]
Return a list of the words in the string, using sep as the delimiter string.

sep
  The delimiter according which to split the string. None (the default value) means 
  split according to any whitespace, and discard empty strings from the result.
maxsplit
  Maximum number of splits to do. -1 (the default value) means no limit.
'''
print('a'.split())
print('Another pop quiz to fun and learn!'.split(sep=' ', maxsplit=3))

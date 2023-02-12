'''How dict class works for an iterable ()

dict(iterable) -> new dictionary initialized as if via:
    d = {} 
    for k, v in iterable:
        d[k] = v
    # Here the iterable is this tuple ("py", "th", "on")
'''
print(dict(("py", "th", "on")))

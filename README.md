# Measurement Package

# Installation Instructions

```
git clone https://github.com/joliver92/measurement/
cd measurement
pip install -e . 
```
To import into your program clone to the base directory
```
from measurement import Measurement 
```
# Package use 
```
from measurement import Measurement
x = Measurement(8,4) 
y = Measurement(2,3)
x.value = 8 
x.error = 4 
x+y = 10 +/- 5
print(x) = 8 +/- 4 
```

TODO

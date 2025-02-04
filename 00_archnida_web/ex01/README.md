# SCORPIAN

Make Virtual Environment
```
python3 -m venv .venv
```

Enter your Virtual Environment
```
source .venv/bin/activate
```

Install requirement
```
pip install -r requirement.txt
```

## Run program
```
python3 scorpion.py FILE1 [FILE2 ...]
```
It display basic attributes such as the creation date, as well as EXIF data

EXIF stand for [Exchangeable image file format](https://en.wikipedia.org/wiki/Exif)

exit Virtual Environment
```
deactivate
```


```
>>> from PIL import Image
>>> im = Image.open('data/_DSC0629.jpg')
>>> im.save('this.png')
```
# Vogue Runway Scraper Made By Isurulkh
Scrapes high resolution images from [Vogue Runway](https://www.vogue.com/fashion-shows).


![](https://upload.wikimedia.org/wikipedia/commons/f/f8/VOGUE_LOGO.svg)


## Installation
```bash
pip install -r requirements.txt
```

# Download images from a specific runway show (edit this miu-miu and the event name )
```python
vogue.designer_show_to_download_images('miu-miu', 'spring-2024-ready-to-wear', './images')
```
# Download images from all shows for a specific designer(edit this miu-miu to your selected one)
```python
vogue.designer_to_download_images('miu-miu', './images')
```
# Get a list of all of the runway shows for a particular designer
```python
shows = vogue.designer_to_shows('miu-miu')
for show in shows:
    print(show)
```
#Finaly Run the Script
```pytho
python download_vogue_images.py
```
## Made By isurulkh
```python
Isuru Lakshan Ekanayaka
```


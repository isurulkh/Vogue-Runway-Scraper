import vogue

# Download images from a specific runway show
vogue.designer_show_to_download_images('miu-miu', 'spring-2024-ready-to-wear', './images')

# Download images from all shows for a specific designer
vogue.designer_to_download_images('miu-miu', './images')

# Get a list of all of the runway shows for a particular designer
shows = vogue.designer_to_shows('miu-miu')
for show in shows:
    print(show)

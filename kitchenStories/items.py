# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class KitchenstoriesItem(Item):
    # define the fields for your item here like:
    # name = Field()
    chinesename=Field(serializer=str)
    imgurl = Field(serializer=str)
    videourl=Field(serializer=str)
    videosourceurl = Field(serializer=str)
    catid=Field(serializer=str)
    catname=Field(serializer=str)
    source = Field(serializer=str)
    ngnixurl = Field(serializer=str)
    pass

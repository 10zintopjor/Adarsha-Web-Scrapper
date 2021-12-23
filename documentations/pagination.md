# adasha-web-parser

## Web Data

**Type:** Pagination

**Syntax:** 
```
id: uuid
annotation_type: Pagination
revision: '00001'
annotations:
  uuid:
    span:
      start: start span
      end: end span
    metadata:
      pbId: pbId
    imgnum: page number
    reference: https://files.dharma-treasure.org/{collection_name}/{collection_name+vol_number}/{image_name}.jpg
```
**Description:** An indication of correspondence with a page of a physical/image page.

**Text Sample:**

```
id: b2d2aad127bd45279f919cf0140d9ead
annotation_type: Pagination
revision: '00001'
annotations:
  f2494f5ede3b4afeb406d734bb83f7cf:
    span:
      start: 0
      end: 26
    metadata:
      pbId: 2977725
    imgnum: 1
    reference: https://files.dharma-treasure.org/degekangyur/degekangyur1-1/1-1-1a.jpg
```



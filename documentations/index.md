# adasha-web-parser

## Web Data

**Type:** Index

**Syntax:** 
```
id: uuid
annotation_type: index
revision: '00001'
annotations:
  uuid:
    work_id: sutraId
    parts:
      uuid:
        work_id: sutraId-volume_number
        span:
        - vol: volume number
          start: start span
          end: end span
```
**Description:** An indication of correspondence with a pagination and Sutra.

**Text Sample:**

```
id: 68f9113d7a7f4f97b1c61af77251e6d7
annotation_type: index
revision: '00001'
annotations:
  51f58796058b461ab32f3c972ee5417c:
    work_id: 6234008
    parts:
      3cbe647abf404688a79c24d14742826c:
        work_id: T1-1
        span:
        - vol: 1
          start: 27
          end: 396711
```



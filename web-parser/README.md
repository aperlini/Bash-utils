# Web Parser

Scrap any [bandcamp](https://bandcamp.com/) collection and transform it into a markdown checkbox's list

> `27/06/2025` : Server does not seem to accept this type of request anymore. This should be done using [Bandcamp API](https://bandcamp.com/developer) instead (TBD).

Usage :

```bash
./main.py <bandcamp-base-url> 
```

`output/artist-name-collection.md` : 

>  \# artist name
>
> \- [ ] \[album-name](url)
